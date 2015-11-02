## Simple recursive algorithm
def recurMul(a,b):
    '''
    Here I want to solve multiplication recursively.
    It only works for positive whole numbers
    '''
    if b == 1:
        return a
    else:
        return a+recurMul(a, b-1) # This is where recursion is happening