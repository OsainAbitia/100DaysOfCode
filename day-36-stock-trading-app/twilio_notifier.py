"""Twilio notifier class"""
import os
from twilio.rest import Client

class TwilioNotifier:
    """Initialize class."""

    def __init__(self) -> None:
        """Retrieve env variables
        
        Variable description as well as were to get them
        can be found inside the README.md file
        """
        self.twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
        self.target_phone_number = os.environ.get("TARGET_PHONE_NUMBER")

    def send_sms(self, message: str) -> None:
        """Send SMS message.
        
        Args:
            message (str): Message to be sent.
        """
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        
        message = client.messages.create(
            from_=self.twilio_phone_number,
            body=message,
            to=self.target_phone_number
            )
        
        print(message.sid)