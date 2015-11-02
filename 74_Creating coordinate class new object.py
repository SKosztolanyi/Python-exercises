class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
## Add an __eq__ method that returns True if coordinates refer to same point in the plane 
## (i.e., have the same x and y coordinate).  
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
# Reproduce method is a special method that returns a string that looks like a valid Python expression 
# that could be used to recreate an object with the same value.     
    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y) 

# example:
c1 = Coordinate(8, 20)
c2 = Coordinate(8, 20)
c3 = Coordinate(7, 2)

print c1
print c2
print c3
print c1 == c2
print c1 == c3
print repr(c3)