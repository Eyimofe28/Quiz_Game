class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        question = self.question_list[self.question_number].question
        solution = self.question_list[self.question_number].answer
        self.question_number += 1

        ask_user = input(f"Q.{self.question_number}: {question} (true/false)?: ").lower()
        self.check_answer(ask_user, solution)

    def check_answer(self, user_input, solution):
        if user_input.title() == solution:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")

        print(f"The correct answer was {solution}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")
