######   Part 1: Build Something: Simple Calculator   ######

# Entering the input numbers
print("Enter the first number:")
number1 = input()
print("Enter the second number:")
number2 = input()
# Making the convertion into integers
number1 = int(number1)
number2 = int(number2)
# Choosing the operation
print("Which operation do you like to use?")
print("Choose between +, -, *, or / by simply writing the symbol.")
operation = input()
# Checking which operation is chosen and print the final result
# Or handling other cases
if operation == '+':
    result = number1 + number2
    print("The final result is:",result)
elif operation == '-':
    result = number1 - number2
    print("The final result is:",result)
elif operation == '*':
    result = number1 * number2 
    print("The final result is:",result)
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print("The final result is:",result)
    else:
        print("The division with 0 cannot happen")    
else:
    print("This is not an actual operation of our calculator!") 

######   Part 2: Explain It: Code Explanation   ######

# - What variables did you use, and what does each variable store?
# I used 4 variables, two to store the numbers, one for the operation,
# and one for the result of the calculator.
# - Why do you need to convert input values using float() or int()?
# In order to have the right result each time. We have to find the result
# depending on the input the user has entered. If we enter one integer then
# the other one should also be an integer. If one is a float then both of 
# them should be floats.
# - How does your if, elif, and else structure decide which operation to run?
# Depending on the symbol that the user had entered. We check with this criteria.
# - How does your program handle division by zero?
# The calculator doesn't continue with calculating this division
# and we simply printing an informative message about the zero division
# - How does your program handle an invalid operation?
# If the user enter any other invalid symbol
# the program print an informative message that this is not an actual operation.
# - Which part of your code shows that you understand the task?
# How the calculator work, the if, elif, else conditions.

######     Part 3: Debug Something: Broken Calculator Code     ######

# - What is wrong with this code?
# We don't convert the numbers, so if the user enter one
# integer and one float the program crashes. The input entered
# is behaved like strings. We don't have the option to do other
# operations rather than addition.
# - What happens if the user enters 10 and 5?
# The program thinks that the variables num1 and num2 are strings
# so it is adding strings, the one to the end of the other.
# - Why is num1 + num2 not safe here?
# Because we haven't define the actual num1 and num2 as numbers.
# - How should the input values be converted?
# Using the casting int() or float() for each number we enter
# What operations are missing?
# The subtraction (-), multiplication (*), and division (/).
# - What other error handling should be added?
# For the division with zero and if the user trying to do another
# operation that is not existing.

######     Part 4: Reflect on ChatGPT Use     ######

# I didn't use ChatGPT this week at all!



