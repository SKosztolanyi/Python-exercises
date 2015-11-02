# "A dictionary is like a bag with no odrder."

bag = dict()
bag["money"] = 12
bag["gums"] = 4
bag["tissues"] = 20
print bag
print bag["gums"]
bag["gums"] = bag["gums"] - 1
print bag["gums"]

# Dictionaries are like lists, 
# except they use keys instead of indices to look up for values.

# Lists mantain order, dictionaries don't.

print "gun" in bag 
# I want to know it element "gun" is in the bag
# It returns False

print "gums" in bag
# and return True if it is there

bag["money"] = bag["money"] - 6
shopping = ["gums", "lipstick", "tissues"]
for element in shopping:
    if element in bag:
        bag[element] = bag[element] +1
    else:
        bag[element] = 1
        
print bag

# This is iterative way of putting items into dictionary
# But there is a simpler way, that uses dictionary methods instead.

ATM = 10
bag["money"] = ATM*6

# I need to refresh my purse and add some money to the bag from ATM
# Here comes another shopping
shopping2_cost = bag["money"] - 34
bag["money"] = shopping2_cost
shopping2 = ["avocado", "perfume", "gums", "lipstick", "umbrella"]

for purchase in shopping2:
    bag[purchase] = bag.get(purchase, 0) +1 
# I need to add 0 after purchase, to add new elements and then +1 to it.
# The length of the code is reduced to two lines
print bag