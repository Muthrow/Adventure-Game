from arcade import Sprite
from time import time
import random

class EnemySprite(Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        self.hitPoints = 1
        self.damage = 1
        self.center_x = 100
        self.center_y = 100
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 10
        self.starttimer = time()

    def update(self):
        # if self.center_x < LIMIT_LEFT:
        #     self.center_x = LIMIT_LEFT
        #     self.change_x *= -1
        # if self.center_x > LIMIT_RIGHT:
        #     self.center_x = LIMIT_RIGHT
        #     self.change_x *= -1
        # if self.center_y > LIMIT_TOP:
        #     self.center_y = LIMIT_TOP
        #     self.change_y *= -1
        # if self.center_y < LIMIT_BOTTOM:
        #     self.center_y = LIMIT_BOTTOM
        #     self.change_y *= -1
        if self.starttimer + 2.5 <= time():   
            dir_x = 0
            dir_y = 0
            direction = random.randint(1, 8)
            if direction == 1:
                dir_y = 1
            elif direction == 2:
                dir_x = 1
                dir_y = 1
            elif direction == 3:
                dir_x = 1
            elif direction == 4:
                dir_x = 1
                dir_y = 1
            elif direction == 5:
                dir_y = 1
            elif direction == 6:
                dir_y = 1
                dir_x = 1
            elif direction == 7:
                dir_x = 1
            elif direction == 8:
                dir_x = 1
                dir_y = 1

            self.change_x = dir_x * self.speed
            self.change_y = dir_y * self.speed

            self.center_x += self.change_x
            self.center_y += self.change_y
            self.starttimer = time()

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