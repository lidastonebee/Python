######   Part 1: Build Something: Password Validator with Functions   ######


# Function that checks whether the password has at leat 8 characters
def characters_lenght_check(password):
    flag = False
    # Counter in order to find out the size of the string
    lenght = 0
    for i in password:
        lenght = lenght + 1
    if lenght >= 8:
        flag = True
        print("The password has at least 8 characters") 
    else:
        print("the password has not at least 8 characters")     
    return flag    

# Function that checks whether the password has at leat one digit
def digit_check(password):
    flag = False
    # Traverse each character of the string
    for i in password:
        # Checking if the current charaster is a digit with the helful function
        # 'isdigit()' that returns 'True' if the character is digit and 'False'
        # if it is not
        if i.isdigit():
            flag = True
    if flag == True:
        print("The password contains at least one digit") 
    else:
        print("The password does not contain at least one digit") 
    return flag              

# Function that checks whether the password has at leat one uppercase letter
def uppercase_check(password):
    flag = False
    # Traverse each character of the string
    for i in password:
        # Checking if the current charaster is an uppercase letter with the helful function
        # 'isupper()' that returns 'True' if the character is uppercase letter and 'False'
        # if it is not
        if i.isupper():
            flag = True
    if flag == True:
        print("The password contains at least one uppercase letter") 
    else:
        print("The password does not contain at least one uppercase letter")
    return flag   
   
# Function that checks whether the password has at leat one lowercase letter    
def lowercase_check(password):
    flag = False
    # Traverse each character of the string
    for i in password:
        # Checking if the current charaster is a lowercase letter with the helful function
        # 'islower()' that returns 'True' if the character is lowercase letter and 'False'
        # if it is not
        if i.islower():
            flag = True
    if flag == True:
        print("The password contains at least one lowercase letter") 
    else:
        print("The password does not contain at least one lowercase letter")
    return flag      

# The user enters a password
print("Please enter a password:")
password = input()
# Calling all the helper functions and store the results in
# related variables
check1 = characters_lenght_check(password)
check2 = digit_check(password)
check3 = uppercase_check(password)
check4 = lowercase_check(password)
# Checking if the password is valid in the end of the day
if (check1 == True) and (check2 == True) and (check3 == True) and (check4 == True):
    print("The password is valid")
else:
    print("The password is invalid")
# Finding which rule was broken    
if check1 == False:
    print("The first rule with the password lenght failed")  
if check2 == False:
    print("The second rule with the existence of at least one digit failed")             
if check3 == False:
    print("The third rule with the existence of at least one uppercase letter failed")     
if check4 == False:
    print("The forth rule with the existence of at least one lowercase letter failed")      

######   Part 2: Explain It: Function Design Explanation   ######

# - What functions did you create?
# I created four functions, one for each rule neened.
# In each one we have a flag that signal whether the check of the 
# specific function is satisfied (the flag is set 'True'). Specifically
# we traverse all characters of the string password that is given from the user,
# one by one, checking the number of characters and their type as well.
# - What parameter does each function receive?
# As a parameter we only use the given password that we want to check.
# - What does each function return?
# Every function return the boolean flag in order to know whether the 
# condition is fulfilled or not.
# - Why is it useful to split the task into helper functions?
# In order to make our code understandable, easy to maintain and change if
# needed in the future. 
# - Where is each function called?
# All functions are called inside the actual main program.
# - How does your program combine the function results?
# After having the results of the functions, with another if condition
# we check which rules are broken and which are fulfilled.

######   Part 3: Debug Something: Broken Function Code   ######

# - Why does True inside the function not work as intended?
# Because we should return the logic value 'True' when the condition
# is fulfilled. Otherwise the function will always return 'False' as
# it exist in the end of the function.
# - Where should return True be placed?
# In the place where the simple 'True' is writen.
# - Why is if has_number: wrong?
# The primary faulse is that the function is called incorrectly 
# without the parameter, so the actual function is never called
# and the condition of this 'if' is always 'True'.
# - How should the function be called with the password argument?
# It should be called as it is writen in the definition line, like this
# 'has_number(password)'.
# - How would you test this function separately?
# If we change the mistakes we mentioned before then the function will 
# work perfectly.

######     Part 4: Reflect on ChatGPT Use     ######

# I didn't use ChatGPT this week at all!