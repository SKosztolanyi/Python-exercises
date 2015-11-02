def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
# Solution 1 with for loop
    newTup = ()
    for i in range(len(aTup)):
        if i%2==0:
            newTup =newTup + (aTup[i],)
    return newTup
    
# Shorter solution 2 with slicing
    return aTup[::2]