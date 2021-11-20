import string
import random
import pyperclip


class PasswordGenerator():
    def __init__(self) -> None:
        # Characters to generate password from
        self.characters = list(string.ascii_letters +
                               string.digits + "!@#$%^&*()")

    def random_password(self):
        # shuffling the characters
        random.shuffle(self.characters)

        # picking random characters from the list
        password = []
        for i in range(12):
            password.append(random.choice(self.characters))

        # shuffling the resultant password
        random.shuffle(password)

        # converting the list to string
        # saving password to clipboard and return new password
        new_password = "".join(password)
        pyperclip.copy(new_password)
        return new_password
