# This is an example list:
L=[1, -2, 3.4]

def applyToEach(L, f):
    '''
    L is a list
    f is a function
    
    This function applies a function f to every member of a list L
    '''
    for i in range(len(L)):
        L[i]=f(L[i])
        print L
        
# This function illustrates, that we can pass a function as an argument into a different function