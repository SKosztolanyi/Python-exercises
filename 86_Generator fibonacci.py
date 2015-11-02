# Generator is any procedure or a method with yield statement
# Generators have a .next() method
# yield suspends execution and returns a value

def genFib():
    fib1 = 1
    fib2 = 2
    while True:
        next = fib1 + fib2
        yield next
        fib1 = fib2
        fib2 = next
        
# Generators compute all the required numbers on the way as they are needed   
fib = genFib()
fib.next()

#for n in genFib():#for n in genFib():
    print n #(this gets me into infinite loop and freezes canopy)#
