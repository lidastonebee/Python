######   Part 1: Build Something: Number Classification Summary   ######

# Our initial fixed list with 6 numbers
numbers = [78, -24, 0, -9, 13, 61]
# Initialize the counters with zeros and the total_sum
positives = 0
negatives = 0
zeros = 0
total_sum = 0
# Traversing each number of the list
for i in numbers:
    # Checking if it is positive, zero or negative
    # and update the proper counter
    if i > 0:
        positives = positives + 1
    elif i == 0:
        zeros = zeros + 1
    else:
        negatives = negatives + 1
    # Updating the total_sum inside the loop
    total_sum = total_sum + i
# Printing the final results after the loop has finished    
print("Number of positives:", positives)
print("Number of negatives:", negatives)
print("Number of zeros:", zeros)     
print("The total summary is:", total_sum)

######   Part 2: Explain It Without AI   ######

# - What did your list contain?
# My list contains 6 integer numbers.
# - How did your loop process each number?
# Inside the loop there is an if condition
# checking the type of the number and updating 
# the proper counter on each iteration.
# - Which variables worked as counters?
# I have three counters, 'positives' 'negatives' 
# and 'zeros', each represent exactly as the name shown.
# - How did your conditions classify the numbers?
# We check if each number is bigger, smaller or equal
# to zero.
# - How did you calculate the total sum?
# Inside the loop, for each new number processed, 
# we add the value of the number into the 'total_sum'
# # variable, without loosing the previous value of 
# the 'total_sum'. We keep the existing number and just 
# addin the new one.
# - What did you understand well without ChatGPT?
# I don't have an opinion on that, because every week
# I'm not using ChatGPT.
# - What felt uncertain without ChatGPT?
# Nothing, everything is happening without the use of ChatGPT.

######   Part 3: Debug Without AI   ######

# - Why can this code count zeros incorrectly?
# Because, inside the loop we have two separate if.
# The first one check if the number is positive, while the other if the
# number is negative and in any other case  of the second if, 
# it is just supposed that the number is zero. That is wrong, because
# we count as zeros also the positive numbers.
# - What is the difference between two separate if statements and an if/elif/else chain?
# With the separate if statements, we always check the if/elif/else of each one. 
# If we have only one, then only the one if/elif/else is checked, and if one condition
# of the if/elif/else is true, then we continue runnign the commands below from
# this specific condition and nothing more. When it's done we exit the if/elif/else chain.
# - How would you rewrite the condition structure?
# Using only one if/elif/else chain with the same predicates as existing
# - How would you test whether your fix works?
# I would running again the program. I trick that I made to find out what's
# going on, was to add some print() statements below each if/else condition,
# in order to see, which number fulfils which predicate.
 
######     Part 4: Reflect on No-AI Experience     ######

# I'm not answering this question because I have never used 
# ChatGPT in this project.


