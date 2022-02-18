""" Represents the player """
import arcade
class Player(arcade.Sprite):
    """ Represents the player """
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        filename = "game\\resources\\player.png"
        self.speed = 3
        #super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        super().__init__(filename, 2, center_x=center_x, center_y=center_y)

    def move(self, x, y):
        self.change_x = x * self.speed
        self.change_y = y * self.speed