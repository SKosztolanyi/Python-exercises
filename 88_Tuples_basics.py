# Tuples are non-changable lists, we can iterate through them
# Tuples are immutable, but lists are mutable.
# String is also immutable - once created, it's content cannot be changed
# We cannot sort, append or reverse a tuple
# We can only count or index a tuple

# The main advantage of a tuple is, they are more efficient
# We can use tuples when we make temporary variables

# The items() method in a dictionary returns a list of (key, value) tuples
# We can sort dictionaries by sorting tuples in dictionary
# Method dict.sort() sorts by keys - the values don't even get looked at.
d = { "b":2, "a":10, "c":18}
t = d.items()
print t
t.sort()
print t
t2 = sorted(d.items()) # this is more direct method
print t2

# It is possible to sort a dictionary by values when I iterate through a list of values
c = { "b":2, "a":10, "c":18, "d":-16, "e": 21}
print c
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) ) # reversing keys and values
print tmp

tmp.sort(reverse = True)
print tmp

#short verion:
d = { "b":2, "a":10, "c":18, "d":-16, "e": 21}
print sorted( [ (v, k) for k, v in d.items() ] )
# sorted by value in one line