# -*- coding: utf-8 -*-

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    otherTup = ()
    for idx, element in enumerate(aTup):
        if idx % 2 == 0:
            otherTup = otherTup + (element,)
        
    return otherTup

print (oddTuples(('I', 'am', 'a', 'test', 'tuple')))
print (oddTuples(()))
print (type(oddTuples(())))


def oddTuplesSlicing(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    otherTup = ()
    for element in aTup[::2]:
        otherTup = otherTup + (element,)
        
    return otherTup

print (oddTuplesSlicing(('I', 'am', 'a', 'test', 'tuple')))
print (oddTuplesSlicing(()))
print (type(oddTuplesSlicing(())))
