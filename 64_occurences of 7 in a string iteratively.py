def c7iter(s):
    '''
    s is an integer
    this function transforms integer into a string and counts the number 
    of occurences of number 7 in the string,
    returning number of times 7 is in the original number.
    '''
    s=str(s)
    times = 0
    for i in s:
        if i == "7":
            times +=1
    return times