### Constants ###
MAX_DIFFICULTY = 3 # Maximum difficulty setting.
MIN_QUIZ_LENGTH = 1 # Minimum quiz length.
MAX_QUIZ_LENGTH = 20 # Maximum quiz length.
#################

def main():
    print("Math Quiz")
    print("---------\n")
    print("What operations do you want to work on?")
    while True:
        s = input("Enter addition, subtraction, multiplication, and / or division (seperated by commas): ").lower().replace(' ', '').split(',')
        add = False
        sub = False
        mult = False
        div = False

        items = []
        for word in s:
            if word == 'addition':
                add = True
                items.append('addition')
            elif word == 'subtraction':
                sub = True
                items.append('subtraction')
            elif word == 'multiplication':
                mult = True
                items.append('multiplication')
            elif word == 'division':
                div = True
                items.append('division')
                
        if items == []:
            items.append("none")
        elif len(items) > 1:
            items[-1] = "and " + items[-1]

        result = ', '.join(items)
        result = result.replace(', and', ' and')

        response = input(f"I understood: {result}. Is that correct? (y/n) ").lower()
        
        if response == "y" or response == "yes":
            break
        else:
            print("\nLet's try again.")
            
    while True:
        try:       
            difficulty = int(input(f"\nSelect a difficulty level: (between 1 and {MAX_DIFFICULTY}) "))
        except ValueError:
            print(f"Difficulty needs to be an integer value (1-{MAX_DIFFICULTY}).")
        else:
            if difficulty > 0 and difficulty <= MAX_DIFFICULTY:
                break
            else:
                print(f"Difficulty must be between 1 and {MAX_DIFFICULTY}.")
                
    while True:
        try:       
            number = int(input(f"\nHow many problems? ({MIN_QUIZ_LENGTH} - {MAX_QUIZ_LENGTH}) "))
        except ValueError:
            print(f"Quiz length must be an integer value ({MIN_QUIZ_LENGTH}-{MAX_QUIZ_LENGTH}).")
        else:
            if number > 0 and number <= MAX_QUIZ_LENGTH:
                break
            else:
                print(f"Quiz length must be between {MIN_QUIZ_LENGTH} and {MAX_QUIZ_LENGTH}.")

    # Generate Quiz Object
    
if __name__ == "__main__":
    main()
