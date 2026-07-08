######   Part 1: Build Something: Grade Classifier and Login Validator   ######

# We define the credentials of the user, setting default values
username = "am.papoutsa"
password = "Am@ryllis06"
# Entering the score
print("Enter a score between 0 and 100:")
score = input()
# Converting into integer
score = int(score)
# Depending on the number of score we calculate the grade
if (score >= 50 and score <= 59):
    grade = 'F'
elif (score >= 60 and score <= 69):    
    grade = 'D'
elif (score >= 70 and score <= 79):    
    grade = 'C'    
elif (score >= 80 and score <= 89):    
    grade = 'B'    
elif (score >= 90 and score <= 100):    
    grade = 'A'    
else:
    # If the score is lower than 50 then is not a pass
    grade = '-'  
# Printing the final grade message
if score >= 50:
    print("Your final grade is:", grade)
else:
    print("You do not pass!")
# Entering the username and the password of the user    
print("Enter your username:")
current_username = input()
print("Enter your password:")
current_password = input()
# Adding some flag in order to check if the username and password match the initial values
flag1 = False
flag2 = False
# We change the flag only in the case where the strings differ somewhere
if username != current_username:
    flag1 = True
if password != current_password:
    flag2 = True
# Both of the flag are untouched then everything is correct  
if (flag1 == False and flag2 == False):
    print("Congratulations! Your credentials are valid.")   
else:
    print("Incorrect username or password. Please try again.")     