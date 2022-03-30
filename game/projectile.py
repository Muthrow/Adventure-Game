import arcade
from game.constants import RESOURCE_PATH, PLAYER_SCALE
from game.zplayer import Player

class Projectile(arcade.Sprite):
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        filename = f"{RESOURCE_PATH}Player\exec1_axehead.png"
        self.damage = 1
        self.spriteList = None
        self.offset = 8
        super().__init__(filename, 0.5, center_x=center_x, center_y=center_y)

    def setSpriteList(self, spriteList):
        self.spriteList = spriteList

    def hit(self):
        collisionList = self.collides_with_list(self.spriteList)
        if len(collisionList) != 0:
            collisionList[0].onHit()
    
    def update(self, player):
        playerPosition = player.getPosition()
        self.center_x = playerPosition[0]
        self.center_y = playerPosition[1]
        direction = player.getDirection()

        if direction == 0:
            self.center_y -= self.offset - 6
        elif direction == 1:
            self.center_y += self.offset + 1
        elif direction == 2:
            self.center_x -= self.offset - 3
        elif direction == 3:
            self.center_x += self.offset - 3

