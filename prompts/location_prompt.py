few_shot_examples = [
    {"input": "What's the weather like in Paris?", "location": "Paris"},
    {"input": "Tell me the weather in Mumbai.", "location": "Mumbai"},
    {"input": "Weather forecast for Tokyo", "location": "Tokyo"},
    {"input": "Can you get the weather for New York?", "location": "New York"},
    {"input": "What's happening in Berlin?", "location": "Berlin"},
    {"input": "Weather in London today", "location": "London"},
    {"input": "Forecast for Los Angeles", "location": "Los Angeles"},
    {"input": "Is it raining in Tokyo?", "location": "Tokyo"},
    {"input": "Show me the weather for Hyderabad", "location": "Hyderabad"}
]


def location_extraction_prompt(user_input, examples):
    """
    Creates a prompt for extracting the location from a weather-related query.
    :param user_input: The user's query.
    :param examples: Few-shot examples for the LLM.
    :return: Prompt string.
    """
    example_text = "\n".join([f"Input: {ex['input']} Location: {ex['location']}" for ex in examples])
    return f"""
    You are a location extraction assistant. Your task is to extract only location from the user's weather-related query.
    The input will always be about weather, and you should strictly extract the location name, and avoid giving reasoning or explanations, just return the location from user input.

    Examples:
    {example_text}

    Input: {user_input}
    Location:
    """
