# -*- coding: utf-8 -*-

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def timesFive(a):
    return a * 5

testList = [1, -4, 8, -9]

applyToEach(testList, timesFive)
        
print(testList)

def absValue(a):
    return abs(a)

testList = [1, -4, 8, -9]

applyToEach(testList, absValue)

print(testList)

def plusOneValue(a):
    return a+1

testList = [1, -4, 8, -9]

applyToEach(testList, plusOneValue)

print(testList)

def squaredValue(a):
    return a**2

testList = [1, -4, 8, -9]

applyToEach(testList, squaredValue)

print(testList)
