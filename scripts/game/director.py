from arcade import SpriteList, View, Camera, Sound, Scene
from time import time
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

    def updates(self):
        """Updates the game every tick"""
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function