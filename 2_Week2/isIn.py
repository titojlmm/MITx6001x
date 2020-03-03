def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = len(aStr) // 2
    if (aStr == ""):
        return False
    elif (middle == 0):
        return (char == aStr[middle])
    elif (char == aStr[middle]):
        return True
    elif (char > aStr[middle]):
        return isIn(char, aStr[middle:])
    else:
        return isIn(char, aStr[0:middle])


print(isIn("a",""))

print(isIn("a","bcde"))

print(isIn("b","bcde"))

print(isIn("c","bcde"))

print(isIn("d","bcde"))

print(isIn("e","bcde"))

print(isIn("f","bcde"))

print(isIn("g","bcde"))

print(isIn("a","bcdef"))

print(isIn("b","bcdef"))

print(isIn("c","bcdef"))

print(isIn("d","bcdef"))

print(isIn("e","bcdef"))

print(isIn("f","bcdef"))

print(isIn("g","bcdef"))

