from os import path

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Game Title"
RESOURCE_PATH = f"{path.dirname(path.abspath(__file__))}/resources/"    #Might need to be changed
MAP_SCALING = .55
PLAYER_SCALE = .8
PLAYER_SPEED = 1
PLAYER_UP = ["Player/exec1_up (2).png", "Player/exec1_up (1).png",
 "Player/exec1_up (2).png", "Player/exec1_up (3).png"]
PLAYER_DOWN = ["Player/exec1_down (2).png", "Player/exec1_down (1).png",
 "Player/exec1_down (2).png", "Player/exec1_down (3).png"]
PLAYER_LEFT = ["Player/exec1_left (2).png", "Player/exec1_left (1).png",
 "Player/exec1_left (2).png", "Player/exec1_left (3).png" ]
PLAYER_RIGHT = ["Player/exec1_right (2).png", "Player/exec1_right (1).png",
 "Player/exec1_right (2).png", "Player/exec1_right (3).png"]
PLAYER_SPRITES = [PLAYER_DOWN, PLAYER_UP, PLAYER_LEFT, PLAYER_RIGHT]
ENEMY_SCALE = PLAYER_SCALE/2
LAYER_OPTIONS = {
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