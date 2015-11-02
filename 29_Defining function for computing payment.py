def computepay(h, r):
    '''
    This function computes a payment for number of hours per week,
    where more hours than 40 is valued as 1.5 times the rate.
    '''
    h=float(h)
    r=float(r)
    if h <=40:
        return h*r
    else:
        return 40*r + ((h-40)*(r*1.5))

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Rate:"))

p = computepay(hrs, rate)

print "Pay",p
