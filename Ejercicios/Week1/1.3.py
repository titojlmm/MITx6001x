"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
#s="azcbobobegghakl"
#s="abcbcd"
s="kfsfzamategyrwgayevgrs"
s="lcbsldbwecrqyyrnxhscpf"
s="abcdefghijklmnopqrstuvwxyz"

cont=0
compstring = ""
longeststring = ""
previous = "a"
for car in s:
    if car >= previous:
        compstring += car
    elif (len(compstring) > len(longeststring)):
        longeststring = compstring
        compstring = car
    else:
        compstring = car
    previous = car

if (len(compstring) > len(longeststring)):
    longeststring = compstring

print("Longest substring in alphabetical order is: " + longeststring)
