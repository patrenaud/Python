
from livewires import games, color
import math

canShoot = True
shotCount = 10
scoreValue = 10
totalScore = 0
pegglesHit = 0
totalPeggles = 104
mewHit = False

games.init(screen_width = 630, screen_height = 630, fps = 50)

# This is to show score
score = games.Text(0, size = 40, color = color.green, x = 580, y = 30)
games.screen.add(score)

# This is to show balls remaining
pokeballCount = games.Text("Balls remaining: " + str(shotCount), size = 30, color = color.red, x = 90, y = 30)
games.screen.add(pokeballCount)

# this is to show Background image
BackImage = games.load_image("background.jpg", transparent = False)
games.screen.background = BackImage

# Theme music
games.music.load("chanson.wav")
games.music.play(-1)

# Sounds
shootSound = games.load_sound("fire.wav")
hitSound = games.load_sound("hit.wav")
mewSound = games.load_sound("mewSound.wav")
yaySound = games.load_sound("yay.wav")
booSound = games.load_sound("boo.wav")


class Peggle(games.Sprite):
    def update(self):
        self.x
        self.y
        self.check_collide()

    def check_collide(self):
        for Pokeball in self.overlapping_sprites:
            Pokeball.handle_collide(self.x)
            global pegglesHit
            global totalPeggles
            totalPeggles -= 1
            pegglesHit += 1
            
            updateScore(pegglesHit)
            hitSound.play(0)
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
            Pokeball.handle_collide(self.x)
            self.destroy()
            global shotCount
            shotCount += 1
            global mewHit
            mewHit = True
            updateShots()
            mewSound.play(0)
            

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
                shootSound.play(0)
                canShoot = False
                setPokeball(dx * 5, dy )
                global shotCount
                shotCount -= 1
                updateShots()


def setCanon():
    canonImage = games.load_image("arrow.png", transparent = True)
    arrow = Canon(image = canonImage, x = games.screen.width/2, y = 0)
    games.screen.add(arrow)

class Pokeball(games.Sprite):
    def update(self):
        self.dy += 0.1
        if self.y >= 600:
            global totalPeggles
            global pegglesHit
            global canShoot
            global shotCount
            global mewHit

            pegglesHit = 0
            canShoot = True
            self.destroy()
                        
            # re-instantiate mew if gone
            if mewHit == True:
                setMew()
                mewHit = False

            # If game is won
            if totalPeggles <= 0:
                canShoot = False
                winGame()
                
            # If game is lost
            elif shotCount == 0:
                canShoot = False
                gameOver()

        if self.right >= games.screen.width:
            self.dx = -self.dx
        if self.left <= 0:
            self.dx = -self.dx
    def handle_collide(self, Px):
        self.dy = -self.dy * 0.8
        self.set_dx((self.x - Px) * 0.15) 
                

def setPokeball(dx, dy):
    PosX = games.screen.width/2
    PosY = 0

    pokeballImage = games.load_image("pokeball.png", transparent = True)
    pokeball = Pokeball(image = pokeballImage, x = PosX, y = PosY, dx = dx, dy = dy)
    games.screen.add(pokeball)


def updateScore(hit):
    global score
    global ScoreValue
    global totalScore

    totalScore += scoreValue * hit
    
    score.set_value(totalScore)

def updateShots():
    global pokeballCount
    global shotCount
    pokeballCount.set_value("Balls remaining: " + str(shotCount))

def gameOver():
    global BackImage
    BackImage = games.load_image("gameover.jpg", transparent = False)
    games.screen.background = BackImage
    
    booSound.play(-1)
    games.music.stop()
    
    global pokeballCount
    global shotCount
    pokeballCount.set_value("YOU LOOSE")

def winGame():
    global BackImage
    BackImage = games.load_image("wingame.png", transparent = False)
    games.screen.background = BackImage
    
    yaySound.play(-1)
    games.music.stop()
    
    global pokeballCount
    global shotCount
    pokeballCount.set_value("YOU WIN")
    
def main():
    setPeggles()    
    setCanon()
    setMew()
    games.screen.mainloop()
    

main()


