L = [5]
L2 = []

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
    
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

## These two functions should be different but I don't see where.

## here's the question:
#You may assume that each function is tested with a list L whose elements are sorted in increasing order;
#for simplicity, assume L is a list of positive integers.