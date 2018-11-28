# Challenge

print("This will change the vowels in the sentence to the one you choose\n")

message = input("Enter your message: ")
choice = input("Enter your vowel: ")

newMessage = ""
VOWELS = "aeiou"

for letter in message:
    if letter.lower() in VOWELS:
         newMessage += choice.lower()
    else:
        newMessage += letter   

print("Your new message is:",newMessage)

input("\n\nPress enter to quit")
