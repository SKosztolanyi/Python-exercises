class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
 
## In defining this method I rely heavily on previous definitions of methods
## I will be creating an empty list using intSet in the __init__ definition.
## I will need to use .member method to compare if the element is in both lists
## I will be using .insert method, to add (not .append directly) a common element to a new list.

    def intersect(self, other): 
        '''
        A method that returns a new intSet containing elements that appear in both sets.     
        ''' 
        intersect_values = intSet()
        for ele in self.vals:
            if other.member(ele):
                intersect_values.insert(ele)
        return intersect_values

## I want to return lenght of a set, so i define the method as __len__
## It cannot have different name, because I need it to be XY.len() method.       
    def __len__(self):
        ''' This simple method returns lenght of the set'''
        return len(self.vals)
        
        
# Test examples from grader:
setA = {-17,-16,-15,-11,-3,8,13}
setB = {-19,-16,-9,-7,-3,-1,7,15,18}
setA.intersect(setB)

setC = {-19,-17,-16,-8,0,7,17,19}
setD = {-20,-18,-14,-3,-2,11,14}
setC.intersect(setD)
print len(setA)