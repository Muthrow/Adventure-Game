from os import path

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Game Title"
RESOURCE_PATH = f"{path.dirname(path.abspath(__file__))}/resources/"    #Might need to be changed
MAP_SCALING = 1.1
PLAYER_SCALE = 1.0
ENEMY_SCALE = PLAYER_SCALE * 0.9
PLAYER_SPEED = 2
PLAYER_UP = ["Player/exec1_up (2).png", "Player/exec1_up (1).png",
 "Player/exec1_up (2).png", "Player/exec1_up (3).png"]
PLAYER_DOWN = ["Player/exec1_down (2).png", "Player/exec1_down (1).png",
 "Player/exec1_down (2).png", "Player/exec1_down (3).png"]
PLAYER_LEFT = ["Player/exec1_left (2).png", "Player/exec1_left (1).png",
 "Player/exec1_left (2).png", "Player/exec1_left (3).png" ]
PLAYER_RIGHT = ["Player/exec1_right (2).png", "Player/exec1_right (1).png",
 "Player/exec1_right (2).png", "Player/exec1_right (3).png"]
PLAYER_ATTACK_UP = ["Player/exec1_attack_up (1).png",
 "Player/exec1_attack_up (2).png", "Player/exec1_attack_up (3).png", "Player/exec1_attack_up (3).png"]
PLAYER_ATTACK_DOWN = ["Player/exec1_attack_down (1).png",
 "Player/exec1_attack_down (2).png", "Player/exec1_attack_down (3).png", "Player/exec1_attack_down (3).png"]
PLAYER_ATTACK_LEFT = ["Player/exec1_attack_left (1).png",
 "Player/exec1_attack_left (2).png", "Player/exec1_attack_left (3).png", "Player/exec1_attack_left (3).png"]
PLAYER_ATTACK_RIGHT = ["Player/exec1_attack_right (1).png",
 "Player/exec1_attack_right (2).png", "Player/exec1_attack_right (3).png", "Player/exec1_attack_right (3).png"]
PLAYER_SPRITES = [PLAYER_DOWN, PLAYER_UP, PLAYER_LEFT, PLAYER_RIGHT,  PLAYER_ATTACK_DOWN, PLAYER_ATTACK_UP, PLAYER_ATTACK_LEFT, PLAYER_ATTACK_RIGHT]
ENEMY_DOWN = ["Beast Hero/beast_hero_down (1).png", "Beast Hero/beast_hero_down (1).png", 
"Beast Hero/beast_hero_down (2).png", "Beast Hero/beast_hero_down (3).png"]
ENEMY_UP = ["Beast Hero/beast_hero_up (2).png", "Beast Hero/beast_hero_up (1).png", 
"Beast Hero/beast_hero_up (2).png", "Beast Hero/beast_hero_up (3).png"]
ENEMY_LEFT = ["Beast Hero/beast_hero_left (2).png", "Beast Hero/beast_hero_left (1).png",
 "Beast Hero/beast_hero_left (2).png", "Beast Hero/beast_hero_left (3).png"]
ENEMY_RIGHT = ["Beast Hero/beast_hero_right (2).png", "Beast Hero/beast_hero_right (1).png", 
"Beast Hero/beast_hero_right (2).png", "Beast Hero/beast_hero_right (3).png"]
ENEMY_SPRITES = [ENEMY_DOWN, ENEMY_UP, ENEMY_LEFT, ENEMY_RIGHT]
BOSS_SPRITES = ["Beholder Boss/beholder_down 1.png", "Beholder Boss/beholder_up 1.png", 
"Beholder Boss/beholder_left 1/.png", "Beholder Boss/beholder_right 1.png"]
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