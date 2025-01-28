from datetime import datetime
import threading
import time
import re
from modules.speech import SpeechModule
from logger import CustomLogger  # Import CustomLogger
from modules.utils import normalize_time

class ReminderModule:
    """
    Handles reminder functionality, allowing users to set and manage reminders interactively.
    """

    def __init__(self):
        """
        Initialize the Reminder Module.
        """
        self.reminders = []  # Store active reminders
        self.conversation_context = {}  # Store intermediate states for interactive reminder setting
        self.speech_module = SpeechModule()  # Initialize speech module for TTS

        # Initialize logger
        self.logger = CustomLogger().get_logger()
        self.logger.info("ReminderModule initialized.")

    def set_reminder(self, reminder_time, message):
        """
        Create a background thread that triggers at the exact reminder_time (12-hour format).
        """
        def reminder_thread():
            while True:
                current_time = datetime.now().strftime("%I:%M %p")  # 12-hour format
                if current_time == reminder_time:
                    # Interrupt ongoing TTS and announce the reminder
                    self.speech_module.stop_tts()
                    self.speech_module.speak(f"Reminder: {message}")
                    self.logger.info(f"Reminder triggered: {message} at {reminder_time}")
                    break
                time.sleep(1)

        self.reminders.append({"time": reminder_time, "message": message})
        threading.Thread(target=reminder_thread, daemon=True).start()
        self.logger.info(f"Reminder set: '{message}' for {reminder_time}")

    def handle_reminder(self, user_input):
        """
        Handles setting reminders interactively with the user.
        :param user_input: The user's input for setting a reminder.
        :return: Response message to guide the user or confirm the reminder.
        """
        self.logger.info(f"Handling reminder input: {user_input}")

        # Handle "exit" command explicitly
        if user_input.lower() == "exit":
            self.conversation_context.clear()  # Clear any active context
            self.logger.info("Exited the reminder functionality. Active reminders will still trigger.")
            return "Exited the reminder functionality. Active reminders will still trigger."

        # If there's a pending action in conversation_context, continue that flow
        if "pending_action" in self.conversation_context:
            action = self.conversation_context.pop("pending_action")
            if action == "set_reminder_time":
                # Normalize time input
                normalized_time = normalize_time(user_input)
                if not normalized_time:
                    self.logger.warning(f"Invalid time format: {user_input}")
                    self.conversation_context["pending_action"] = "set_reminder_time"
                    return "Invalid time format. Please provide the time in HH:MM AM/PM format (e.g., 02:30 PM)."
                self.conversation_context["reminder_time"] = normalized_time
                self.conversation_context["pending_action"] = "set_reminder_message"
                self.logger.info(f"Reminder time set: {normalized_time}")
                return "What should I remind you about?"
            elif action == "set_reminder_message":
                # Now we have time and message, we can set the reminder
                reminder_time = self.conversation_context.pop("reminder_time")
                reminder_message = user_input
                self.set_reminder(reminder_time, reminder_message)
                return f"Reminder set for {reminder_time} with message: '{reminder_message}'"

        # Start the reminder setting process
        self.conversation_context["pending_action"] = "set_reminder_time"
        self.logger.info("Starting reminder setup process.")
        return "What time should I set the reminder for? (e.g., 02:30 PM)"
