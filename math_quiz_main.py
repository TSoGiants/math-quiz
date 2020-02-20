
def main():
    print("Math Quiz")
    print("---------\n")
    print("What operations do you want to work on?")
    s = input("Enter addition, subtraction, multiplication, and / or division (seperated by commas): ").lower().replace(' ', '').split(',')
    add = False
    sub = False
    mult = False
    div = False
    result = ""
    for word in s:
        if word == 'addition':
            add = True
            result += 'addition,'
        elif word == 'subtraction':
            sub = True
            result += 'subtraction,'
        elif word == 'multiplication':
            mult = True
            result += 'multiplication,'
        elif word == 'division':
            div = True
            result += 'division,'
            
    items = result[0:-1].split(',')
    if len(items) == 1:
        result = items[0]
    elif len(items) == 2:
        result = items[0] + " and " + items[1]
    else:
        result = ""
        for i in range(len(items)):
            result += items[i]
            if i < len(items) - 2:
                result += ", "
            elif i == len(items) - 2:
                result += ", and "
    
    response = input(f"I understood: {result}. Is that correct? ")
    
    print([add, sub, mult, div])
    
if __name__ == "__main__":
    main()