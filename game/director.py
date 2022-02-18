from arcade import SpriteList, View, Sound, Window
from arcade.key import ESCAPE, F
import arcade
from time import time
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, RESOURCE_PATH
from game.zplayer import Player
#import game.constants as c
#Here is where we will import the classes from other files
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(Window):
    def __init__(self):

        layer_options = {
            "Water": {
                "use_spatial_hash": True,
            },
            "Island": {
                "use_spatial_hash": True,
            },
            "Castle": {
                "use_spatial_hash": True,
            },
        }
        #Define attributes here
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        self.keep_playing = True
        self.background = SpriteList()
        self.island = SpriteList()
        self.castle = SpriteList()
        self.player = Player()
        #self.tile_map = None
        #self.scene = None
        self.tile_map = arcade.load_tilemap(RESOURCE_PATH + "Maps\\untitled.tmx")
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        #, update_rate, antialiasing, screen
        #had to remove this from super.__init__
    

    def start_game(self):
        """Starts the game"""
        while self.keep_playing:
            self.inputs()
            self.update()
            self.outputs()

    def inputs(self):
        """Gets user input"""
        #This is where we will get the input to the user and store it in a variable to be used
        # self.on_key_press
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == ESCAPE:
            arcade.close_window()
        if symbol == F:
            self.set_fullscreen(not self.fullscreen)
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player.draw()
        #self.background.draw()
        #self.island.draw()
        #self.castle.draw()
        return super().on_draw()

    def updates(self):
        """Updates the game every tick"""
        self.background.update()
        self.castle.update()
        self.island.update()
        self.player.update()
        return super().update(delta_time)
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function