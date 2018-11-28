# Demonstrates lists, sets and dictionnaries


# List can me modified anyhow
List = [0, 1, 2, 3, 3, 3]

# Set cannot be modified and CANNOT have 2 of the same
Set = {0, 1, 2, 3, 3, 3}

# May have a key and a value
Dictionnary = {"un" : 0,"deux" : 1,"trois" : 2,"quatre" : 3}

value = Dictionnary["trois"]
print(value)

value = Dictionnary["trois"] = False
print(value)


print(Set)
print(List)
print(Dictionnary)
