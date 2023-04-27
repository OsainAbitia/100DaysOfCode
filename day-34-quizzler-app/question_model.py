"""Structure the questions and answers format."""

class Question:
    """Main class for question model."""

    def __init__(self, q_text, q_answer) -> None:
        """Initiate the question model."""

        self.text = q_text
        self.answer = q_answer
