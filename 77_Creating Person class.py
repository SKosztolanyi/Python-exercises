import datetime  # If I wanted to add birthday

class Person(object):
    def __init__(self, name):
        '''create a person called name'''
        self.name = name
        self.birthday = None # This can be assigned later
        self.lastName = name.split(" ")[-1] # I split the name into list and index the last element
        
    def getLastName(self):
        '''return self's last name'''
        return self.lastName
        
    ## Other methods
    
    def __str__(self):
        '''return self's name'''
        return self.name
        
class MITPerson(Person):  ## This is how inheritance works,
    ## This is a subclass that can be thought as Specialization of Person
    ## MITPerson inherits all the attributes of Person class
    nextIdNum = 0 ## next ID number to assign. 
    ## This is an attribute that belongs to the class, not yet to the instances of the class
    
    def __init__(self, name):
        Person.__init__(self, name) ## Initialize Person attributes
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
        
    ## sorting MIT people uses their ID number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum
        
#Example:
p1 = MITPerson("Eric")
p2 = MITPerson("Stefan")
p3 = MITPerson("Eric")
p4 = Person("Stefan")

p3.getIdNum()
p1.getIdNum()
# p4.getIdNum() would print an AttributeError: 'Person' object has no attribute 'getIdNum'

p1<p2
p3<p2

class Student(MITPerson): # I needed to clean the classes, so I added a new superclass for all the students at MIT
    pass

#Adding another level to the hierarchy - a student, that is an MIT person
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def GetClass(self):
        return self.year
    
class Grad(Student): 
    pass # with pass, it inherits all the methods from MITPerson object, but doesn't have any special methods.
    # We can still distinguis this subclass from UnderGrad (UG) object.
    
class Transfer(Student): # I added a new object that is also student, but isn't considered a student in isStudent function.
    # Therefore, I will create a new superclass, that will capture all the students and modify the isStudent function afterwards.
    pass


#def isStudent(obj):
#    return isinstance(obj, UG) or isinstance(obj, G)
 
def isStudent(obj):
    return isinstance(obj, Student)   
