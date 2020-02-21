from random import randint
from time import time

### Constants ###
BAD_ANSWER_LIMIT = 3 # Number of non-digit attempts allowed to a user.
WRONG_ANSWER_LIMIT = 5 # Number of incorrect answers allowed to a user.
#################

x = randint(0,9)
y = randint(0,9)

answer = x + y

'''
Stuff goes here.
Stuff also goes here.
This is a multi-line comment.
'''

mistakes = 0
attempts = 0
start = time() # Persistent measurement of start time when the user was
               # first shown the problem.
while True:
    print(" " + str(x))
    print("+" + str(y))
    print('---')
    
    try: # Attempt to cast user's input to int.
        response = int(input(" "))
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
            end = time()
            print("Correct!")
            print("It took you " + str(round(end-start,1)) + " seconds to solve the problem.")
            break
        else: # User's answer was incorrect.
            print("Incorrect.")
            attempts += 1
            if attempts < WRONG_ANSWER_LIMIT:
                print("Please try again.\n")
            else: # User has already retried the problem enough times.
                print("The correct answer was: " + str(answer))
                break
        
        
def print_even(a):
    for item in a:
        if not item % 2: # Only even elements.   
            print(item)
            
def print_odd(a):
    if isinstance(a, list):
        try:
            for item in a:
                if item % 2: # Only odd elements.   
                    print(item)
        except TypeError:
            print("List elements must be numbers.")
        except:
            print("Something else went wrong.")
    else:
        print("That is not a list.")
    
def get_odd(a):
    if isinstance(a, list):
        odd_elements = []
        try:
            for item in a:
                if item % 2: # Only odd elements.   
                    odd_elements.append(item)
            return odd_elements
        except TypeError:
            print("List elements must be numbers.")
        except:
            print("Something else went wrong.")
    else:
        print("That is not a list.")