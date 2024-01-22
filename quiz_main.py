from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

print('WELCOME TO MY QUIZ GAME!!!')
print('{Select the correct answers for the following questions}')
question_bank = []
for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_data = Question(question_text, question_answer)
    question_bank.append(new_data)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f'Your final score is {quiz.score}/{quiz.question_number}')
