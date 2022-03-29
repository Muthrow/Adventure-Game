from arcade import Sprite
from time import time
import random
from game.constants import ENEMY_SCALE, RESOURCE_PATH


class EnemySprite(Sprite):

    def __init__(self, position):
        super().__init__(filename=f"{RESOURCE_PATH}beast_hero.png", scale=ENEMY_SCALE)
        self.hitPoints = 3
        self.damage = 1
        self.center_x = position[0]
        self.center_y = position[1]
        self.vel_x = 1
        self.vel_y = 1
        self.speed = 16
        self.start_timer = time()
        
        self.left_limit = self.center_x - 100
        self.right_limit = self.center_x + 100
        self.top_limit = self.center_y + 100
        self.bottom_limit = self.center_y - 100
        # print(f'({self.center_x},{self.center_y})')

    def update(self):
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()
        self.move()

    def move(self):
        # if self.center_x < self.left_limit:
        #     self.center_x = self.left_limit
        #     self.change_x *= -1
        # if self.center_x > self.right_limit:
        #     self.center_x = self.right_limit
        #     self.change_x *= -1
        # if self.center_y > self.top_limit:
        #     self.center_y = self.top_limit
        #     self.change_y *= -1
        # if self.center_y < self.bottom_limit:
        #     self.center_y = self.bottom_limit
        #     self.change_y *= -1

        if self.start_timer + 2.5 <= time():
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
                dir_x = -1
                dir_y = -1
            elif direction == 5:
                dir_y = -1
            elif direction == 6:
                dir_x = -1
                dir_y = 1
            elif direction == 7:
                dir_x = -1
            elif direction == 8:
                dir_x = 1
                dir_y = -1

            self.change_x = self.center_x + (dir_x * self.speed)
            self.change_y = self.center_y + (dir_y * self.speed)
            self.start_timer = time()

        if self.center_x != self.change_x:
            if self.center_x < self.change_x:
                self.center_x += self.vel_x

            elif self.center_x > self.change_x:
                self.center_x -= self.vel_x

        if self.center_y != self.change_y:
            if self.center_y < self.change_y:
                    self.center_y += self.vel_y

            elif self.center_y > self.change_y:
                self.center_y -= self.vel_y


    def setDirection(self, x, y):
        self.vel_x += x * self.speed
        self.vel_y += y * self.speed

    def getHealth(self):
        return self.hitPoints

    def getDamage(self):
        return self.damage

    def onHit(self, damage = 1):
        self.hitPoints -= damage