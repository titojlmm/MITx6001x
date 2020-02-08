#Convert the following into code that uses a for loop.
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!
for x in range(1,6):
    print(2*x)
print("Goodbye!")

#Convert the following into code that uses a for loop.
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2

print("Hello!")
for x in range(5, 0,-1):
    print(2*x)

#Write a for loop that sums the values 1 through end, inclusive. 
# end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:
#21
#which is 1 + 2 + 3 + 4 + 5 + 6.

end=7
total = 0
for x in range(1, end+1):
    total += x
print(total)
