# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            # There is at least one letter not guessed
            return False
    # If we reached this point, every letter of the secret word was guessed
    return True

def isWordGuessedOneLine(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return len(set(secretWord) - set(lettersGuessed)) == 0

def isWordGuessedOneLineSecondVersion(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all([False if (letter not in lettersGuessed) else True for letter in secretWord])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            # The letter is printed
            guessedWord += letter
        else:
            # An underscore is printed
            guessedWord += " _ "
    return guessedWord

def getGuessedWordOneLine(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return "".join([letter if (letter in lettersGuessed) else " _ " for letter in secretWord])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableletters = string.ascii_lowercase
    for letter in lettersGuessed:
        # We put out every guessed letter
        availableletters = availableletters.replace(letter, "")
    
    return availableletters


def getAvailableLettersOneLine(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    return string.ascii_lowercase.translate({ord(letter): None for letter in lettersGuessed})

def getAvailableLettersOneLineSecondVersion(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    return "".join(sorted("".join(set(string.ascii_lowercase) - set(lettersGuessed))))
   

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # We greet the player
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    # We initialize the variables for the game
    maxGuesses = 8
    lettersGuessed = []
    mistakesMade = 0
    
    # We loop over the guesses
    while (mistakesMade < maxGuesses) and (not isWordGuessed(secretWord, lettersGuessed)):
        availableLetters = getAvailableLetters(lettersGuessed)
        print("You have " + str(maxGuesses - mistakesMade) + " guesses left.")
        print("Available letters: " + availableLetters)
        newGuess = input("Please guess a letter: ").lower()
        
        if (newGuess in lettersGuessed):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(newGuess)
            if (newGuess in secretWord):
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        print("------------")
        
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
        
secretWord = "tact"
hangman(secretWord)


"""
secretWord = "partial"
lettersGuessed = ["t", "s", "h", "a"]
#lettersGuessed = ["t", "s", "h", "a", "p", "i", "r", "i", "l"]
print(isWordGuessed(secretWord, lettersGuessed))
print(isWordGuessedOneLine(secretWord, lettersGuessed))
print(isWordGuessedOneLineSecondVersion(secretWord, lettersGuessed))
print(getGuessedWord(secretWord, lettersGuessed))
print(getGuessedWordOneLine(secretWord, lettersGuessed))
print(getAvailableLetters(lettersGuessed))
print(getAvailableLettersOneLine(lettersGuessed))
print(getAvailableLettersOneLineSecondVersion(lettersGuessed))
"""