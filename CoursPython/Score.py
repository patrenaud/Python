# Big Score
# Demonstrate displaying text on a graphic screen

from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)
backImage = games.load_image("pokemon.jpg", transparent = False)
games.screen.background = backImage

score = games.Text(value = 1756521, size = 60, color = color.black, x = 550, y = 30)
games.screen.add(score)

games.screen.mainloop()
