######   Part 5: Optional Challenge for Stronger Learners   ######  

# We have test calls for each function because we have printing messages
# while the function runs.

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

# Function that checks for a special character
def special_character_check(password):
    flag = False
    for i in password:
        # In order to check if it is a special character we check if it is not a letter or a digit
        if (i.isdigit() == False) and (i.isupper() == False) and (i.islower() == False):
            flag = True
            print("The password has a special character") 
    else:
        print("the password has not a special character")     
    return flag   

# The 'main' function where the actual program runs
def main():
    # The user enters a password
    # or writes 'quit' to exit the program
    print("Please enter a password:")
    print("Press 'quit' if you want to exit.")
    password = input()
    while (password != "quit"):
        # Calling all the helper functions and store the results in
        # related variables
        check1 = characters_lenght_check(password)
        check2 = digit_check(password)
        check3 = uppercase_check(password)
        check4 = lowercase_check(password)
        check5 = special_character_check(password)
        # Checking if the password is valid in the end of the day
        if (check1 == True) and (check2 == True) and (check3 == True) and (check4 == True) and (check5 == True):
            print("The password is valid")
        else:
            print("The password is invalid")
        failed_rules_list = []    
        # Finding which rule was broken
        # and adding the corresponding message to the final list  
        if check1 == False:
            failed_rules_list.append("The first rule with the password lenght failed")
        if check2 == False:
            failed_rules_list.append("The second rule with the existence of at least one digit failed")
        if check3 == False:
            failed_rules_list.append("The third rule with the existence of at least one uppercase letter failed")             
        if check4 == False:
            failed_rules_list.append("The forth rule with the existence of at least one lowercase letter failed")     
        if check5 == False:
            failed_rules_list.append("The fifth rule with the existence of a special character failed") 
        # Printing the rules that are broken
        for i in failed_rules_list:
            print(i)
        print("Do you want to try again with another password?")
        print("Please enter a password:")
        print("Press 'quit' if you want to exit.")
        password = input()    

# Calling the 'main' function
main()        

        
