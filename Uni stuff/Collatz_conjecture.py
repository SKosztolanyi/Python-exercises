def collatz_conjecture(n):
    '''
    Take any natural number n. If n is even, divide it by 2 to get n / 2. 
    If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. 
    Repeat the process (which has been called "Half Or Triple Plus One") indefinitely.
    The conjecture is that no matter what number you start with, you will always eventually reach 1. 
    '''
    while n != 1:
        print n
        if n%2 == 0:
            n = n/2
        else:
           n = n*3+1
    print n
    
import pylab
def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
    sequence.append(n)
    return sequence
    
pylab.plot(collatz(7))
pylab.show()

def collatz_length(n):
    ## How long is the sequence from number n to number 1.
    length = 1
    while n != 1:
        if n % 2:
            n = 3*n + 1
        else:
            n = n / 2
        length += 1
    return length

def collatz_table(steps):
    ## The number and lenght of the sequence that is associated with it.
    for i in range(1, steps+1):
        print i, collatz_length(i)
