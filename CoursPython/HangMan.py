# HangMan Game !!!!!!!!!!!!!!!!!!!

# The classic game of HangMan. The computer picks a random word
# and the player tries to guess it one letter at a time. If the player
# can't guess the word in time, the little Trump gets hanged.

# imports
import random as fuck

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("STAMINA", "OVERUSED", "MEXICAN", "PYTHON", "BRIAN", "TRILLIONS", "LOAN")

# initialise variables
word = fuck.choice(WORDS)
progression = "_" * len(word)
wrong = 0
used = []

print("Welcome to HangTrump. Good luck China!")

while wrong < MAX_WRONG and progression != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters: \n", used)
    print("So far, your word is:\n" + progression)
    
    guess = input("Choose your next letter: ")
    guess = guess.upper()

    while guess in used:
        print("Letter ", guess, "already used")
        
        guess = input("Choose your next letter: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes! ", guess, "is in the word!")
        new = ""
        
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += progression[i]

        progression = new
    else:
        print("\nSorry, ", guess, "isn't part of the word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Trump has been hanged but is still alive")
else:
    ("You guessed right! Trump still lives :(")

print("The word was:", word)

input("\n\nPress the enter key to exit")

        
            
    


