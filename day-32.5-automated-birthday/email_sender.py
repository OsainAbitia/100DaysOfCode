"""Email sender contains the logic to send emails to users."""
import os,random
import smtplib

from scheduler import Scheduler

class EmailSender():
    """Main class to send emails."""
    def __init__(self) -> None:
        """Initialize the email sender."""
        self.email_from = os.environ.get("EMAIL_FROM")
        self.email_password = os.environ.get("EMAIL_PASSWORD")
        self.email_to = os.environ.get("EMAIL_TO")

        self.message_template = self.get_letter_template()

    def get_letter_template(self) -> str:
        """Return a random letter template from ./letter_templates/ as string"""
        file = random.choice(os.listdir("./letter_templates/"))
        with open(f"./letter_templates/{file}", "r") as f:
            return f.read()
    
    def send_email(self, message) -> None:
        """Send an email."""
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.email_from, self.email_password)
            connection.sendmail(
                from_addr=self.email_from, 
                to_addrs=self.email_to, 
                msg=f"Subject: New message\n\n{message}\n"
            )

    def check_birthdays(self):
        """Check if there are birthdays today."""
        birthdays = Scheduler().get_birthdays()

        if len(birthdays) == 0:
            return "There are no birthdays today."
        else:
            for friend in birthdays:
                message = self.message_template.replace("[NAME]", friend["name"])
                self.send_email(message)