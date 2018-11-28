# Simple Creater
# Demonstrates a basic class and object

class Creature(object):
    """A virtual pet"""
    def talk(self):
        print("Hi, I'm an instance of class Creature.")

# Main
crit = Creature()
crit.talk()

input("\n\n Press enter to exit")
