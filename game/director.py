"""
TODO:
 * implement setup function
 * water and lava collision
 * set up cameras (maybe)
 * map switching
 * foreground layer
"""
from sqlite3 import Time
from arcade import SpriteList, Window, draw_text
from arcade.key import ESCAPE, F, W, A, S, D, SPACE, M, Q, U, P
from arcade.color import WHITE
import arcade
import arcade.gui
from numpy import arange
import game.questions as qs
from random import randint
from time import time
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, RESOURCE_PATH, MAP_SCALING, PLAYER_SCALE, AGGRO_DISTANCE
from game.zplayer import Player
from game.dialogue import Dialogue
from game.enemySprite import EnemySprite, Boss
from game.map import Boss_Arena, Cross_Dungeon, Other_Dungeon, Overworld, Map
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

        self.maps = [Overworld(), Cross_Dungeon(), Other_Dungeon(), Boss_Arena()]
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
        self.wrong = False
        self.lava = SpriteList()
        self.door = SpriteList()
        self.player = Player()
        self.boss = Boss((0,0), self.manager, self.score)
        # self.enemy = EnemySprite()
        # self.enemySprites.append(self.enemy)
        self.enemySprites = SpriteList()
        self.projectile = Projectile()
        self.camera = None
        self.question = None
        self.wall_physics = None
        self.water_physics = None
        self.setup()

    def setup(self):
        self.camera = arcade.Camera(self.width, self.height)
        if self.map_num > 4:
            print(f'Score: {self.score}')
            arcade.close()
        cur_map = self.maps[self.map_num]
        self.player.center_x, self.player.center_y = cur_map.player_spawn
        self.scene = arcade.Scene.from_tilemap(cur_map)
        self.wall_physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['obstacle'])
        self.water_physics = arcade.PhysicsEngineSimple(self.player, walls=self.scene['water'])
        #self.enemySprites.clear()
        if cur_map.boss_spawns != None:
            self.boss = Boss(cur_map.boss_spawns, self.manager, self.score)
            self.enemySprites.append(self.boss)
        for position in cur_map.grunt_spawns:
            self.enemySprites.append(EnemySprite(position))
            # pass
        myQ = randint(0, len(qs.questions) - 1)
        self.question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)

    def input(self):
        return

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
            print(str(self.player.getPosition()))
            print(str(self.projectile.getPosition()))
        if symbol == M:
            self.map_num = (self.map_num + 1) % 3
            self.setup()
        if symbol == SPACE:
            self.projectile.setSpriteList(self.enemySprites)
            self.player.attack(self.projectile)
        if symbol == U:
            myQ = randint(0, len(qs.questions) - 1)
            self.question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)
        if symbol == P:
            self.paused = not self.paused

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
        self.camera.use()
        self.scene.draw()
        self.player.draw()
        self.enemySprites.draw()
        # self.projectile.draw()
        #self.ground.draw()
        #self.island.draw()
        #self.castle.draw()
        self.scene['foreground'].draw()
        self.manager.draw()
        draw_text(f"Score: {self.score} | Player Health: {self.player.getHealth()}", 5, 5, WHITE, 14)
        return super().on_draw()

    def center_camera(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def update(self, delta_time: float):
        """Updates the game every tick"""

        # self.score = Dialogue.getScore()
        self.player.setSpriteList(self.enemySprites)
        question_list = arcade.check_for_collision_with_list(self.player, self.scene['question'])
        if len(question_list) >= 1:
            myQ = randint(0, len(qs.questions) - 1)
            self.question = Dialogue(qs.questions[myQ][0], qs.questions[myQ][1], qs.questions[myQ][2], self.manager, self.score)
            question_list.pop().kill()
        if self.question.score != self.score:
            self.score = self.question.score
        if not self.question.paused:
            self.scene.update()
            # self.ground.update()
            # self.obstacle.update()
            # self.water.update()
            self.player.update()
            self.wall_physics.update()
            self.water_physics.update()
            self.enemySprites.update()
            if len(self.enemySprites) <= 1:
                self.boss.vulnerable = True
            else:
                self.boss.vulnerable = False
            for enemy in self.enemySprites:
                wall = arcade.check_for_collision_with_lists(enemy,[self.scene['obstacle'],self.scene['water'],self.scene['lava']])
                if len(wall) >= 1:
                    for bump in wall:
                        if abs(bump.center_x - enemy.center_x) > abs(bump.center_y - enemy.center_y):
                            enemy.change_x *= -1
                        elif abs(bump.center_x - enemy.center_x) < abs(bump.center_y - enemy.center_y):
                            enemy.change_y *= -1
                        elif abs(bump.center_x - enemy.center_x) == abs(bump.center_y - enemy.center_y):
                            enemy.change_x *= -1
                            enemy.change_y *= -1
                if arcade.get_distance_between_sprites(enemy, self.player) <= AGGRO_DISTANCE:
                    enemy.aggro = True
                    # enemy.setChase(self.player.position)
                else:
                    enemy.aggro = False

            if self.boss != None:
                if self.boss.defeated:
                    print(self.score)
                    arcade.close()

            self.projectile.update(self.player)
            # check if we walk through a door
            if len(arcade.check_for_collision_with_list(self.player, self.scene['door'])) >= 1:
                self.map_num += 1
                self.setup()
            # check if we walk into a question space

        if self.question.wrong:
            en_cnt = randint(2,6)
            for enemy in range(en_cnt):
                new_enemy = EnemySprite((100,100))
                invalid = True
                while invalid:
                    spawn_x = randint(-100, 100) + self.player.center_x
                    spawn_y = randint(-100, 100) + self.player.center_y
                    new_enemy.set_position(spawn_x, spawn_y)
                    if len(arcade.check_for_collision_with_lists(new_enemy, [self.scene['obstacle'],self.scene['water'],self.scene['lava']])) <= 0:
                        invalid = False
                self.enemySprites.append(new_enemy)
            self.question.wrong = False



        self.center_camera()
        return super().update(delta_time)
        #Here is where we will use and process the variable containing the previous input

    def outputs(self):
        """Displays the game information that was updated in the updates function"""
        #We will add anything to be displayed that was updated in this functionf