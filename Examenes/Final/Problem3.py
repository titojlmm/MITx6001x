# -*- coding: utf-8 -*-
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    tmp = ""
    # We remove every non-digit character
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            tmp += s[i]
    if len(tmp)==0:
        raise ValueError("Strings with no digits are not allowed")
    else:
        total=0
        for i in range(len(tmp)):
            total += int(tmp[i])
        return total
          
print(sum_digits("a;35d4"))
print(sum_digits("95458464645"))
print(sum_digits("a;35d4."))
print(sum_digits("a;d"))
print(sum_digits(""))
