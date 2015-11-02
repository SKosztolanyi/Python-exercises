# This function finds all the common divisors of two numbers.
# The divisors are returned in the form of a tuple

def findDivisors(n1, n2):
    '''
    assumes n1 and n2 positive ints returns tuple 
    containing common divisors of n1 and n2'''
    divisors = () # the empty tuple that will be filled at the end of function call
    for i in range(1, min(n1, n2)+1):
        if n1%i ==0 and n2%i == 0:
            divisors = divisors +(i,)
    return divisors