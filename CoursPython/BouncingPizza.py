# Bouncing pizza
# Demonstrate dealing with screen boundaries

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    def update(self):
        """ invert velocity component if edge of screen reached """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy

def main():
    backImage = games.load_image("pokemon.jpg", transparent = False)
    games.screen.background = backImage

    pizzaImage = games.load_image("pizza.bmp")
    pizza = Pizza(image = pizzaImage, x = games.screen.width/2, y = games.screen.height/2, dx = 1, dy = 1)

    games.screen.add(pizza)

    games.screen.mainloop()

main()

#win_message = games.Message(value = "You won!",
                                                   # size = 100,
                                                  #  color = color.red,
                                                   # x = games.screen.width/2,
                                                   # y = games.screen.height/2,
                                                   # lifetime = 250,
                                                   # after_death = games.screen.quit)
