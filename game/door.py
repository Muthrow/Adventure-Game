import arcade
import game.constants

class Door(arcade.Sprite):
    """ Represents a Door """
    def __init__(self, door_position, base_map):
        self.current_position = door_position
        self.current_map = base_map
        self.exit_door = None
        self.exit_position = None
        self.exit_map = None
        self.activated = True

    def link(self, outlet):
        """ Links two doors together, allowing for travel between them """
        self.exit_door = outlet
        self.exit_map = outlet.current_map
        self.exit_position = outlet.current_position
        outlet.link(self)
