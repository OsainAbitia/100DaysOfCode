"""Email sender contains the logic to send emails to users."""
import os
import smtplib

from scheduler import Scheduler

class EmailSender():
    """Main class to send emails."""
    def __init__(self) -> None:
        """Initialize the email sender."""
        self.email_from = os.environ.get("EMAIL_FROM")
        self.email_password = os.environ.get("EMAIL_PASSWORD")
        self.email_to = os.environ.get("EMAIL_TO")

        self.message = Scheduler().get_quotes()

    
    def send_email(self) -> None:
        """Send an email."""
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.email_from, self.email_password)
            connection.sendmail(
                from_addr=self.email_from, 
                to_addrs=self.email_to, 
                msg=f"Subject: New message\n\n{self.message}\n"
            )