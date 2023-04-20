"""Orchestrate email sending for the application."""
import datetime as dt
import pandas as pd

class Scheduler():
    """Schedule emails to be sent."""

    def __init__(self):
        """Initialize the Scheduler."""
        self.current_timestamp = dt.datetime.now()

    def wish_happy_birthday(self) -> list:
        """Read birthday CSV and wish happy birthday to the matching users."""
        birthdays = {}

        df = pd.read_csv('birthdays.csv')
        friends = df.to_dict(orient="records")
        for friend in friends:
            if friend['month'] == self.current_timestamp.month and \
                friend['day'] == self.current_timestamp.day:
                    self.birthdays.update({friend['name']: friend['email']})
        
        return birthdays
