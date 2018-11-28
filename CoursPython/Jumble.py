# Word Jumble
#
# The computer picks random word and then "jumbles" it
# The player has to guess the original word

import random

# create sequence of words to choose from
WORDS = ("python","jumble","easy", "difficult", "jimmy","patin", "tipat", "answer")

# Pick a random word from sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is right
correct = word

# Create jumbled version
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Start game
print("Welcome to the jumble!  if you want to stop, type exit")
print("!n The jumble word is: ", jumble)

guess = input("Enter your guess: ")
while guess != correct and guess != "exit":
    print("Wong")
    guess = input("Try again: ")

if guess == correct:
    print("Right! You guess right!")
else:
    print("Thanks for playing")

input("\n\nPress enter to quit")
