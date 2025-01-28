main_bot_examples = [
    # QnA Examples (General Knowledge)
    {"input": "What is Machine Learning?", "intent": "qna"},
    {"input": "Tell me about photosynthesis.", "intent": "qna"},
    {"input": "How does a solar panel work?", "intent": "qna"},
    {"input": "Who is the President of the United States?", "intent": "qna"},
    {"input": "Explain the concept of quantum physics.", "intent": "qna"},
    {"input": "What are the benefits of exercise?", "intent": "qna"},
    {"input": "Can you help me with world history?", "intent": "qna"},
    {"input": "What is the capital of Japan?", "intent": "qna"},

    # Music Examples
    {"input": "Play some relaxing piano music.", "intent": "music"},
    {"input": "Find and play a jazz playlist.", "intent": "music"},
    {"input": "Play Arijit Singh's latest song.", "intent": "music"},
    {"input": "I want to listen to the theme song of Harry Potter.", "intent": "music"},
    {"input": "Play some workout music.", "intent": "music"},
    {"input": "Find a trending pop song for me.", "intent": "music"},
    {"input": "Can you play Lofi beats?", "intent": "music"},

    # Weather Examples
    {"input": "What's the weather like in New York?", "intent": "weather"},
    {"input": "How's the weather today in London?", "intent": "weather"},
    {"input": "Is it raining in Tokyo right now?", "intent": "weather"},
    {"input": "Tell me the weather in Sydney tomorrow.", "intent": "weather"},
    {"input": "What's the current temperature in Paris?", "intent": "weather"},
    {"input": "Is it sunny in California?", "intent": "weather"},

    # Reminder Examples
    {"input": "Remind me to call Sarah at 4 PM.", "intent": "reminder"},
    {"input": "Set a reminder to drink water at 3 PM.", "intent": "reminder"},
    {"input": "Can you remind me to take my medicine at 8 PM?", "intent": "reminder"},
    {"input": "Create a reminder for my meeting tomorrow at 10 AM.", "intent": "reminder"},
    {"input": "Remind me about my doctor's appointment at 7 AM.", "intent": "reminder"},
    {"input": "Set a reminder to wish John a happy birthday tomorrow morning.", "intent": "reminder"},
]


def main_prompt(user_input, few_shot_text):
    prompt = f"""
    You are an intent detection assistant. Your only task is to classify the user's input into one of the following intents:
    - qna: For general knowledge questions across a wide range of topics, such as science, history, technology, arts, health, and more.
    - music: For requests related to finding and playing music or playlists.
    - weather: For queries about current or future weather conditions in a specific location.
    - reminder: For creating reminders, such as tasks, appointments, or scheduled events.

    ### Rules:
    1. Only output the intent as one of the following: **qna**, **music**, **weather**, **reminder**, or **unknown**.
    2. Do not provide any explanation, interpretation, or additional details.
    3. If the user's input doesn't match any of the predefined intents, respond with **unknown**.

    ### Examples:
    {few_shot_text}

    ### Input:
    {user_input}

    ### Intent:
    """
    return prompt

