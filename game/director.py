"""
TODO:
 * implement setup function
 * water and lava collision
 * set up cameras (maybe)
 * map switching
 * foreground layer

"""
from arcade import SpriteList, View, Sound, Window
from arcade.key import ESCAPE, F, W, A, S, D, U
import arcade
import arcade.gui
import game.questions as qs
from random import randint
from time import time
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, RESOURCE_PATH, MAP_SCALING, PLAYER_SCALE
from game.zplayer import Player
from game.dialogue import Dialogue
from game.enemySprite import EnemySprite
#import game.constants as c
#Here is where we will import the classes from other files
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False)

        layer_options = {
            "water": {
                "use_spatial_hash": True,
            },
            "lava": {
                "use_spatial_hash": True,
            },
            "obstacle": {
                "use_spatial_hash": True,
            },
        }
        #Define attributes here
        self.keep_playing = True
        self.score = 0
        self.ground = SpriteList()
        self.water = SpriteList()
        self.obstacle = SpriteList()
        self.inMenu = False
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        self.lava = SpriteList()
        self.door = SpriteList()
        self.player = Player(center_x=250,center_y=250)
        self.enemy = EnemySprite(f"{RESOURCE_PATH}ghost.png", PLAYER_SCALE/2)
        #self.tile_map = None
        #self.scene = None
        # self.tile_map = arcade.load_tilemap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING)
        self.tile_map = arcade.TileMap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])
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
        if not self.inMenu:
            if symbol == W:
                self.player.setDirection(0,1)
            if symbol == A:
                self.player.setDirection(-1,0)
            if symbol == S:
                self.player.setDirection(0,-1)
            if symbol == D:
                self.player.setDirection(1,0)
            if symbol == U:
                myQ = randint(0, len(qs.questions) - 1)
                question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)
        
    def on_key_release(self, symbol: int, modifiers: int):
        if not self.inMenu:
            if symbol == W:
                self.player.setDirection(0,-1)
            if symbol == A:
                self.player.setDirection(1,0)
            if symbol == S:
                self.player.setDirection(0,1)
            if symbol == D:
                self.player.setDirection(-1,0)
        return super().on_key_release(symbol, modifiers)

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player.draw()
        self.enemy.draw()
        self.manager.draw()
        #self.ground.draw()
        #self.island.draw()
        #self.castle.draw()
        return super().on_draw()

    def update(self, delta_time: float):
        """Updates the game every tick"""
        self.scene.update()
        # self.ground.update()
        # self.obstacle.update()
        # self.water.update()
        self.player.update()
        self.physics.update()
        return super().update(delta_time)
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function