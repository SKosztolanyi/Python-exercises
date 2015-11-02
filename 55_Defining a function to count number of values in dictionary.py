# This function counts the number of values in a dictionary.
# Universal form of a dictionary is <key, value>
# It has a form:
# animals = { 'a': ['aardvark'], 'b': ['baboon', 'bird'], 'c': ['coati']}

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    # Your Code Here
    total=0
    for value in aDict.values():
        total+=len(value)
    return total
    
    total=0
    for key in aDict.keys():
        total+=len(aDict[key])
    return total
    
    #both of these functions give the same result
    #It's just another way of counting the function call