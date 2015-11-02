def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    assert type(char) == str and type(aStr)== str
    ans=(len(aStr))/2        
    if aStr=="":
        return False
    elif len(aStr) <= 1:
        return char == aStr
    else:
        ans=(len(aStr))/2
        if aStr[ans]==char:
            return True
        elif aStr[ans] < char:
            return isIn(char, aStr[:ans])
        else:
            return isIn(char, aStr[ans+1:])