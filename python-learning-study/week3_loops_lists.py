######   Part 1: Build Something: Number List Analyzer   ######

# Setting a list with 5 integer numbers
numbers = [3, -98, 54, 0, 231]
# Initialize the counters and the total sum
pos_counter = 0
neg_counter = 0
zero_counter = 0
total_sum = 0
# Starting the for loop, traversing each element of the list
for i in numbers:
    # Checking conditions for each number
    # and updating the corrent counter each time
    if i > 0:
        pos_counter = pos_counter + 1
    elif i == 0:
        zero_counter = zero_counter + 1
    else:    
        neg_counter = neg_counter + 1
    # In every interation, we undate the total sum   
    total_sum = total_sum + i
# Printing the results after leaving the for loop    
print("The final summary is:", total_sum)  
print("Number of positives:", pos_counter)   
print("Number of negatives:", neg_counter)     
print("Number of zeros:", zero_counter)      

######   Part 2: Explain It: Loop Trace Explanation   ######

# - What values are stored in your list?
# In my list I store only integers.
# - Which counters did you create and why?
# I created three counters, one for positives, one for 
# negatives and one for zeros. Three different counters for
# each different case.
# - What happens during the first loop iteration?
# Inside the first loop iteration we access the first
# number of the list with the help of the interator i,
# and then we check what is this number in order to 
# classify it.
# - How does the program decide whether a number is positive, negative, or zero?
# We have the if, elif and else conditions to check for each case.
# - How does the total sum change during the loop?
# We keep the existing sum and adding in every iteration
# the new number that we access.
# - Why is the final print statement usually outside the loop?
# Because we want to print the final results, after finishing the
# for loop, having traversed all the elements (numbers) of the list.

######   Part 3: Debug Something: Broken Loop Logic   ######

# - Why does positive_count not increase?
# Because we do not assign the new value to the variable 
# just increasing it by one for this specific moment.
# - What is missing from positive_count + 1?
# The missing part is this one: positive_count = positive_count + 1.
# - Why will print(positive) cause an error?
# Because we haven't defined any variable with the name 'positive'.
# - What counters are missing for negative numbers and zeros?
# There are two counter missing, one for negatives and one for zeros.
# - How would you add a running sum?
# Just undating the total sum before the end of each interation, 
# like that 'total_sum = total_sum + number'.

######     Part 4: Reflect on ChatGPT Use     ######

# I didn't use ChatGPT this week at all!