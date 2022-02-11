from arcade import SpriteList, View, Sound, Window
from arcade.key import ESCAPE, F11, W, A, S, D
import arcade
from time import time
from zplayer import Player
import constants as c
#Here is where we will import the classes from other files scripts\game\zplayer.py
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False, update_rate: float = 1 / 60, antialiasing: bool = True, screen = None):
        #Define attributes here
        self.keep_playing = True
        self.background = SpriteList()
        self.island = SpriteList()
        self.castle = SpriteList()
        self.player = Player()
        map = arcade.read_tmx("resources\Maps\\untitled.tmx")
        self.background = arcade.process_layer(map,'Water')
        self.island = arcade.process_layer(map,'Island')
        self.castle = arcade.process_layer(map,'Castle')
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing, screen)

    def start_game(self):
        """Starts the game"""
        while self.keep_playing:
            self.inputs()
            self.updates()
            self.outputs()

    def inputs(self):
        """Gets user input"""
        #This is where we will get the input to the user and store it in a variable to be used
        self.on_key_press

    def on_key_press(self, symbol, modifiers):
        if symbol == ESCAPE:
            self.keep_playing = False

        if symbol == W:
            self.player.move(0,1)
        if symbol == A:
            self.player.move(-1,0)
        if symbol == S:
            self.player.move(0,-1)
        if symbol == D:
            self.player.move(1,0)
        # if symbol == F11:
        #     Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE, resizable = True, fullscreen = False)

    def on_draw(self):
        self.background.draw()
        self.island.draw()
        self.castle.draw()
        return super().on_draw()

    def updates(self):
        """Updates the game every tick"""
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function