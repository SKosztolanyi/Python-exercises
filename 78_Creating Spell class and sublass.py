## Creating an object and a subclass of the object + function that calls the method of parent object, that is a superclass.

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell): # subclass of Spell
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm') # Inserts incantation and name of Spell

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.' # Inserts description.

def studySpell(spell): # defines a function to print Spell information according to __str__ method.
    print spell

spell = Accio()  # prints nothing, just assigns value to a variable
spell.execute()  # prints incantation of the spell. In this case "Accio"
studySpell(spell) # prints Summoning Charm Accio /n No description

studySpell(Confundo()) # prints Confundus Charm Confundo /n Causes the victim to become confused and befuddled.
