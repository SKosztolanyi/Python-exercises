# These two functions together represent movement of blocks in Tower of Hanoi,
# Where there are three pillars, of which two are empty and one is full of discs.
# Every disc is of different size and these discs are ordered successively from to biggest at the bottom to the smallest on the top.
# Task is to move all the discs from one pillar to the next pillar one by one, without putting big disc on smaller one.
# The final order of the discs on new pillar should be the same as the beginning order of discs on the first pillar.

def printMove(fr, to):
    # This function only prints movement of discs
    print ("move from "+str(fr)+" to " + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        # This function moves discs from the first one to the next one according to the rules in specification.
        # I just don't know how exactly it works.
        # This is an example of recursion with multiple base cases.
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare) 
        Towers(n-1, spare, to, fr)