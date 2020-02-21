# -*- coding: utf-8 -*-

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    for key in aDict.keys():
        aDict[key] = len(aDict[key])
        
    maxsize = max(aDict.values())
    
    for key in aDict.keys():
        if aDict[key] == maxsize:
            return key


print(biggest(animals))
