#Convert the following into code that uses a while loop.
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!
x = 1
while x<=5:
    print(2*x)
    x += 1
print("Goodbye!")

#Convert the following into code that uses a while loop.
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2

print("Hello!")
x = 5
while x>0:
    print(2*x)
    x -= 1

#Write a while loop that sums the values 1 through end, inclusive. 
# end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:
#21
#which is 1 + 2 + 3 + 4 + 5 + 6.

end=6
x = 1
total = 0
while x<=end:
    total += x
    x += 1
print(total)
