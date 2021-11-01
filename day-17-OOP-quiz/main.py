from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a dict of questions using our class Question
question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

# Send question bank to quiz brain and start the game
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(
    f"Your final score is {quiz.score}/{quiz.question_number}, let's go for a drink to celebrate 😎🍺")
