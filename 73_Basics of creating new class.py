# Creating new objects similarly to defining functions.

class Clock(object):
    '''
    This object
    '''
    def __init__(self, time): # Always use self to apply the attribute to itself.
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30') # With this, I assign the value to class Clock.
clock.print_time() # With this, I only print the value of Clock class.
print time
