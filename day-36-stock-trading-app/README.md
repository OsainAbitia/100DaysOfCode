# Summary

Day 36 for stock trading app uses [Alpha Ventage API](https://www.alphavantage.co) for 
retrieving stock data from the past 3 days. If the desired stock has a increment or
decrement of at least 5% we look for the most recent news of the company with [News Api](https://newsapi.org).

Once all our data has been retrieved, we then send SMS notification with Twilio to our desired number.

# Usage

In order to run the following script, do:

1. Create an Alpha Ventage API account
2. Create a Twilio account
3. Create a News Api account

Import the following variables (Format inside `.env.example`)

Variable | Description 
--- | ---
STOCK | (Optional) Stock name, default is `TSLA` |
COMPANY_NAME | (Optional) Company name, default is `Tesla Inc` |
STOCK_TRACKER_API_KEY | (Required) API from Alpha Ventage API |
STOCK_NEWS_API_KEY | (Required) API from News API |
TWILIO_ACCOUNT_SID | (Required) You can find it on the Twilio console |
TWILIO_AUTH_TOKEN | (Required) Development or production, also on the Twilio console |
TWILIO_PHONE_NUMBER | (Required) The provided phone number by Twilio |
TARGET_PHONE_NUMBER | (Required) The phone number where the SMS willa arrive, don't forget to verify it|
