import arcade
from fileinput import filename
from turtle import position
from arcade import Sprite
from time import time
import random
from game.constants import ENEMY_SCALE, RESOURCE_PATH, ENEMY_SPRITES, BOSS_SPRITES
from game.dialogue import Dialogue
import game.questions as qs


class EnemySprite(Sprite):

    def __init__(self, position, filename=f"{RESOURCE_PATH}beast_hero.png"):
        super().__init__(filename=filename, scale=ENEMY_SCALE)
        self.hitPoints = 1
        self.damage = 1
        self.center_x = position[0]
        self.center_y = position[1]
        self.vel_x = 1
        self.vel_y = 1
        self.speed = 16
        self.start_timer = time()
        self.direction = 0
        self.sprites = ENEMY_SPRITES
        self.animationFrame = 0
        self.animationSpeed = 2
        self.aggro = False

        self.left_limit = self.center_x - 100
        self.right_limit = self.center_x + 100
        self.top_limit = self.center_y + 100
        self.bottom_limit = self.center_y - 100
        # print(f'({self.center_x},{self.center_y})')

    def setPlayer(self, player):
        self.player = player


    def update(self):
        if self.hitPoints <= 0:
            self.remove_from_sprite_lists()
        self.move()
        self.update_animation()

    def move(self):
        if self.start_timer + 2.5 <= time():
            dir_x = 0
            dir_y = 0
            direction = random.randint(1, 8)
            if direction == 1:
                dir_y = 1
                self.direction = 1
            elif direction == 2:
                dir_x = 1
                dir_y = 1
                self.direction = 3
            elif direction == 3:
                dir_x = 1
                self.direction = 3
            elif direction == 4:
                self.direction = 2
                dir_x = -1
                dir_y = -1
            elif direction == 5:
                self.direction = 0
                dir_y = -1
            elif direction == 6:
                self.direction = 2
                dir_x = -1
                dir_y = 1
            elif direction == 7:
                self.direction = 2
                dir_x = -1
            elif direction == 8:
                self.direction = 3
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

    def update_animation(self):
        if self.vel_x != 0 or self.vel_y != 0:
            if self.animationFrame >= 3 * self.animationSpeed:
                self.animationFrame = 0
            else:
                self.animationFrame += 1
        else:
            self.animationFrame = 0
        self.texture = arcade.load_texture(f"{RESOURCE_PATH}{self.sprites[self.direction][int(self.animationFrame/self.animationSpeed)]}")

    def setDirection(self, x, y):
        self.vel_x += x * self.speed
        self.vel_y += y * self.speed

    def getHealth(self):
        return self.hitPoints

    def getDamage(self):
        return self.damage

    def onHit(self, damage = 1):
        self.hitPoints -= damage


class Boss(EnemySprite):
    def __init__(self, position):
        super().__init__(filename=f"{RESOURCE_PATH}boss.png", position=position)
        self.scale = self.scale*0.4

    def ask(self, manager, score):
        myQ = random.randint(0, len(qs.questions) - 1)
        question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], manager, score)
        return

    def onHit(self, takeDamage=False, damage=1, manager=None, score=None):
        print("ouch")
        if takeDamage:
            self.ask(manager, score)
            return super().onHit(damage)
        else:
            return

    def update_animation(self):
        return
