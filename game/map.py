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
        self.player_spawn = (538, 160)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (1484.0, 1108),
            (1598.0, 1450),
            (956.0, 1448),
            (588.0, 1020),
            (804.0, 756),
            (252.0, 546),
            (270.0, 1260),
            (246.0, 1500),
            (516.0, 1368),
            (462.0, 1710),
            (180.0, 1662)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')

class Cross_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map2.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (200, 1708)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (234.0, 1170),
            (666.0, 1566),
            (1100.0, 1512),
            (1574.0, 1566),
            (1580.0, 1044),
            (1556.0, 702),
            (1436.0, 452),
            (1046.0, 222),
            (680.0, 92),
            (476.0, 308),
            (140.0, 344),
            (698.0, 716),
            (920.0, 560),
            (1136.0, 830),
            (842.0, 1052)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')


class Other_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map3.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (92, 1708)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = [
            (182.0, 1448),
            (182.0, 1214),
            (596.0, 1610),
            (1104.0, 1390),
            (1320.0, 1564),
            (1536.0, 1192),
            (1020.0, 771.5),
            (732.0, 1005.5),
            (912.0, 1197.5),
            (648.0, 579.5),
            (276.0, 603.5),
            (654.0, 207.5),
            (1532.0, 555.5),
            (1460.0, 261.5)
        ]
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')

class Boss_Arena(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map4.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (92, 100)
        self.boss_spawns = [240,240]
        self.grunt_spawns = [
            (160,240),
            (320,240),
            (240,160),
            (240,320)
        ]
        self.captain_spawns = None
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
        print('======= Done')