import arcade
from game.constants import MAP_SCALING, RESOURCE_PATH, LAYER_OPTIONS
from game.door import Door

class Map(arcade.TileMap):
    """ Creates and stores map information. Could be expanded in the future to allow for persistent changes between loads """
    def __init__(self, map_file = "", scaling = MAP_SCALING, layer_options = LAYER_OPTIONS):
        super().__init__(map_file, scaling, layer_options)
        # self.door_list = list()
        print(f'Loading {self.filename[-8:-4]} =======', end='')


    def set_doors(self, door_list, map_name):
        for door in door_list:
            door = Door(door.position, map_name)
            self.door_list.append(door)


class Overworld(Map):
    """ Object containing all the data for the overworld map """
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map1.tmj"
        super().__init__(map_file=self.filename)
        print('=',end='')
        self.player_spawn = (269, 80)
        print('=',end='')
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (742.0, 554),
            (799.0, 725),
            (478.0, 724),
            (294.0, 510),
            (402.0, 378),
            (126.0, 273),
            (135.0, 630),
            (123.0, 750),
            (258.0, 684),
            (231.0, 855),
            (90.0, 831)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')

class Cross_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map2.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (100, 854)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (117.0, 585),
            (333.0, 783),
            (550.0, 756),
            (787.0, 783),
            (790.0, 522),
            (778.0, 351),
            (718.0, 126),
            (523.0, 111),
            (340.0, 46),
            (238.0, 154),
            (70.0, 172),
            (349.0, 358),
            (460.0, 280),
            (568.0, 415),
            (421.0, 526)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')


class Other_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map3.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (46, 854)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (91.0, 724),
            (91.0, 607),
            (298.0, 805),
            (552.0, 695),
            (660.0, 782),
            (768.0, 596),
            (510.0, 385.75),
            (366.0, 502.75),
            (456.0, 598.75),
            (324.0, 289.75),
            (138.0, 301.75),
            (327.0, 103.75),
            (766.0, 277.75),
            (730.0, 130.75)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')
