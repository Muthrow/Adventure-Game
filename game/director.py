"""
TODO:
 * implement setup function
 * water and lava collision
 * set up cameras (maybe)
 * map switching
 * foreground layer
"""
from arcade import SpriteList, View, Sound, Window
from arcade.key import ESCAPE, F, W, A, S, D, SPACE
import arcade
from time import time
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, RESOURCE_PATH, MAP_SCALING, PLAYER_SCALE
from game.zplayer import Player
from game.enemySprite import EnemySprite
from game.map import Overworld, Map
#import game.constants as c
#Here is where we will import the classes from other files
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(Window):
    def __init__(self):

        self.maps = [Overworld()]
        self.map_num = 0
        #Define attributes here
        self.keep_playing = True
        self.ground = SpriteList()
        self.water = SpriteList()
        self.obstacle = SpriteList()
        self.lava = SpriteList()
        self.door = SpriteList()
        self.player = Player()
        self.enemy = EnemySprite(f"{RESOURCE_PATH}ghost.png", PLAYER_SCALE/2)
        #self.tile_map = None
        #self.scene = None
        # self.tile_map = arcade.load_tilemap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING)
        # self.tile_map = arcade.TileMap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING, layer_options=layer_options)
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        # self.physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])
        #, update_rate, antialiasing, screen
        #had to remove this from super.__init__
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False)
        self.setup()

    def setup(self):
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
        map = self.maps[self.map_num]
        self.player.center_x, self.player.center_y = map.player_spawn
        self.tile_map = arcade.TileMap(map.filename, scaling=MAP_SCALING, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])

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
        if symbol == W:
            self.player.setDirection(0,1)
        if symbol == A:
            self.player.setDirection(-1,0)
        if symbol == S:
            self.player.setDirection(0,-1)
        if symbol == D:
            self.player.setDirection(1,0)
        if symbol == SPACE:
            print(self.player.position)

    def on_key_release(self, symbol: int, modifiers: int):
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
        self.player.update_animation()
        self.player.draw()
        self.enemy.draw()
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
        self.enemy.update()
        return super().update(delta_time)
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function