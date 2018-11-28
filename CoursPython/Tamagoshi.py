# Creature  Caretaker
# Virtual pet to take care of

class Creature(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __passTime(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            m = "happy"
        elif unhapiness <= 10:
            m = "okay"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now. \n")
        self.__passTime()

    def eat(self, food = 4):
        print("Buuuuurp. Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__passTime()

    def play(self, fun = 4):
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__passTime()

def main():
    crit_name = input("How do you want to name your pet? : ")
    crit = Creature(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Creature CareTaker

        0 = Quit
        1 = Listen to your creature
        2 = Feed your creature
        3 = Play with your creature
        """)

        choice = input("Choice: \n")
        
        if choice == "0":
            print("Byyeeeeeeee")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Ouch, why meee??? Choose something right instead of: ", choice)

main()

input("\n\n Press enter key to exit")
