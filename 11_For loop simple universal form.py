greeting = 'Hello!'
count = 0

# This is universal python for loop function form
# The "letter" is <identifier> and "greeting" is <sequence>
# the "in" is crucial. "letter" can be changed for any word and the function still works

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter

print 'done'