#Assume that two variables, varA and varB, are assigned values, either numbers or strings.
#Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:
#"string involved" if either varA or varB are strings
#"bigger" if varA is larger than varB
#"equal" if varA is equal to varB
#"smaller" if varA is smaller than varB

#varA = 25
#varB = "testB"
#varA = 25
#varB = 20
#varA = 25
#varB = 25
varA = 25
varB = 30
#varA = "testA"
#varB = 20
#varA = "testA"
#varB = "testB"

if (type(varA)==type("") or type(varB)==type("")):
    print("string involved")
elif (varA > varB):
    print("bigger")
elif (varA == varB):
    print("equal")
elif (varA < varB):
    print("smaller")
