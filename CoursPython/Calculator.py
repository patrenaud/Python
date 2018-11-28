# Calculator

while True:
    print("\nOptions")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")

    userInput = input(": ")
    
    if userInput == "quit":
        break
    
    elif userInput == "add":
        num1 = (input("Enter a number: "))
        
        if num1.isnumeric():
            num2 = (input("Enter another number: "))
            
            if num2.isnumeric():
                result = float(float(num1) + float(num2))
                print("Your result is: ", result)
            else:
                print("Not a valid number")                
        else:
            print("Not a valid number")

    elif userInput == "substract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = float(num1 - num2)
        print("Your result is: ", result)
        
    elif userInput == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = float(num1 * num2)
        print("Your result is: ", result)
        
    elif userInput == "divide":        
        num1 = float(input("Enter a number: "))        
        num2 = float(input("Enter another number: "))
        if num2 == 0:
            print("cannot divide by 0")
        else:
            result = float(num1 / num2)
            print("Your result is: ", result)
    else:
        print("You rebel! This is not a valid choice!")
