# NOTES DE COURS EXAM

from livewires import games, color
import random as fuck
import math


# Background --------------------------------------------------------------------------------------
games.init(screen_width = 640, screen_height = 480, fps = 50)
nebulaImage = games.load_image("nebula.jpg", transparent = False)
games.screen.background = nebulaImage
# ----------------------------------------------------------------------------------------------------------

# Animation-------------------------------------------------------------------------------------------
explosionFiles = ["explosion1.bmp",
                          "explosion2.bmp",
                          "explosion3.bmp",
                          "explosion4.bmp",
                          "explosion5.bmp",
                          "explosion6.bmp",
                          "explosion7.bmp",
                          "explosion8.bmp",
                          "explosion9.bmp",]
explosion = games.Animation(images = explosionFiles,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            n_repeats = 0,
                            repeat_interval = 5)
games.screen.add(explosion)
# -----------------------------------------------------------------------------------------------------------

# Load/Play Sound ----------------------------------------------------------------------------------
missileSound = games.load_sound("missile.wav")
missileSound.play(0)
# -----------------------------------------------------------------------------------------------------------

# Load/Play Music ----------------------------------------------------------------------------------
games.music.load("theme.mid")
games.music.play()
# ------------------------------------------------------------------------------------------------------------


# Bouncing Pizza--------------------------------------------------------------------------------------
class Pizza(games.Sprite):
    def update(self):
        """ invert velocity component if edge of screen reached """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy
    def handle_collide(self):
        """ Move to random Pos """
        self.x = fuck.randrange(games.screen.width)
        self.y = fuck.randrange(games.screen.height)

pizzaImage = games.load_image("pizza.bmp")
pizza = Pizza(image = pizzaImage, x = games.screen.width/2, y = games.screen.height/2, dx = 1, dy = 1)
games.screen.add(pizza)
# ------------------------------------------------------------------------------------------------------------


# Rotating Pizza--------------------------------------------------------------------------------------
class RotPizza(games.Sprite):
    def update(self):
        """ Rotates Pizza """
        self.set_angle(self.get_angle() + 1)
    def handle_collide(self):
        """ Move to random Pos """
        self.x = fuck.randrange(games.screen.width)
        self.y = fuck.randrange(games.screen.height)

rotpizzaImage = games.load_image("pizza.bmp")
rotpizza = RotPizza(image = rotpizzaImage, x = games.screen.width/4, y = games.screen.height/4, dx = 0, dy = 0)
games.screen.add(rotpizza)
# ------------------------------------------------------------------------------------------------------------


# Object following Mouse---------------------------------------------------------------------------
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
            pizza.destroy

panImage = games.load_image("pan.bmp")
pan = Pan(image = panImage, x = games.mouse.x, y = games.mouse.y)
games.screen.add(pan)
games.mouse.is_visible = False # Disables mouse
games.screen.event_grab = True # Locks mouse in screen
# ------------------------------------------------------------------------------------------------------------


# Keyboard Moving Pizza---------------------------------------------------------------------------
class KeyboardPizza(games.Sprite):
    def update(self):
        """ Moves using keyboard keys """
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        
    def handle_collide(self):
        """ Move to random Pos """
        self.x = fuck.randrange(games.screen.width)
        self.y = fuck.randrange(games.screen.height)

keypizzaImage = games.load_image("pizza.bmp")
keypizza = KeyboardPizza(image = keypizzaImage, x = games.screen.width/6, y = games.screen.height/6, dx = 0, dy = 0)
games.screen.add(keypizza)
# ------------------------------------------------------------------------------------------------------------

# Follow mouse CANON ---------------------------------------------------------------------------
class Canon(games.Sprite):
    def update(self):
        mouseX = games.mouse.x
        mouseY = games.mouse.y
        midX = mouseX - self.x
        midY = mouseY - self.y
        self.angle = math.degrees(math.atan2(midY, midX) - math.pi/2)

        dx = math.cos(math.radians(self.angle + 90))
        dy = math.sin(math.radians(self.angle + 90))
        
canonImage = games.load_image("arrow.png", transparent = True)
arrow = Canon(image = canonImage, x = games.screen.width/2, y = 0)
games.screen.add(arrow)
# ------------------------------------------------------------------------------------------------------------


# Text -----------------------------------------------------------------------------------------------------
score = games.Text(value = 1756521, size = 60, color = color.black, x = 550, y = 30)
games.screen.add(score)
# ------------------------------------------------------------------------------------------------------------



def main():
    games.screen.mainloop()

main()


