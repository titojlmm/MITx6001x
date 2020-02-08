def square(x):
  return x**2


def fourthPower(x):
  '''
  x: int or float.
  '''
  return square(square(x))


def odd(x):
  return x % 2 == 1


def iterPower(base, exp):
  result = 1
  for cont in range(0, exp):
    result = result * base
  return result


def recurPower(base, exp):
  if exp == 0:
    return 1
  else:
    return base * recurPower(base, exp - 1)


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    tmp = min(a, b)
    for result in range(tmp, 0, -1):
      if (a % result == 0 and b % result == 0):
        tmp = result
        break
    return tmp


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
      return a
    else:
      return gcdRecur(b, a % b)


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if (len(aStr) == 0):
      return False
    elif (len(aStr) == 1):
      return aStr == char
    else:
      return isIn(char, aStr[0:len(aStr)//2]) or isIn(char, aStr[0:len(aStr)//2])


print(fourthPower(3))
print(odd(25))
print(odd(38))
print(iterPower(5, 0))
print(iterPower(2.1, 3))
print(iterPower(3, 4))
print(iterPower(10, 6))
print(recurPower(5, 0))
print(recurPower(2.1, 3))
print(recurPower(3, 4))
print(recurPower(10, 6))
print(gcdIter(7, 5))
print(gcdIter(15, 25))
print(gcdIter(18, 6))
print(gcdIter(65, 13))
print(gcdIter(7, 5))
print(gcdIter(15, 25))
print(gcdIter(18, 6))
print(gcdIter(65, 13))
print(gcdIter(1071, 462))
print(gcdIter(462, 1071))
