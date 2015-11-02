def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    num=0
    for s in aStr:
        num+=1
    return num
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == "":
        return 0
    else:
        return 1+lenRecur(aStr[1:])