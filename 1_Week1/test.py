low = 0
high = 100
guess = (low + high) // 2
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + "?")
answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while (answer != "c"):
  if (answer == "h"):
    high = guess
    guess = (low + high) // 2
  elif (answer == "l"):
    low = guess
    guess = (low + high) // 2
  else:
    print("Sorry, I did not understand your input.")
  print("Is your secret number " + str(guess) + "?")
  answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: " + str(guess))
