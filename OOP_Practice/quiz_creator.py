class Question:
    def __init__(self, prompt: str, correct_answer: str):
        self.prompt = prompt
        self.correct_answer = correct_answer


class Quiz:
    def __init__(self, name: str):
        self.name = name
        self.questions = []

    def add_questions(self, question):
        self.questions.append(question)
    
    def display(self):
        print(f"-----------\n{self.name}")
        for question in self.questions:
            print("--------------")
            print(question.prompt)
            user_ans = input("Response: ")
            if user_ans == question.correct_answer:
                print("correct!")
                continue

quiz = Quiz("myquiz")

q1 = Question("what is my name", "Aarwin")
q2 = Question("what is 2+2", "4")

quiz.add_questions(q1)
quiz.add_questions(q2)

quiz.display()