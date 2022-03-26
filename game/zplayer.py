""" Represents the player """
import arcade
from game.constants import RESOURCE_PATH, PLAYER_SCALE, PLAYER_SPEED, PLAYER_SPRITES
class Player(arcade.Sprite):
    """ Represents the player """
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        filename = f"{RESOURCE_PATH}Player\exec1_down (2).png"
        self.speed = PLAYER_SPEED
        self.hitPoints = 3
        self.damage = 1
        self.vel_x = 0
        self.vel_y = 0
        self.playerDirection = 0
        self.animationFrame = 0
        self.animationSpeed = 2
        self.spriteList = None
        #super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        super().__init__(filename, 0.5, center_x=center_x, center_y=center_y)

    def move(self):
        self.change_x = self.vel_x
        self.change_y = self.vel_y
        # print(self.position)

    def setDirection(self, x, y):
        self.vel_x += x * self.speed
        self.vel_y += y * self.speed
        if self.vel_y < 0:
            self.playerDirection = 0
        elif self.vel_y > 0:
            self.playerDirection = 1
        elif self.vel_x < 0:
            self.playerDirection = 2
        elif self.vel_x > 0:
            self.playerDirection = 3

    def getHealth(self):
        return self.hitPoints

    def getDamage(self):
        return self.damage

    def onHit(self, damage = 1):
        self.hitPoints -= damage

    def update_animation(self):
        if self.vel_x != 0 or self.vel_y != 0:
            if self.animationFrame >= 3 * self.animationSpeed:
                self.animationFrame = 0
            else:
                self.animationFrame += 1
        else:
           self.animationFrame = 0
        self.texture = arcade.load_texture(f"{RESOURCE_PATH}{PLAYER_SPRITES[self.playerDirection][int(self.animationFrame/self.animationSpeed)]}")

    def update(self):
        self.move()
        return super().update()

    def setSpriteList(self, spriteList):
        self.spriteList = spriteList

    def attack(self, projectile):
        projectile.hit()

    def getDirection(self):
        return self.playerDirection

    def getPosition(self):
        return [self.center_x, self.center_y]