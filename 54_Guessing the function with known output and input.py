testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
#What is the value of f given:
# a) >>> print testList [5, -20, 40, -45]
def fivetimes(x):
    return x*5

# b) >>> print testList [1, 4, 8, 9]
def positive(x):
    return abs(x)

# c)  >>> print testList [2, -3, 9, -8]
def plusone(x):
    return x+1

# d)  >>> print testList [1, 16, 64, 81]
def powertotwo(x):
    return x*x
    
applyToEach(testList, powertotwo)