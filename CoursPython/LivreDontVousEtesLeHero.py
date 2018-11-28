# Livre dont vous êtes le héro

import random as fuck

canWin = None
isDead = None
book = None

def makeChoice():
    choice = None
    while choice != "1" or choice !="2":
        choice = input("Faites votre choix: \n")
        if choice == "1":
            return choice
        elif choice == "2":
            return choice
        else:
            print("Votre choix n'est pas valide....")


def readlines(a, b):
    story = open("Story.txt", "r")
    lines = story.readlines()
    for line in lines[a:b]:
        print(line)

    myFile = open("myBook.txt", "a+")
    for line in lines[a:b]:
        myFile.write(line)
    myFile.close()
    
    story.close()
    

def beginStory():
    readlines(0,16)
    firstAction(makeChoice())    


def firstAction(choice):    
    if choice == "1":
        readlines(17,25)
        Fight1()
        
    elif choice == "2":
        readlines(26,36)
        Archers()

def meleeCombat(isDead):
    print(" Vous entrez en combat, vos choix sont simples:")
    enemiHP = 5
    playerHP = 10
    
    while enemiHP > 0 and playerHP > 0:
        
        print("1 = Attaque rapide")
        print("2 = Attaque en puissance")
        print("3 = Bloque\n")
        
        choice = input(print("Choisissez:\n"))
        enemiMove = fuck.randint(1,3)        

        if choice == "1":
            if enemiMove == 1:
                print("L'enemi est aussi rapide que vous.")
                print("Rien ne se passe")
            elif enemiMove == 2:
                print("Votre attaque est rapide")
                print("Vous blessez l'ennemi!")
                enemiHP -= 1
            elif enemiMove == 3:
                print("Votre attaque est rapide")
                print("Mais l'ennemi bloque et vous blesse!")
                playerHP -=1
                
        elif choice == "2":
            if enemiMove == 1:
                print("L'ennemi est trop rapide...")
                print("L'ennemi vous blesse!")
                playerHP -= 1
            elif enemiMove == 2:
                print("L'ennemi est aussi puissant que vous")
                print("Rien ne se passe")                
            elif enemiMove == 3:
                print("Vous brisez le bloque adverse")
                print("Vous blessez l'ennemi!")
                enemiHP -=1

        elif choice == "3":
            if enemiMove == 1:
                print("Vous bloquez l'attaque ennemi")
                print("Votre riposte le blesse!")
                enemiHP -= 1
            elif enemiMove == 2:
                print("Votre bloque est brisé par une attaque en puissance")
                print("L'ennemi vous blesse!")
            elif enemiMove == 3:
                print("Vous et votre adversaire êtes sur vos gardes")
                print("Rien ne se passe")
        else:
            print("Mauvais choix d'action!")
            print("Vous perdez de la vie...")
            playerHP -= 1

        print("Il vous reste: ", playerHP,"points de vie")
        print("L'ennemi a: ", enemiHP,"points de vie restant\n")

        if playerHP == 0:
            isDead = True
            return isDead
    

def Fight1():
    meleeCombat(isDead)
    if isDead == True:
        readlines(38,42)
    else:
        CliffStairs()

def Archers():
    print("Vous entrez en phase de fuite.")
    print("Roulez un dé è 6 faces en appuyant sur enter.")
    print("Seul un résultat de 1 mène à l'échec")
    input(print("Lancez le dé! :"))
    roll = fuck.randint(1,6)
    print("Votre résultat est: ", roll)
    if roll == 1:
        readlines(44,49)
    else:
        CliffStairs()
    

def CliffStairs():
    readlines(51,64)
    choice = makeChoice()
    if choice == "1":
        Cliff()
    elif choice == "2":
        Stairs()
    
def Cliff():
    readlines(66,73)
    
    print("Vous entrez en phase de grimpe.")
    print("Roulez un dé à 6 faces en appuyant sur enter.")
    print("Seul un résultat de 1 mène à l'échec")
    input(print("Lancez le dé! :"))
    roll = fuck.randint(1,6)
    print("Votre résultat est: ", roll)
    if roll == 1:
        readlines(75,79)
    else:
        Traitor()

def Stairs():
    readlines(81,86)

    print("Vous entrez en phase de descente.")
    print("Roulez un dé à 10 faces en appuyant sur enter.")
    print("Seul un résultat de 1 mène à l'échec")
    input(print("Lancez le dé! :"))
    roll = fuck.randint(1,10)
    print("Votre résultat est: ", roll)
    if roll == 1:
        readlines(88,92)
    else:
        Traitor()

def Traitor():
    readlines(94,109)
    choice = makeChoice()
    if choice == "1":
        canWin = None
        FightFinal(canWin)
    elif choice == "2":
        FightTraitor()
        
def FightTraitor():
    readlines(111,116)
    meleeCombat(isDead)
    if isDead == True:
        readlines(118,122)
    else:
        readlines(124,127)
        canWin = True
        FightFinal(canWin)

def FightFinal(canWin):
    readlines(129,139)
    print("Roulez un dé à 10 faces en appuyant sur enter.")
    print("Seul un résultat de 1 mène à l'échec")
    input(print("Lancez le dé! :"))
    roll = fuck.randint(1,10)
    print("Votre résultat est: ", roll)

    if roll == 1:
        readlines(162,166)
    elif roll > 1 and canWin:
        Success()
    elif roll > 1:
        WinDead()

def WinDead():
    readlines(141,152)
    print("Roulez un dé à 10 faces en appuyant sur enter.")
    print("Seul un résultat de 9 ou 10 vous permet de survivre!")
    input(print("Lancez le dé! :"))
    roll = fuck.randint(1,10)
    print("Votre résultat est: ", roll)
    if roll >= 9:
        print("Vous entrer votre épée dans le dos de votre compagne avant")
        print("qu'elle puisse faire le moindre geste. Son corps s'écroule ")
        print("devant la porte et vous vous empressez de prendre la clef.")
        Success()
    else:
        readlines(118,122)

def Success():
    readlines(154,160)


beginStory()

input("\n\n Press enter to exit")

