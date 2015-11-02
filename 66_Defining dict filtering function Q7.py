# -*- coding: utf-8 -*-
#Write a Python function that returns a list of keys in aDict that map to 
#integer values that are unique (i.e. values appear exactly once in aDict).
#The list of keys you return should be sorted in increasing order. 
#(If aDict does not contain any unique values, you should return an empty list.)

#This function takes in a dictionary and returns a list.
from collections import defaultdict
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
#    L= []
#    for i in aDict:
#        L.append(i)
#        lol=sum(L, [])
#    Postup:
#    1 zo slovníka vytvorím dlhý zoznam hodnôt po ich prečítaní
#    2 zoznam vymením na nový, kde nebudú duplicitné hodnoty a bude usporiadaný od najmenšieho po najväčšie
#    return sorted(list(set(L)))
    
    invert = defaultdict( list )
    for key, value in aDict.items():
        invert[value].append( key )
    
    result = []
    for key in invert.keys():
        if(len(invert[key]) == 1):
            result.append(invert[key][0])
    
    
    return sorted(result)
    
    #vytvoriť slovník kde sú len kľúče s unikátnymi hodnotami
    #vrátiť iba kľúče cez aDict.keys()
    
uniqueValues({0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0})
# Correct output: [3, 7, 9]