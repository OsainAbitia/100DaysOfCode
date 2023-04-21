"""Track ISS entrypoint."""
import logging
import time

from iss_tracker import ISSTracker
from email_sender import EmailSender

# Logger configurations
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

if __name__ == "__main__":
    """Start program."""
    
    iss_tracker = ISSTracker()
    email_sender = EmailSender()

    while True:
        if iss_tracker.is_above_me() and iss_tracker.is_visible():
            email_sender.send_email()
        else:
            logging.info('Nothing to report, Houston.')

        time.sleep(60)



