import os
import requests

class StockTracker:

    def __init__(self) -> None:
        self.stock = os.environ.get("STOCK", "TSLA")
        self.company_name = os.environ.get("COMPANY_NAME", "Tesla Inc")
        self.stock_tracker_api_key = os.environ.get("STOCK_TRACKER_API_KEY")
        self.stock_tracker_api_url = "https://www.alphavantage.co/query"
        self.stock_tracker_api_function = "TIME_SERIES_DAILY"
        self.stock_news_api_key = os.environ.get("STOCK_NEWS_API_KEY")
        self.stock_news_api_url = "https://newsapi.org/v2/everything"

    def __retrieve_stock_data(self) -> dict:
        stock_params = {
            "function": self.stock_tracker_api_function,
            "symbol": self.stock,
            "apikey": self.stock_tracker_api_key,
            "datatype": "json",
            "outputsize": "compact"
        }
        
        response = requests.get(self.stock_tracker_api_url, params=stock_params)
        response.raise_for_status()
        daily_time_series = response.json()["Time Series (Daily)"]
        return list(daily_time_series.values())[1:3]
    
    def compare_stock_prices(self) -> bool:
        yesterday_price, day_before_yesterday_price = self.__retrieve_stock_data()
        yesterday_price = yesterday_price["4. close"]
        day_before_yesterday_price = day_before_yesterday_price["4. close"]

        change_percentage = (float(yesterday_price) - float(day_before_yesterday_price)) / float(day_before_yesterday_price) * 100
        self.change_percentage = round(change_percentage)

        return self.change_percentage > 5 or self.change_percentage < -5

    def get_company_news(self) -> dict:
        news_params = {
            "q": self.company_name,
            "apiKey": self.stock_news_api_key
        }

        response = requests.get(self.stock_news_api_url, params=news_params)
        latest_news = response.json()['articles'][:3]

        news = ""
        for article in latest_news:
            article_title = article["title"]
            article_description = article["description"]
            news += f"{self.stock}: {self.change_percentage}%\nHeadline: {article_title}\nBrief: {article_description}\n\n"

        return news

        