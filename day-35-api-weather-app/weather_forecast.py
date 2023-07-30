"""Weather forecaster logic."""
import os
import requests
from twilio.rest import Client

# Constant variables
WEATHER_CONDITION_CODES = {
    '200': 'thunderstorm',
    '300': 'drizzle',
    '500': 'rain',
    '600': 'snow',
    '700': 'atmosphere',
    '800': 'clear',
    '801': 'clouds'
}

WEATHER_CONDITION_MESSAGES = {
    'thunderstorm': 'stay at home',
    'drizzle': 'use umbrella',
    'rain': 'use raincoat',
    'snow': 'use snowshoes',
    'atmosphere': 'stay at home',
    'clear': 'enjoy the sun!',
    'clouds': 'go outside'
}

class Forecaster:
    """Weather forecaster class initializer."""

    def __init__(self) -> None:
        """Initialize the forecaster."""
        self.weather_api_key = os.environ.get('WEATHER_API_KEY')
        self.latitude = os.environ.get('LATITUDE', '24.05718')
        self.longitude = os.environ.get('LONGITUDE', '-107.689')
        self.owm_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
        self.weather_params = {
            'lat': self.latitude,
            'lon': self.longitude,
            'appid': self.weather_api_key
        }

    def get_hourly_forecast(self) -> dict:
        """Get forecast of weather condition each hour.
        
        As part of API request, current, minutely, and daily
        forecasts are excluded.
        
        Returns:
            dict: Hourly main weather conditions.
        """
        exclude = {'exclude': 'current,minutely,daily'}
        hourly_weather_params = self.weather_params.update(exclude)

        response = requests.get(self.owm_endpoint, params=hourly_weather_params)
        response.raise_for_status()

        weather_data = response.json()
        # From hourly weather data list, return only the first 12 elements
        weather_slice = weather_data['hourly'][:12]
        for hour_data in weather_slice:
            condition_code = hour_data['weather'][0]['id']
            self.__describe_condition(condition_code)

    
    def __describe_condition(self, condition_code: str) -> None:
        """Translate current condition id into real weather.
        
        Given a condition id, translate it into a human-readable
        string.
        
        Args:
            condition_code (str): Current condition id.
        
        Returns:
            str: Human-readable weather message.
        """
        # Condition code 700 doesn't exist so we recode it to the 
        # next available condition code
        if condition_code == 700:
            condition_code += 1

        translated_condition = WEATHER_CONDITION_CODES.get(condition_code, "a crazy day")
        suggestion = WEATHER_CONDITION_MESSAGES.get(translated_condition, "stay alert")

        message = f"You can expect {translated_condition}, don't forget to {suggestion}"

        if translated_condition == 'rain':
            self.__send_sms(message)

    def __send_sms(self, message: str) -> None:
        """Initialize Twilio Client given the specific condition.
        
        Args:
            message (str): Human-readable weather message.
        """
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_API_KEY')
        client = Client(account_sid, auth_token)

        sms = client.messages \
            .create(
                body=message,
                from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                to=os.environ.get('MY_PHONE_NUMBER')
            )
        print(sms.status)