# Summary

Weather App uses [OpenWeather API](https://openweathermap.org/) to 
fetch the next 12 hours conditions and send SMS messages with the
[Twilio API](https://www.twilio.com/es-mx/docs) within rain conditions
in order to remember user to carry an umbrella.

Alongside OOP, we create the Forecaster class that allows get the hourly
forecast, then, according to the status within the API response which is
compared against a constant dictionary, we are able to find the desired
condition to notify users, this `condition code` dictionary avoids creating 
multiple if statements for building a message containing the condition and
a suggestion action, then this message will be send with Twilio.

## Usage

In order to run the following script, do:

1. Create a OpenWeather account
2. Create a Twilio account
3. Get the longitude and latitude of your city

Then, just create some env vars

Variable | Description 
--- | ---
WEATHER_API_KEY | (Required) OpenWeather API key |
LATITUDE | (Optional) Your city latitude, default belongs to Durango, MX |
LONGITUDE | (Optional) Your city longitude, default belongs to Durango, MX |
TWILIO_ACCOUNT_SID | (Required) You can find it on the Twilio console|
TWILIO_API_KEY | (Required) Development or production, also on the Twilio console |
TWILIO_PHONE_NUMBER | (Required) The provided phone number by Twilio |
MY_PHONE_NUMBER | (Required) The phone number where the SMS willa arrive, don't forget to verify it|


