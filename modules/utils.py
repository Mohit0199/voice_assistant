from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from prompts.location_prompt import location_extraction_prompt, few_shot_examples

@staticmethod
def normalize_time(user_input):
    """
    Normalize unconventional time inputs into a valid 12-hour HH:MM AM/PM format.
    For example:
    - '8:54 p.m.' -> '08:54 PM'
    - '854pm' -> '08:54 PM'
    - '443pm' -> '04:43 PM'
    - '9pm' -> '09:00 PM'
    """
    import re
    from datetime import datetime

    # Clean input: Remove unwanted characters like '.' and extra spaces
    user_input = re.sub(r'[^\w\s:]', '', user_input).strip()

    # Match valid time formats (HH, HH:MM, compact HHMM, optional AM/PM)
    match = re.match(r'(\d{1,4})(AM|PM|am|pm)?', user_input, re.IGNORECASE)
    if not match:
        return None  # Invalid input

    raw_time = match.group(1)  # Extract the numeric part
    period = match.group(2).upper() if match.group(2) else "PM"  # Default to PM if not provided

    # Handle compact time formats (e.g., 443 -> 4:43)
    if len(raw_time) in [3, 4]:  # HHMM or HMM formats
        hour = int(raw_time[:-2])  # Extract hour (first 1-2 digits)
        minute = int(raw_time[-2:])  # Extract minute (last 2 digits)
    elif len(raw_time) in [1, 2]:  # HH format
        hour = int(raw_time)
        minute = 0
    else:
        return None  # Invalid format

    # Validate hour range
    if hour < 1 or hour > 12:
        return None

    # Adjust for invalid minute range
    while minute >= 60:
        hour += 1
        minute -= 60

    # Convert to 12-hour format
    try:
        normalized_time = datetime.strptime(f"{hour}:{minute:02d} {period}", "%I:%M %p")
        return normalized_time.strftime("%I:%M %p")
    except ValueError:
        return None  # Invalid after adjustment

    
def weather_description_fetcher(weather_code):
    weather_conditions = {
                    0: "Clear sky",
                    1: "Mainly clear",
                    2: "Partly cloudy",
                    3: "Overcast",
                    45: "Foggy",
                    48: "Depositing rime fog",
                    51: "Light drizzle",
                    53: "Moderate drizzle",
                    55: "Dense drizzle",
                    61: "Slight rain",
                    63: "Moderate rain",
                    65: "Heavy rain",
                    71: "Slight snow",
                    73: "Moderate snow",
                    75: "Heavy snow",
                    80: "Rain showers",
                    81: "Moderate rain showers",
                    82: "Heavy rain showers",
                    95: "Thunderstorm",
                    96: "Thunderstorm with hail",
                }
    weather_description = weather_conditions.get(weather_code, "Unknown conditions")
    return weather_description

@staticmethod
def extract_location(user_input, llm):
    """
    Uses the Groq LLM to extract the location from the user's query.
    :param user_input: The user's query.
    :param llm: The initialized LLM object.
    :return: Extracted location or None.
    """
    prompt = location_extraction_prompt(user_input, few_shot_examples)
    messages = [
        {"role": "system", "content": "You are a location extraction assistant."},
        {"role": "user", "content": prompt}
    ]

    response = llm.invoke(messages)
    location = response.content.strip()
    return location if location else None
