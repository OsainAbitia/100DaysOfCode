"""Orchestrate email sending for the application."""
import datetime as dt
import random

class Scheduler():
    """Schedule emails to be sent."""

    def __init__(self):
        """Initialize the Scheduler."""
        self.current_timestamp = dt.datetime.now()
        self.quotes = self.get_quotes()

    def get_quotes(self) -> list:
        """Read motivational quotes from ./quotes.txt."""
        with open('./quotes.txt', 'r') as f:
            quotes = f.readlines()
        return quotes
    
    def motivational_monday(self, weekday: int = 2) -> str:
        """Return motivational quote from ./quotes.txt on Monday."""
        if weekday == self.current_timestamp.weekday():
            return random.choice(self.quotes)
        else:
            return "Come back Monday for a motivational quote"