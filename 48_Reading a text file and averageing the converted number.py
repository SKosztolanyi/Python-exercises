# Use the file name mbox-short.txt as the file name
# In this assignment I work with another .txt file and I want to extract a number as a float from every line that starts with:
# Then I calculate the average of all the numbers I gained.
# I only print the final value

fname = raw_input("Enter file name: ")
fh = open(fname)
num=0
total=0
avg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    elif line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(":")
        num+=1
        total += float(line[pos+1: ])
avg=total/num
print "Average spam confidence: " + str(avg)