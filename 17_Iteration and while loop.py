# L3 Problem 6A

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
        # This counts every letter in the string "hello, world"
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    # And only after it had counter every word it continues to print
    iteration += 1
    # Then it adds iteration +1 and starts again from while
    
    