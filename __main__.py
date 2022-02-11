""" Main class and Game Runner """
from arcade import run
from game.director import Director

def main():
    Director()
    run()
    #If we do a start screen, we add it before this line

if __name__ == "__main__":
    main()