def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    num = max(a,b)
    while a <= a and b <=b:
        a/num and b/num
        if a%num==0 and b%num==0:
            break
        num-=1
    return num