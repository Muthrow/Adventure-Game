import arcade
from game.constants import MAP_SCALING, RESOURCE_PATH, LAYER_OPTIONS
from game.door import Door

class Map(arcade.TileMap):
    """ Creates and stores map information. Could be expanded in the future to allow for persistent changes between loads """
    def __init__(self, map_file = "", scaling = MAP_SCALING, layer_options = LAYER_OPTIONS):
        super().__init__(map_file, scaling, layer_options)
        # self.door_list = list()


    def set_doors(self, door_list, map_name):
        print('========================', self.filename)
        for door in door_list:
            door = Door(door.position, map_name)
            self.door_list.append(door)


class Overworld(Map):
    """ Object containing all the data for the overworld map """
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map1.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (250, 250)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = None
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)

class Cross_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map2.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (100, 854)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = None
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)

class Other_Dungeon(Map):
    def __init__(self):
        self.filename = RESOURCE_PATH + "Maps\\map3.tmj"
        super().__init__(map_file=self.filename)
        self.player_spawn = (46, 854)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = None
        self.door_list = list()
        self.set_doors(self.sprite_lists['door'], self.filename)
