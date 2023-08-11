"""Entrypoint for the application"""
from stock_tracker import StockTracker
from twilio_notifier import TwilioNotifier

stock = StockTracker()

if __name__ == "__main__":
    stock_update = stock.compare_stock_prices()
    if stock_update:
        message = stock.get_company_news()
        notifier = TwilioNotifier()
        notifier.send_sms(message)
    else:
        print("No update on stock prices")
