# Example values
L=[abs, float, int]
x=-4

def applyFuns(L, x):
    '''
    This function applies every function f from a list to an argument x
    '''
    for f in L:
        print(f(x))
        