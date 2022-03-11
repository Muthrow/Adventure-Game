import arcade
from game.constants import RESOURCE_PATH

class Map():
    """ Creates and stores map information. Could be expanded in the future to allow for persistent changes between loads """
    def __init__(self):
        self.filename = None
        self.player_spawn = (250, 250)
        self.grunt_spawns = None
        self.captain_spawns = None
        self.boss_spawns = None
        self.door_list = None

class Overworld(Map):
    """ Object containing all the data for the overworld map """
    def __init__(self):
        super().__init__()
        self.filename = RESOURCE_PATH + "Maps\\map1.tmj"
        self.player_spawn = (250, 250)
        self.boss_spawns = None
        self.captain_spawns = None
        self.grunt_spawns = None
