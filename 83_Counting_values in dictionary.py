# Counting the most common word in a text
counts = dict()
line = "lama lama duck face palm the the the the monkey donkey monkey lama lama duck lama lama duck face palm the the the the monkey donkey monkey lama lama duck"
words = line.split() 
# I split (change the string into a list) the words and count them one by one
print "Words:", words

print "Counting..."
for element in words:
    counts[element] = counts.get(element, 0) +1
    
print "Counts", counts

# This way I count the number of times a word is in a written sentence.
# I then print the result in a form of a dictionary:
# The key is the word and value is the number of occurences of the word in a text.

# So far, I have to find the biggest number of occurences manually.
for key in counts:
    print key, counts[key] # With this, I print key followed by value
    
# From dictionary, I can only print the values if I want to:
print counts.values()
# or keys
print counts.keys()
# or tuples
print counts.items()