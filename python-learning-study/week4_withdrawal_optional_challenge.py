######   Part 5: Optional Independent Challenge   ######

try:

    # Initialize an empty list
    numbers = []
    # Message for thr user
    print("Please enter a number:")
    print("In case that you don't want to add more numbers, then write 'stop'")
    current = input()
    # We continue entering numbers until the user write 'stop'
    while current != "stop":
        # Making the conversion to integer
        current = int(current) 
        # We add the new number into the numbers list
        numbers.append(current)
        print("Please enter a number:")
        print("In case that you don't want to add more numbers, then write 'stop'")
        current = input()
    # Initialize the counters and the total sum
    pos_counter = 0
    neg_counter = 0
    zero_counter = 0
    total_sum = 0
    # Initialize max and min with the first number of the list
    max = numbers[1]
    min = numbers[1]
    # Seperate lists for each type of number
    positives = []
    negatives = []
    zeros = []
    # Starting the for loop, traversing each element of the list
    for i in numbers:
        # Updating the max and min
        if i > max:
            max = i
        if i < min:
            min = i   
        # Checking conditions for each number       
        # updating the corrent counter each time
        # and adding the number to the correct list
        if i > 0:
            pos_counter = pos_counter + 1
            positives.append(i)
        elif i == 0:
            zero_counter = zero_counter + 1
            zeros.append(i)
        else:    
            neg_counter = neg_counter + 1
            negatives.append(i)
        # In every interation, we undate the total sum   
        total_sum = total_sum + i
    # Calculating the average
    if ((pos_counter + neg_counter + zero_counter) != 0):
        average = total_sum / (pos_counter + neg_counter + zero_counter)
        print("The average of all numbers is:", average)
    else:
        print("It is impossible to calculate the average!") 
    # Printing the results after leaving the for loop    
    print("The maximun number is:", max)
    print("The minimun number is:", min)           
    print("The final summary is:", total_sum)  
    print("Number of positives:", pos_counter)   
    print("Number of negatives:", neg_counter)     
    print("Number of zeros:", zero_counter)  
    # Printing the list of positives and negatives with the help of a for loop
    print("Here is the final list of our positive numbers:") 
    for i in positives:
        print(i)
    print("Here is the final list of our negative numbers:") 
    for i in negatives:
        print(i)  

except:
    print("Only numbers should be entered!")