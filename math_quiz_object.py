from random import randint

### Constants ###
BAD_ANSWER_LIMIT = 3 # Number of non-digit attempts allowed to a user.
WRONG_ANSWER_LIMIT = 5 # Number of incorrect answers allowed to a user.
#################

class MathQuiz:
    def __init__(self, add=True, sub=False, mult=False, div=False, difficulty=1, number=1):
        self.difficulty = difficulty
        self.operators = []
        if add:
            self.operators.append('+')
        if sub:
            self.operators.append('-')
        if mult:
            self.operators.append('*')
        if div:
            self.operators.append('/')
            
        self.length = 0
        
        self.operand_1 = []
        self.operand_2 = []
        self.operator = []
        self.answers = []
        
        while self.length < number:
            self.add_problem()
            
    def __str__(self):
        return f"{self.operand_1.pop()} {self.operator.pop()} {self.operand_2.pop()} = "
        
    def __repr__(self):
        return f"Quiz object with {self.number} problems."
        
    def next_question(self):
        mistakes = 0
        attempts = 0
        q = str(self)
        answer = self.answers.pop()
        
        while True:
            try: # Attempt to cast user's input to int.
                response = int(input(q))
            except ValueError: # User entered a non-digit.
                print("That is not a number.\n") # \n is "new line" character.
                mistakes += 1
                if mistakes >= BAD_ANSWER_LIMIT: # Bad response limit reached.
                    print("Too many bad responses. Quitting.")
                    break
            except Exception as e: # Unknown error has occurred.
                print("Something unexpected went wrong.")
                print("Error: " + str(e))
                break
            else: # User's input was formatted correctly.
                if response == answer: # User's answer was correct.
                    #end = time()
                    print("Correct!")
                    #print("It took you " + str(round(end-start,1)) + " seconds to solve the problem.")
                    break
                else: # User's answer was incorrect.
                    print("Incorrect.")
                    attempts += 1
                    if attempts < WRONG_ANSWER_LIMIT:
                        print("Please try again.\n")
                    else: # User has already retried the problem enough times.
                        print("The correct answer was: " + str(answer))
                        break
        
        
    def add_problem(self):
        self.operand_1.append(randint(0,10**self.difficulty-1))
        self.operand_2.append(randint(0,10**self.difficulty-1))
        
        self.operator.append(self.operators[randint(0,len(self.operators)-1)])
        
        if self.operator[-1] == "+":
            self.answers.append(self.operand_1[-1] + self.operand_2[-1])
        elif self.operator[-1] == "-":
            self.answers.append(self.operand_1[-1] - self.operand_2[-1])
        elif self.operator[-1] == "*":
            self.answers.append(self.operand_1[-1] * self.operand_2[-1])
        elif self.operator[-1] == "/":
            self.answers.append(self.operand_1[-1] / self.operand_2[-1])
            
        self.length += 1