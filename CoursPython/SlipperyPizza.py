# Slippery Pizza program
# Demonstrates testing for sprite collisions

from livewires import games
import random as fuck

# First thing that needs to be done
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """ A pan controlled by mouse """
    def update(self):
        """ Move to mouse position """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """ Check for collision with pizza """
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

class Pizza(games.Sprite):
    """ A Slippery pizza """
    def handle_collide(self):
        """ Move to random Pos """
        self.x = fuck.randrange(games.screen.width)
        self.y = fuck.randrange(games.screen.height)
        
def main():
    backImage = games.load_image("pokemon.jpg", transparent = False)
    games.screen.background = backImage

    pizzaImage = games.load_image("pizza.bmp")
    pizzaPosX = fuck.randrange(games.screen.width)
    pizzaPosY = fuck.randrange(games.screen.height)
    pizza = Pizza(image = pizzaImage, x = pizzaPosX, y = pizzaPosY)
    games.screen.add(pizza)

    panImage = games.load_image("pan.bmp")
    pan = Pan(image = panImage, x = games.mouse.x, y = games.mouse.y)
    games.screen.add(pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

# Start the game
main()
