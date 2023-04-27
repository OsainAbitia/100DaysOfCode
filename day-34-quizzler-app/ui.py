"""
This module contains the QuizInterface class.
"""
from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"

class QuizInterface():
    """
    This class is responsible for creating the user interface.
    """

    def __init__(self, quiz_brain: QuizBrain) -> None:
        """
        Initializes the QuizInterface class.

        Inputs:

        quiz_brain: QuizBrain object.
        """
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label configuration
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas question configuration
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Some Question Text", 
            width=280, 
            font=("Arial", 18, "italic"), 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons configuration
        TRUE_IMAGE = PhotoImage(file="images/true.png")
        self.true_button = Button(image=TRUE_IMAGE, highlightthickness=0, command=self.check_users_answer("True"))
        self.true_button.grid(row=2, column=0)

        FALSE_IMAGE = PhotoImage(file="images/false.png")
        self.false_button = Button(image=FALSE_IMAGE, highlightthickness=0, command=self.check_users_answer("False"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        """
        Displays nex question inside the quiz UI.

        get_next_question constantly updates the question
        prompt to the users and verifies if there's still
        available answers.
        """
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_users_answer(self, answer: bool) -> None:
        """
        Verifies if the answer provided by the user is correct.

        Inputs:

        answer: bool.
        """
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool) -> None:
        """
        Displays feedback to the user.

        Inputs:

        is_right: bool.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
