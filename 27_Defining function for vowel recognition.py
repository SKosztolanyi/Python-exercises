def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char == "a" or char == 'e' or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        return True
    else:
        return False
        
def isVowel2(char):
    '''
    char: a single letter of any case
    
    If char is in a list, then it returns True, otherwise it returns False

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char in "aeiouAIEOU":
        return True
    else:
        return False