# -*- coding: utf-8 -*-

def uniqueValues(aDict):
    '''
    Returns a list of keys in aDict that map to integer values that are unique 
    (i.e. values appear exactly once in aDict). 
    The list of keys you return should be sorted in increasing order. 
    If aDict does not contain any unique values, you should return an empty list.
    
    aDict: a dictionary
    '''
    # Your code here
    keyList = []

    dupValuesSet = set()
    uniqueValuesSet = set()
    for value in aDict.values():
        if value in dupValuesSet:
            continue
        elif value in uniqueValuesSet:
            dupValuesSet.add(value)
            uniqueValuesSet.remove(value)
        else:
            uniqueValuesSet.add(value)
            
    for clave in aDict.keys():
        if aDict[clave] in uniqueValuesSet:
            keyList.append(clave)
            
    return sorted(keyList)
    
    
    
print(uniqueValues({}))
print(uniqueValues({1:2, 2:4, 4:3, 6:1, 3:2, 8:3, 9:0}))
print(uniqueValues({1:2, 2:4, 4:3, 6:1, 3:10, 8:3, 9:0}))
print(uniqueValues({1:2, 2:4, 4:33, 6:1, 3:10, 8:3, 9:0}))
print(uniqueValues({1:2, 2:4, 4:3, 6:2, 3:2, 8:3, 9:1}))
print(uniqueValues({1:3, 2:4, 4:3, 6:2, 3:2, 8:3, 9:4}))