## This is a good example of divide and conquer algorithm
# I break a difficult problem into more simpler problems, which can be solved easily.

def isPalindrome(s):
    '''
    I want to know if an object(word, sentence) is a palindrome.
    Palindrome is something that reads the same from beginning as from the end.
    '''
    
    def toChars(s): # With this function I want to put all the spaces away and transfer the sentence into one word
        s=s.lower() #Given s is a string, this internal method transforms all letters to lowercase
        ans="" # I create an empty string, which I will fill with the correct letters
        for c in s:
            if c in "abcdefghijklmnopqrstuwxyz":
                ans+=c
        return ans
        
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0] == s [-1] and isPal(s[1:-1]) # This line is tricky
            # I want to compare always the first with last, the second with the second latest etc.
            
    return isPal(toChars(s))