#L3 5A
for num in range(1, 11, -1):
    if num%2==0:
        print num
print "Goodbye!"
    
    # L3 5B
print "Hello!"
for i in reversed(range(2, 11, 2)):
    print i

# L3 5C
# End is defined variable
# I want the last number to be included, therefore I give end+1
# If end wasn't defined, I would just put there number that is one count bigger

fun=0
for i in range(1, end+1, 1):
    fun+=i
print fun