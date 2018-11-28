
from livewires import games, color
import math


canShoot = True
shotCount = 5
scoreValue = 0

games.init(screen_width = 630, screen_height = 630, fps = 50)

score = games.Text(scoreValue, size = 40, color = color.green, x = 580, y = 30)
games.screen.add(score)

BackImage = games.load_image("background.jpg", transparent = False)
games.screen.background = BackImage


class Peggle(games.Sprite):
    def update(self):
        self.x
        self.y
        self.check_collide()

    def check_collide(self):
        for Pokeball in self.overlapping_sprites:
            Pokeball.handle_collide()
            global scoreValue
            scoreValue += 1
            updateScore()
            self.destroy()

def setPeggles():
    distanceX = 0
    distanceY = 0

    while distanceX < 585:
        distanceX += 45
        distanceY = 100
        while distanceY < 455:
            distanceY += 45
            peggleImage = games.load_image("peggle.png", transparent = True)
            peggle = Peggle(image = peggleImage, x = distanceX, y = distanceY)
            games.screen.add(peggle)

class Mew(games.Sprite):
    def update(self):
        if self.right > (games.screen.width ) or self.left < 0:
            self.dx = -self.dx
        self.check_collide()
        
    def check_collide(self):
        for Pokeball in self.overlapping_sprites:
            Pokeball.handle_collide()
            self.destroy()
            global shotCount
            shotCount += 1

def setMew():
    PosX = 60
    PosY = 570
    mewImage = games.load_image("mew.png", transparent = True)
    mew = Mew(image = mewImage, x = PosX , y = PosY, dx = 1, dy = 0)
    games.screen.add(mew)

class Canon(games.Sprite):
    def update(self):
        mouseX = games.mouse.x
        mouseY = games.mouse.y
        midX = mouseX - self.x
        midY = mouseY - self.y
        self.angle = math.degrees(math.atan2(midY, midX) - math.pi/2)
        
        games.mouse.set_is_visible(False)

        dx = math.cos(math.radians(self.angle + 90))
        dy = math.sin(math.radians(self.angle + 90))
        
        global canShoot
        
        if games.mouse.is_pressed(0):
            if canShoot:
                canShoot = False
                setPokeball(dx * 5, dy )


def setCanon():
    canonImage = games.load_image("arrow.png", transparent = True)
    arrow = Canon(image = canonImage, x = games.screen.width/2, y = 0)
    games.screen.add(arrow)

class Pokeball(games.Sprite):
    def update(self):
        self.dy += 0.1
        if self.y >= 600:
            global canShoot
            canShoot = True
            self.destroy()
        if self.right >= games.screen.width:
            self.dx = -self.dx
        if self.left <= 0:
            self.dx = -self.dx
    def handle_collide(self):
        self.dy = -self.dy * 0.8
        self.dx
                

def setPokeball(dx, dy):
    PosX = games.screen.width/2
    PosY = 0

    pokeballImage = games.load_image("pokeball.png", transparent = True)
    pokeball = Pokeball(image = pokeballImage, x = PosX, y = PosY, dx = dx, dy = dy)
    games.screen.add(pokeball)


def updateScore():
    global score
    global scoreValue
    score.set_value(scoreValue)
    
def main():
    setPeggles()    
    setCanon()
    setMew()
    games.screen.mainloop()
    

main()


