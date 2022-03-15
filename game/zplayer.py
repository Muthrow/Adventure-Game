""" Represents the player """
import arcade
from game.constants import RESOURCE_PATH, PLAYER_SCALE, PLAYER_SPEED
class Player(arcade.Sprite):
    """ Represents the player """
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        filename = f"{RESOURCE_PATH}Player/player_idle.gif"
        self.speed = PLAYER_SPEED
        self.hitPoints = 3
        self.damage = 1
        self.vel_x = 0
        self.vel_y = 0
        #super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        super().__init__(filename, PLAYER_SCALE, center_x=center_x, center_y=center_y)

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

    def update(self):
        self.move()
        return super().update()