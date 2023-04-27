"""Format and handle quiz logic after user's respond. """
import html

class QuizBrain:
    """This class handles logic of quiz."""

    def __init__(self, q_list:list[str]) -> None:
        """
        Initialize quiz with list of questions.
        
        Inputs:

        - q_list: list[str], list of questions.
        
        Outputs:

        - None.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """
        Validate remaining questions.
        
        Outputs:

        - bool, True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """
        Show next question after user's response.
        
        Outputs:

        - str, next question.
        
        Example:

        - Q.1: What is the capital of France? (True/False): True
        
        - Q.2: What is the capital of Germany? (True/False): False
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False): "
    
    def check_answer(self, user_answer:str) -> None:
        """
        Compare if the user's the user's response is correct and increase score.
        
        Inputs:

        - users_answer: str, user's answer.
        
        Outputs:

        - None.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
