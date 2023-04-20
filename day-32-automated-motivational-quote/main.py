"""Entrypoint file to send Email using smtplib module"""
from email_sender import EmailSender

if __name__ == "__main__":
    """Entrypoint function to send Email"""
    EmailSender().send_email()
