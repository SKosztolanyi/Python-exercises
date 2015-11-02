def findRoot3(x, power, epsilon):
    '''
This is advanced function for finding roots of both negative and fractional numbers
It is advanced because it uses built in function in it's body to make it simpler
    x=number(float or int)
    power= int, power to x
    epsilon=float to which I compare needed precision
    '''
    if x < 0 and power%2 == 0:
        return None
    # It's impossible to find even powered root of negative number
    low = min(-1, x)
    high = max(1, x)
    # I need to use min and max because of negative numbers 
    # and -1 and 1 instead of 0 because of fractional numbers
    ans = (low+high)/2
    while abs(ans**power-x)>epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans = (high+low)/2.0
    return ans
        