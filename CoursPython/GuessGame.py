# Guess my number
#
# The computer picks a random number between 1 and 100
# The player tries to guess and the computer lets
# the player know if guess is too high, too low
# or right on the spot !

import random

print("\tWelcome to 'Guess My Number' !")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible. \n")

# Set the initial values
theNumber = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Guessing loop
while guess != theNumber:    
    if guess < theNumber:
        print("Your number is too low")
    elif guess > theNumber:
        print("Your number is too high")
        
    guess = int(input("Try again: "))
    tries += 1

# End text
print("\n\nGood job! You found the number in", tries, "tries")

input("\n\nPress the enter key to exit")
