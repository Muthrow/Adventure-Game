""" Main class and Game Runner """

import arcade

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Game(arcade.Window):
    """ Main game Class. Handles all game logic """

    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

    def setup(self):
        pass

    def update(self, delta_time: float):
        """ Update game """
        return super().update(delta_time)

def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Your Mom', False)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()