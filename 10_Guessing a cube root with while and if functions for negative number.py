x = int(raw_input("Enter integer: "))
ans = 0
while ans**3< abs(x):
    ans+=1
if ans**3 != abs(x):
    print str(x)+" is not a perfect cube" + "; closest root is " + str(ans)
else:
    if x<0:
        ans = -ans
    print "Cube root of " + str(x)+" is " + str(ans)