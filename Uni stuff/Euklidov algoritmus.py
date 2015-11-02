# -*- coding: utf-8 -*-
# Euklidov algoritmus má elegantným spôsobom nájsť najväčšieho spoločného deliteľa akýchkoľvek dvoch celých čísel.
def EuklidSubstraction(x, y):
    ''' Assumes x and y are positive integers.
        Finds the biggest common divisor of two numbers.'''
    if x == 0:
        return y
    while y!=0: ## I repeat the substraction until one number is 0.
        if x >y:
            x = x-y 
    ## The idea behind the substaction is to always substract the smaller number from the bigger.
    ## If the bigger and smaller number meet at some point, I get to the common divisor.
    ## Otherwise, the result will be 1, which means, one of the numbers is a prime number.
        else:
            y = y-x
    return x
            
def EuklidRecursive(x, y):
    ## This function recursively works with the modulo operator, until the result i 0.
    ## When result of modulo is 0, the number that we divided is returned as the biggest common divisor.
    if y == 0:
        return x
    else:
        return EuklidRecursive(y, x%y)