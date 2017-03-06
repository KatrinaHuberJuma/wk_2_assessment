"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.


        abstraction, encapsulation, and polymorphism

        Abstraction is generalizing your chunks of code so that they can be reused
        in different situations. In object orientation, defining a class allows you 
        to instantiate different but similar objects without retyping 
        anything more than the name of the class

        Encapsulation is the art of setting attributes and methods in the most 
        efficient class or parent class depending on how specific they need to be.
        For example, an attribute that is shared by all instances of all child classes
        can 

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   As I learned in the course of this assessment, if you make a class attribute
   and write a method that updates it, the update is reflected in all future instances 
   of that class and the children of that class. Updating a class attribute for 
   an Animal class updates the very concept of what an animal is. A list that is
   set as a class attribute is shared between all instances and if you append to
   one you append to all. Instance attributes keep things their "self" instance
   and don't bleed into others.


"""

# *****************
#       PART 2
# *****************

'''
{'first_name': 'Jasmine',
 'last_name': 'Debugger',
 'address': '0101 Computer Street'}

{'first_name': 'Jaqui',
 'last_name': 'Console',
 'address': '888 Binary Ave'}
 '''

class Student(object):
    ''' Creates student objects with first and last names, and addresses (all strings)'''

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return "%s is a Student object" % self.first_name

class Question(object):
    ''' Creates question objects with question strings and correct answer strings'''

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return "'%s' is a Question object" % self.question

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question)
        return user_answer.lower() == self.correct_answer.lower()

class Exam(object):
    ''' Creates exam objects that each have a questions attribute (list of questions) and a name '''

    

    def __init__(self, name):
        self.name = name
        self.questions = []

    def __repr__(self):
        return "'%s' is an Exam object" % self.name

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        print "in exam"
        correct = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1
        score = correct / len(self.questions) * 100
        print "your score is {0:.2f}%".format(score)
        return score


class Quiz(Exam):

    def administer(self):
        old = super(Quiz, self).administer()
        return old > 50
# *****************
#       PART 3
# *****************




# *****************
#       PART 4
# *****************

def take_test(exam, student):
    student.score = exam.administer()

def add_qs(obj):
    obj.add_question("Eat this?", "Yes")
    obj.add_question("Eat that?", "Yes")
    obj.add_question("Eat the other?", "Yes")



def example():
    poppy = Student("Poppy", "Friedman", "Here")
    sniff_test = Exam("Sniff test")
    add_qs(sniff_test)
    results = sniff_test.administer()
    poppy_score = "{0:.2f}%".format(results)
    print "{:} {:}, your score is {}%".format(poppy.first_name, poppy.last_name, poppy_score)
        
def quiz_example():
    hobbit = Student("Hobbit", "Huber", "Home")
    hobbit_sniff_test = Quiz("Sniff test")
    add_qs(hobbit_sniff_test)
    if hobbit_sniff_test.administer():
        pass_or_fail = "PASS!"
    else:
        pass_or_fail = "fail."

    print "Hobit you {}".format(pass_or_fail)




print "testing quiz object"

quiz_example()

print "testing exam object"

example()