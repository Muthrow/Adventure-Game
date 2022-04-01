""" Main class and Game Runner """
from arcade import run
from game.director import Director

def main():
    Director()
    run()
    #If we do a start screen, we add it before this line

if __name__ == "__main__":
    main()

"""
 TODO: Fix enemy spawn movement
 TODO: Add enemy chase feature
 TODO: Add Boss
 TODO: Line of Sight
 TODO: Border bug on map 1


 David - Boss Map
 Cameron - Pause
 Zack - Boss class
 Jace - Enemy chasing
"""