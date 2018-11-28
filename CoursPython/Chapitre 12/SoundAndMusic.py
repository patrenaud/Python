# sounds and Music and stuff
# Demonstrates playing music and sounds

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

# load a sound file
missileSound = games.load_sound("missile.wav")

# load a music file
games.music.load("theme.mid")

choice = None
while choice != "0":
    print(
        """
        Sound and Music

        0 - Quit
        1 - Play missile sound
        2 - Loop missile sound
        3 - Stop missile sound
        4 - Play theme music
        5 - Loop theme music
        6 - Stop theme music
        """
        )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Good bye mon homme")
    elif choice == "1":
        missileSound.play()
        print("Playing missile sound")
    elif choice == "2":
        missileSound.play(5)
        # -1 = loop forever
        print("Looping missile sound")
    elif choice == "3":
        missileSound.stop()
        print("Stopping the sound")
    elif choice == "4":
        games.music.play()
        print("Playing the music")
    elif choice == "5":
        games.music.play(-1)
        print("Looping the music")
    elif choice == "6":
        games.music.stop()
        print("Stopping the music")
    else:
        print("\n Sorry........ wrong input ! ")

input("\n\n Press enter to quit")
        
