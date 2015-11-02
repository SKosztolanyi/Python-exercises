# Use words.txt as the file name - words.txt is provided online in the grader
# This way I first read the file into a variable and then change it using for loop.
# For every line in the file I delete the empty line and capitalize every letter.
# Then I print the result.
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print line