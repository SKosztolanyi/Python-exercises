# This function is a while loop that sums the values 1 through end,
# inclusive.
#end is a defined variable in a tester. 
#So, for example, if we define end to be 6,
#your code should print out the result:

#21
#which is 1 + 2 + 3 + 4 + 5 + 6

num=1
fun=0
while num<=end:
    fun+=num
    num+=1
print fun