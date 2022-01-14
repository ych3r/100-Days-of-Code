class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        u_answer = input(f"Q.{self.q_number}: {current_q.text} (True/False)?: ")
        self.check_answer(u_answer, current_q.answer)

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")
