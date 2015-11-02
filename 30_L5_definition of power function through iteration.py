def iterPower(base, exp):
    result=1 # The first value must be 1 and not 0, because that is the first power of any number
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    while exp>0:
        result*=base # I cannot write base*=base, I must write result(or something else) *=base
                    # base must stay constant during the computation and only result is changing
        exp-=1 # Exp is alway decreasing by 1
    return result # I must return result and not base