"""
TODO:
 * implement setup function
 * water and lava collision
 * set up cameras (maybe)
 * map switching
 * foreground layer
"""
from sqlite3 import Time
from arcade import SpriteList, View, Sound, Window
from arcade.key import ESCAPE, F, W, A, S, D, SPACE, M, Q, U
import arcade
import arcade.gui
import game.questions as qs
from random import randint
from time import time
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, RESOURCE_PATH, MAP_SCALING, PLAYER_SCALE
from game.zplayer import Player
from game.dialogue import Dialogue
from game.enemySprite import EnemySprite
from game.map import Cross_Dungeon, Other_Dungeon, Overworld, Map
from game.projectile import Projectile

#import game.constants as c
#Here is where we will import the classes from other files
"""
Director Class:
Class that hanldes the main game view. Inherits from Arcade View.
"""

class Director(Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=False)

        self.maps = [Overworld(), Cross_Dungeon(), Other_Dungeon()]
        self.map_num = 0
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
        self.player = Player()
        self.enemy = EnemySprite(f"{RESOURCE_PATH}beast_hero.png", PLAYER_SCALE/2)
        self.enemySprites = SpriteList(use_spatial_hash = False)
        self.enemySprites.append(self.enemy)
        self.projectile = Projectile()

        #self.tile_map = None
        #self.scene = None
        # self.tile_map = arcade.load_tilemap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING)
        # self.tile_map = arcade.TileMap(RESOURCE_PATH + "Maps\\map1.tmj", scaling=MAP_SCALING, layer_options=layer_options)
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        # self.physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])
        #, update_rate, antialiasing, screen
        #had to remove this from super.__init__
        self.wall_physics = None
        self.water_physics = None
        self.setup()

    def setup(self):
        # layer_options = {
        #     "water": {
        #         "use_spatial_hash": True,
        #     },
        #     "lava": {
        #         "use_spatial_hash": True,
        #     },
        #     "obstacle": {
        #         "use_spatial_hash": True,
        #     },
        # }
        cur_map = self.maps[self.map_num % 3]
        self.player.center_x, self.player.center_y = cur_map.player_spawn
        # self.tile_map = arcade.TileMap(cur_map.filename, scaling=MAP_SCALING, layer_options=layer_options)
        self.scene = arcade.Scene.from_tilemap(cur_map)
        # cur_map.set_doors(self.scene['door'], cur_map.filename)
        self.wall_physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])
        self.water_physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['water'])
        # self.door = arcade.PhysicsEngineSimple(self.player, walls=self.scene['door'])

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
        if symbol == Q:
            print(self.player.position)
        if symbol == M:
            self.map_num = (self.map_num + 1) % 3
            self.setup()
        if symbol == SPACE:
            self.projectile.setSpriteList(self.enemySprites)
            self.player.attack(self.projectile)
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
        self.player.update_animation()
        self.player.draw()
        self.enemy.draw()
        self.projectile.draw()
        #self.ground.draw()
        #self.island.draw()
        #self.castle.draw()
        self.scene['foreground'].draw()
        self.manager.draw()
        return super().on_draw()

    def update(self, delta_time: float):
        """Updates the game every tick"""
        self.scene.update()
        # self.ground.update()
        # self.obstacle.update()
        # self.water.update()
        self.player.update()
        self.wall_physics.update()
        self.water_physics.update()
        self.enemy.update()
        self.projectile.update(self.player)
        # check if we walk through a door
        if len(arcade.check_for_collision_with_list(self.player, self.scene['door'])) >= 1:
            self.map_num += 1
            self.setup()
        # check if we walk into a question space
        question_list = arcade.check_for_collision_with_list(self.player, self.scene['question'])
        if len(question_list) >= 1:
            myQ = randint(0, len(qs.questions) - 1)
            sc = self.score
            Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)
            # question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)
            # put pause here
            if sc == self.score:
                pass
            # spawn enemies adn stuff
            question_list.pop().kill()


        return super().update(delta_time)
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this function