# Private Creature
# Demonstrates private variables and methods

class Creature(object):
    def __init__(self, name, mood):
        print("A new creature is born")
        self.name = name    # PUBLIC
        self.__mood = mood    # PRIVATE
        
    def talk(self):
        print("\nI'm,", self.name)
        print("Right now I feel", self.__mood, "\n")

    def  __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()

# main
crit = Creature(name = "Poohi", mood = "Happy")
crit.talk()
crit.public_method()

print(crit.mood)
crit.__private_method()

input("\n\n Press the enter key to exit")
