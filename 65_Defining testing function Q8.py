## This function should test another function.
## The other function is unknown to me and only provided by the grader.
## I know the correct output of the function but I have to fit it.

L = ['a', 'b', 'a']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    L2 = [l for l in L if f(l) == True]
    L[:] = L2     
    return len(L2)
    
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L