"""Email sender contains the logic to send emails to users."""
import os
import smtplib

class EmailSender():
    """Main class to send emails."""
    def __init__(self) -> None:
        self.email_from = os.getenv("EMAIL_FROM")
        self.email_password = os.getenv("PASSWORD")
        self.email_to = os.getenv("EMAIL_TO")

    def send_email(self) -> None:
        """Send email to user."""
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email_from, password=self.email_password)
            connection.sendmail(
                from_addr=self.email_from,
                to_addrs=self.email_to,
                msg="Subject:ISS Tracker update!\n\nLook up! ISS is above you in the sky.\n"
            )