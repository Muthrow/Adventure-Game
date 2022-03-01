from arcade import Sprite

class EnemySprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 1
        self.damage = 1
        self.center_x = 100
        self.center_y = 100
    
    def update(self):
        super().update()
        # here is where we will add the movement and set the scene for encounters
        ""

    def getHealth(self):
        return self.hitPoints

    def getDamage(self):
        return self.damage

    def onHit(self, damage = 1):
        self.hitPoints -= damage