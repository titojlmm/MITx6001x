# -*- coding: utf-8 -*-

def getSublists(L, n):
    '''
    This function returns a list of all possible sublists in L of length n 
    without skipping elements in L. The sublists in the returned list should 
    be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

    Parameters
    ----------
    L : List of integers. It's not empty
    n : Integer. 0 < n <= len(L)

    Returns List of all sublists in L of lenght n without skipping elements in L
    -------
    None.

    '''
    sublist = []
    for iniIndex in range(len(L)-n+1):
        sublist.append(L[iniIndex:iniIndex+n])
    return sublist

print(getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4))
print(getSublists([1, 1, 1, 1, 4], 2))
print(getSublists([0], 1))

