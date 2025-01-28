import pyttsx3
import speech_recognition as sr
from logger import CustomLogger
import threading

class SpeechModule:
    """
    Handles Speech-to-Text (STT) and Text-to-Speech (TTS) functionalities with wake word detection.
    """

    def __init__(self):
        """
        Initialize the SpeechModule with TTS engine and recognizer for STT.
        """
        self.logger = CustomLogger().get_logger()
        self.logger.info("Initializing SpeechModule.")

        # Initialize Text-to-Speech (TTS) engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty("rate", 150)
        self.tts_thread = None

        # Initialize Speech-to-Text recognizer
        self.recognizer = sr.Recognizer()

        # Control flags
        self.listening = False
        self.wake_word_thread = None
        self.wake_word_detected = False

    def speak(self, text: str):
        """
        Convert text to speech in a separate thread to allow interruption.
        """
        def tts_task():
            self.logger.info(f"TTS Output: {text}")
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except Exception as e:
                self.logger.error(f"Error in TTS: {e}")

        # Stop any ongoing TTS before starting a new one
        self.stop_tts()

        # Start the TTS task in a thread
        self.tts_thread = threading.Thread(target=tts_task)
        self.tts_thread.start()

    def stop_tts(self):
        """
        Stop any ongoing TTS operation.
        """
        if self.tts_thread and self.tts_thread.is_alive():
            self.logger.info("Stopping TTS...")
            self.tts_engine.stop()
            self.tts_thread.join()

    def listen_for_commands(self):
        """
        Activate Speech-to-Text after detecting the wake word.
        """
        self.logger.info("Listening for a command...")
        with sr.Microphone() as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio)
                self.logger.info(f"Command received: {command}")
                return command
            except sr.UnknownValueError:
                self.logger.warning("Could not understand the audio.")
                return None
            except sr.WaitTimeoutError:
                self.logger.warning("Listening timed out.")
                return None

    def wake_word_listener(self):
        """
        Continuously listen for the wake word ("hey infy" or "infy").
        """
        self.logger.info("Starting wake word detection...")
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            while True:
                try:
                    self.logger.info("Listening for wake word...")
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    recognized_text = self.recognizer.recognize_google(audio).lower()
                    self.logger.info(f"Recognized: {recognized_text}")

                    # Check for wake word
                    if "hey infy" in recognized_text or "infy" in recognized_text:
                        self.logger.info("Wake word detected! Ready to listen for commands.")
                        self.speak("Yes, I am listening.")
                        self.wake_word_detected = True

                        # Listen for a command after wake word is detected
                        command = self.listen_for_commands()
                        if command:
                            self.process_command(command)
                        self.wake_word_detected = False  # Reset flag after processing command

                except sr.UnknownValueError:
                    # Handle case where speech recognition can't understand the audio
                    self.logger.warning("Could not understand the audio.")
                except sr.RequestError as e:
                    # Handle request errors from the Google speech API
                    self.logger.error(f"Request error: {e}")
                except Exception as e:
                    # Catch any other errors
                    self.logger.error(f"Unexpected error: {e}")

    def process_command(self, command: str):
        """
        Process the recognized command and take appropriate actions.
        """
        if "play" in command.lower():
            self.speak("Playing your music.")
            # Integrate with your music module here
        elif "stop" in command.lower() or "pause" in command.lower():
            self.speak("Stopping the music.")
            # Integrate stop functionality here
        else:
            self.speak(f"I heard: {command}. But I don't understand it yet.")

    def start(self):
        """
        Start the wake word listener in a separate thread.
        """
        self.wake_word_thread = threading.Thread(target=self.wake_word_listener, daemon=True)
        self.wake_word_thread.start()
        self.logger.info("SpeechModule is running. Say 'Hey Infy' or 'Infy' to activate.")