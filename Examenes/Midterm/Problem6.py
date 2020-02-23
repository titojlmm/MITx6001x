# -*- coding: utf-8 -*-

def sumDigits(N):
    '''
    Calculate and return the sum of its digits (recursively)
    
    N: a non-negative integer
    '''
    # Your code here
    if N < 10:
        return N
    else:
        return sumDigits(N // 10) + sumDigits(N % 10)
    

print(sumDigits(0))
print(sumDigits(1))
print(sumDigits(8))
print(sumDigits(10))
print(sumDigits(23))
print(sumDigits(564))
print(sumDigits(1234))
print(sumDigits(1000))