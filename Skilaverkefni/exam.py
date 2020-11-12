class Question:
    ''' This class encapsulates a single question and the corresponding correct answer. '''
    def __init__(self, question='', answer=''):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def set_question(self, question):
        self.question = question
        return Question(self.question)

    def set_answer(self, answer):
        self.answer = answer
        return Question(self.answer)

    def check_answer(self, response):
        true_or_false = bool(response.lower() == self.answer.lower())
        return true_or_false

    def __repr__(self):
        return "Q: {} A: {}".format(self.question, self.answer)


class ChoiceQuestion(Question):
    ''' This class extends the functionality of Question by providing a multiple choice question. '''
    def __init__(self, question='', answers=[]):
        Question.__init__(self, question)
        self.answers = answers
        self._choices = ''
        self._number = 0

    def __str__(self):
        for choice in self.answers:
            self._choices += ('\n' + str(choice[2]) + '. ')      # Choice number
            self._choices += str(choice[0])                      # Answer
        return "{}{}".format(self.question, self._choices)

    def set_question(self, question):
        return Question.set_question(self, question)
    
    def add_choice(self, option, true_or_false):
        self._number += 1 # Choice number
        tuple_item = option, true_or_false, self._number
        self.answers.append(tuple(tuple_item))

    def check_answer(self, response):
        for answer in self.answers:
            if answer[1]: # If True
                return bool(str(answer[2]) == response)
    
    def __repr__(self):
        for answer in self.answers:
            if answer[1]: # If True
                return "Q: {} A: {}".format(self.question, answer[2])

class Exam(ChoiceQuestion):
    ''' This class encapsulates an exam consisting of one or more instances of Questions and/or one or more instances of ChoiceQuestion. '''
    def __init__(self):
        self.points = 0
        self.num_questions = 0
        self.POINTS = 1

    def __str__(self):
        return self.present_exam()

    def add_question(self, question, answer):
        self.num_questions += 1
        return Question.__init__(self, question, answer)

    def add_choice_question(self, question, answers):
        self.num_questions += 1
        if ChoiceQuestion.check_answer():
            self.points += self.POINTS
        return ChoiceQuestion.__init__(self, question, answers)

    def present_exam(self):
        Question.__str__(self)
        ChoiceQuestion.__str__(self)

    def get_points(self):
        if Question.check_answer(self):
            self.points += self.POINTS
        return self.points

    def get_num_questions(self):
        return self.num_questions

exam = Exam()
exam.add_question("Who is the inventor of Python?", "Guido van Rossum")
exam.add_question("What does OOP stand for?", "Object-oriented programming")

question1_str = "In what year was the Python language first released?"
choices1_list = [("1991", True), ("1995", False), ("1998", False), ("2000", False)]
exam.add_choice_question(question1_str, choices1_list)

question2_str = "Which of the following is a built-in type in Pyhon?"
choices2_list = [("array", False), ("record", False), ("dict", True), ("bug", False)]
exam.add_choice_question(question2_str, choices2_list)

exam.present_exam()
print("Your score is {} point(s) out of {} point(s)".format(exam.get_points(), exam.get_num_questions()))