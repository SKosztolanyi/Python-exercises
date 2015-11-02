school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0
# This is starting count

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1
        
# With this function I divide vowels from cons and count them accordingly

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)

# With this I print the final result