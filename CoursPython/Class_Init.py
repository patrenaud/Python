# Constructor of Creature
# Demonstrate constructor

class Creature(object):
    """ A virtual pet"""
    def __init__(self):
        print("A new creature has been born")

    def talk(self):
        print("\n Hi, I'm an instance")

# Main
creature = Creature()
creature2 = Creature()

creature.talk()
creature2.talk()

input("\n\n Press enter to exit")
