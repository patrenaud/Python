# Loosing the battle
# Avoids the dreaded infinite loop

print("Your lone hero is surrounded by a massive army of mexicans")
print("Their decaying yellow bodies stretch out melting the horizon")
print("Your hero unsheathes his sword for the last fight of his life\n")

health = 10
mexicans = 0
damage = 3

while health > 0:
    mexicans +=1
    health -= damage

    print("Your hero swings and defeats an evil mexican, " \
          "but takes", damage, "damage points.\n")

print("Your hero fought valiantly and defeated", mexicans, "evil mexicans")
print("But alas, your hero is no more...")
input("\n\nPress the enter key to exit")
