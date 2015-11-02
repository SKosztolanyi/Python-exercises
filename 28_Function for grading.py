## This function grades a test by A-F grade according to float given
## Correct values are only 0-1.

score=raw_input("Your score:")
score = float(score)

if score <1.0 and score >= 0.9:
    print "A"
elif score <0.9 and score >= 0.8:
    print "B"
elif score <0.8 and score >=0.7:
    print "C"
elif score <0.7 and score >= 0.6:
    print "D"
elif score <0.6 and score >0:
    print "F"
else:
    print "error"
    print "Select only value <0,1>"