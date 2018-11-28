# Fuck vowels
# Demonstrates creating a new string with a for loop

message = input("Enter a message: ")
newMessage = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        newMessage += letter
        #print("New string created: ", newMessage)
print("\nYour message without vowels is: ", newMessage)

input("\n\nPress enter to quit")
