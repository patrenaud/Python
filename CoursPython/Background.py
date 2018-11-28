# Background
# Demonstrate setting the background image of a graphic screen

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

BackImage = games.load_image("pokemon.jpg", transparent = False)
games.screen.background = BackImage

games.screen.mainloop()
