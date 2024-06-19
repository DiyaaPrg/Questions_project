from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


question_bank = []
for question in question_data:
    question_var = Question(text=question["question"], answer=question["correct_answer"])  # Question Object
    question_bank.append(question_var)


quiz = Quizbrain(question_bank)        # Sending the list of questions to Quizbrain class by quiz object
while quiz.still_has_question():
    quiz.next_question()
else:
    print("You've completed the quiz.")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
