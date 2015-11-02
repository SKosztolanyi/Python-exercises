def Fib(x):
    '''
    assumes x an int>=0
    returns Fibonacci of x'''
    assert type(x) == int and x>=0
    if x == 1 or x == 0:
        return 1
    else:
        return (x-1)+(x-2) # This function has two base cases