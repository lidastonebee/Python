######   Part 1: Build Something: Grade Classifier and Login Validator   ######

# We define the credentials of the user, setting default values
username = "lida756"
password = "Lid@k!xexe"
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

######   Part 2: Explain It: Decision Logic Explanation   ######

# - Which variables store the score, username, and password?
# There are specific variables with the exact names
# for the store of the score, username, and password.
# All of them are strings, although score is casting to integer.
# - Why must the score input be converted to a number?
# If we do not convert the score into a number we cannot use 
# logic expression to compare numbers, because the one variable will be string.
# - What grade boundaries did you choose?
# Every decade we change range.
# - Why is the order of if, elif, and else important?
# I started from the smaller and finishing to the very last one,
# from F to A. So, we checking each range in every if condition,
# and if nothing fits then we enter the else section. 
# - How does the login condition use and?
# I had added two flags, one for the username and one for the password.
# The flags are firstly false and they turn true when there is a mismatch
# between the strings. With a simple comparison we check if the given 
# strings given from the user are maching with the initials stored 
# in the variables username and password.
# - What would happen if you used or instead of and in the login check?
# Then we will get wrong results because a predicate is true when we
# the logic OR when at least one condition is true. On the other hand
# with the logic AND all conditions should be true in order the 
# predicate to be true.
# - Which boundary case did you test, and what did the result show?
# I tasted all the boundaries and everything work as expected.

######   Part 3: Debug Something: Broken Grade Logic   ######

# - Why will this code not run correctly?
# First of all this code is not running at all due to a syntax error;
# in order to compare a number you should use the operator ==, not 
# the assignment operator =. Rather than that, there are important parts
# that are missing, creating other prolems and wrong results.
# - What is wrong with comparing score before converting it to a number?
# In this case we have a type error because we try to compare a string
# (as it is initial given from the user) with an integer.
# - What is wrong with score = 70 inside elif?
# We have already answered this question in the beginning.
# - Which grade ranges are missing?
# What is happening if the score is below 80 and not 70? What about below 50
# which is not a pass at all? Unfortunately, these cases are not covered.
# - How should invalid score values such as -5 or 120 be handled?
# Setting a default value for the grade if it is not a pass or if it is an
# invalid number.

######     Part 4: Reflect on ChatGPT Use     ######

# I didn't use ChatGPT this week at all!