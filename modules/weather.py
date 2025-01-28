import requests
from langchain_groq import ChatGroq
from modules.utils import weather_description_fetcher
from logger import CustomLogger
from modules.utils import extract_location


class WeatherModule:
    """
    Handles weather-related functionality, including fetching weather details for a given location.
    """

    def __init__(self, api_key):
        """
        Initialize the Weather Module.
        """

        self.llm = ChatGroq(
            api_key=api_key,
            model="llama3-8b-8192",
            temperature=0.7
        )
        # Initialize logger
        self.logger = CustomLogger().get_logger()
        self.logger.info("WeatherModule initialized.")
        


    @staticmethod
    def fetch_weather(location):
        """
        Fetches the weather details for a given location using the Open-Meteo API.
        :param location: Location for which weather needs to be fetched.
        :return: Weather details or an error message.
        """
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}"

        try:
            # Fetch latitude and longitude
            geocode_response = requests.get(geocode_url)
            geocode_response.raise_for_status()
            geocode_data = geocode_response.json()

            if "results" not in geocode_data or len(geocode_data["results"]) == 0:
                CustomLogger().get_logger().warning(f"No weather details found for location: {location}")
                return f"Sorry, I couldn't find weather details for '{location}'. Please try the same or another location."

            latitude = geocode_data["results"][0]["latitude"]
            longitude = geocode_data["results"][0]["longitude"]
            location_name = geocode_data["results"][0]["name"]

            # Fetch weather details
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            weather_response = requests.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

            if "current_weather" in weather_data:
                current_weather = weather_data["current_weather"]
                temperature = current_weather["temperature"]
                windspeed = current_weather["windspeed"]
                weather_code = current_weather.get("weathercode", -1)

                weather_description = weather_description_fetcher(weather_code)

                temperature_description = (
                    "hot" if temperature > 30 else "cold" if temperature < 15 else "moderate"
                )

                weather_message = (f"The current weather in {location_name} is {weather_description} with a temperature of "
                                   f"{temperature}°C ({temperature_description}) and a windspeed of {windspeed} km/h.")
                CustomLogger().get_logger().info(f"Weather fetched successfully for {location_name}: {weather_message}")
                return weather_message
            else:
                CustomLogger().get_logger().warning(f"Weather details not available for {location}.")
                return "Sorry, I couldn't fetch the weather details at this time."

        except requests.exceptions.RequestException as e:
            CustomLogger().get_logger().error(f"Error fetching weather data for {location}: {e}")
            return f"An error occurred while fetching weather data: {e}"

    def handle_weather(self, user_input):
        """
        Handles weather-related queries interactively with the user.
        :param user_input: The location or command related to weather.
        :return: Response message or weather details.
        """
        self.logger.info(f"Handling weather query: {user_input}")

        # Extract location from the input
        location = extract_location(user_input, self.llm)
        self.logger.info(f"Extracted location: {location}")

        # Fetch weather for the extracted location
        response = self.fetch_weather(location)
        self.logger.info(f"Weather response: {response}")
        return response
