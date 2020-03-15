# -*- coding: utf-8 -*-

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

L1 = [2, 5, 8, 9, 10]

L2 = []

L3 = [6]

L4 = [5, 9]

L5 = [3, 7, 10] 