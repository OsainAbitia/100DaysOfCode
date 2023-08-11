import os
from twilio.rest import Client

class TwilioNotifier:
    def __init__(self) -> None:
        self.twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
        self.target_phone_number = os.environ.get("TARGET_PHONE_NUMBER")

    def send_sms(self, message: str) -> None:
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        
        message = client.messages.create(
            from_=self.twilio_phone_number,
            body=message,
            to=self.target_phone_number
            )
        
        print(message.sid)