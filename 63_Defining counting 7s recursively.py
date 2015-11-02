#Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.
#This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.

# I want to create a recursive function that counts number of occurence of a digit in a number:
def count7(N, times = 0):
    '''
    N: a non-negative integer
    '''
    # Your code here
    N=str(N) # At first I change the number of type int to a string, because I can compare slice a word based on it's characters positions.
   # times = 0 # I set the starting count to 0 times.
    if N=="":
        return times
    elif len(N)==1:
        if "7" == N[-1]:
            times+=1
            print times
            print N
            return times and count7(N[:-1], times)
    else:
        if "7" == N[-1]:
            times+=1
        print N
        print times   
        return count7(N[:-1], times) # this is the recursive call to the same string without the last letter
    return times
    
    # This function works, but is not tidy.
    # The trick here was to add a variable times in the definition that updates every recursive call
    
    ## I need to visualize all the steps of this function to see where it fails.
    # I need to find the link to the visualiser and bookmark it.