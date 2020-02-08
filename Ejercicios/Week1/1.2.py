"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s="bobobobobobobobbobobobob"

cont = 0
pos = 0
tam = len(s)
while tam >= pos + 3:
    pieza = s[pos:pos+3]
    if pieza == "bob":
        cont += 1
    pos += 1

print("Number of times bob occurs is: " + str(cont))
