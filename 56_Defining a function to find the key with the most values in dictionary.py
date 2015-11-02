# a procedure, called biggest, which returns the key corresponding 
# to the entry with the largest number of values associated with it. 

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    x=[]
    x=max(aDict.values())
    for e in aDict:
        if x == aDict[e]:
            aDict[e]
            return e

max(aDict.iterkeys(), key=(lambda key: aDict[key]))

# None of these solutions are complete, will have to return to it later

# the problem here is, that I find the key with the longest value and not the biggest count of values 