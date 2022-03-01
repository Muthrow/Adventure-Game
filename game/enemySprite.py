from arcade import Sprite

class EnemySprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 1
        self.damage = 1
        self.center_x = 100
        self.center_y = 100
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.move()
        super().update()
        # here is where we will add the movement and set the scene for encounters
        ""

    def move(self):
        self.change_x = self.vel_x
        self.change_y = self.vel_y

    def setDirection(self, x, y):
        self.vel_x += x * self.speed
        self.vel_y += y * self.speed

    def getHealth(self):
        return self.hitPoints

    def getDamage(self):
        return self.damage

    def onHit(self, damage = 1):
        self.hitPoints -= damage