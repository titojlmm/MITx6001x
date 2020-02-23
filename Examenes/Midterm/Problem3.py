def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N < 10:
        if N == 7:
            return 1
        else:
            return 0
    return count7(N % 10) + count7(N // 10)
    
print (count7(0))
print (count7(717))
print (count7(1237123))
print (count7(8989))
print (count7(7))
print (count7(9))
print (count7(777777))

