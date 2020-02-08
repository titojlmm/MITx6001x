"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
#s= "This is a test. I'm great."

cont = 0
vocales = ("a","e","i","o","u")
for letra in s:
    if (letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
        cont += 1

print("Number of vowels: " + str(cont))
