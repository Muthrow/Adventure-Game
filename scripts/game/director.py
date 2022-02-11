from arcade import SpriteList, View, Camera, Sound, Scene, Window
from arcade.key import ESCAPE, F11
from time import time
import constants as c
#Here is where we will import the classes from other files
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(View):
    def __init__(self):
        #Define attributes here
        self.keep_playing = True

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
        if symbol == F11:
            Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE, resizable = True, fullscreen = False)

    def updates(self):
        """Updates the game every tick"""
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function