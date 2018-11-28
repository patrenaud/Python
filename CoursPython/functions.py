# Birthday Wishes
# Demonstrates keyword arguments and default parameters values

# Fonctions avec parametres
def birthday1(name, age):
    print("Happy Birthday,", name, "!"," I hear you\'re now ", age, "years old.\n")

# Fonctions avec parametres par defaut
def birthday2(name = "Jackson", age = 1):
    print("Happy Birthday,", name, "!"," I hear you\'re now ", age, "years old.\n")

birthday1("Jackson", 2)
birthday1(1, "Jackson")
birthday1(name = "Bob", age = 1)

birthday2()
birthday2(age= 9)
birthday2(name = "Jose")

input("\n\nPress enter to exit!")
