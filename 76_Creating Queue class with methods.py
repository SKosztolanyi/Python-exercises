class Queue(object):
    
    def __init__(self):
        '''
        initialize your Queue
        '''
        self.qlist = []
    
    def insert(self, e):
        '''Assumes e is an integer and inserts e into self'''    
        self.qlist.append(e)
        
    def __str__(self):
        """Returns a string representation of self"""
        self.qlist()
        return '[' + ','.join([str(e) for e in self.qlist]) + ']'
        
    def remove(self):
        if self.qlist != []:
           return self.qlist.pop(0)
        else:
            raise ValueError('List is empty')
        