

import maze
import minotaur
import hero

def main():
    new_maze = maze.Maze()
    min = minotaur.Minotaur()
    her = hero.Hero()


    print(new_maze)

    print(new_maze.search_maze('s'))

if __name__ == "__main__":
    main()