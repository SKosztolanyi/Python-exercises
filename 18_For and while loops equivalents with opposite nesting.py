# This while loop counts the letter of phrase "hello, world" 5 times

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
    
# This is the result:
#Iteration 0; count is: 12
#Iteration 1; count is: 24
#Iteration 2; count is: 36
#Iteration 3; count is: 48
#Iteration 4; count is: 60

#I want the same result, but nest a while loop inside of for loop
#That means, the same result but with different way

#Here are examples of getting the same result:
#1
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
        
#2
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)

#3 This one is the same as #2 but without while and break conditions
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)
