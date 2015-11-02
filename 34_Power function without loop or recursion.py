## This is another way how to get compute any power of a number without using recursion or loop

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp > 0 and exp % 2 == 0:
        return (base**2)**(exp/2)
    elif exp >0 and exp % 2 != 0:
        return base*(base**(exp-1))
    elif exp ==0:
        return 1
    else:
        print "Invalid input"