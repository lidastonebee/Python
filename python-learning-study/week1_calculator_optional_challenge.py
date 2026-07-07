######   Part 5: Optional Challenge for Stronger Learners   ######

# We define the list as global in order to have access in every result
history_list = []

# Functions for each operation
# Inside them we add the new elements into the history_list
def add(num1, num2):
    result = num1 + num2
    history_list.append(result)
    return result

def subtract(num1, num2):
    result = num1 - num2
    history_list.append(result)
    return result

def multiply(num1, num2):
    result = num1 * num2
    history_list.append(result)
    return result

def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        history_list.append(result)
        return print("The final result is:",result)
    else:
        return print("The division with zero cannot happen")

# Starting by printing a message for the basic use of the calculator
print("Do you want to use a simple calculator?")
print("Write anything to continue or quit in order to leave")
answer = input()

# The try is very usefull in order to detect invalid input numbers
# for instance random characters
try:

    while (answer != "quit"):
        print("Enter the first number:")
        number1 = input()
        print("Enter the second number:")
        number2 = input()
        # Making the convertion into floats
        number1 = float(number1)
        number2 = float(number2)
        # Choosing the operation
        print("Which operation do you like to use?")
        print("Choose between +, -, *, or / by simply writing the symbol.")
        operation = input()
        # Checking which operation is chosen and print the final result
        # Or handling other cases with unknown operations
        if operation == '+':
            result = add(number1, number2)
            print("The final result is:",result)
        elif operation == '-':
            result = subtract(number1, number2)
            print("The final result is:",result)
        elif operation == '*':
            result = multiply(number1, number2) 
            print("The final result is:",result)
        elif operation == '/':
            divide(number1, number2)    
        else:
            print("This is not an actual operation of our calculator!") 
        print("Do you want to use a simple calculator?")
        print("Write anything to continue or quit in order to leave")
        answer = input() 
# We print a message when the program crashes due to invalid input number        
except:
    print("Only numbers should be entered!")

# We always print the elements of history_list before finishing the program
finally:
    print("Here is the calculation history:")
    for i in history_list:
        print(i) 
