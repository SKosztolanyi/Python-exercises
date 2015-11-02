# This functions returns the middle number without using conditionals
# This function has to find the middle number using only min and max functions
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    # At first, I find the bigger number compared lo and x
    # Then I find the smaller number from pair either lo+hi(hi is always bigger)
    # or x+hi(x can be bigger or smaller)
    return min(max(lo,x),hi)