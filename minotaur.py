

import random
import maze

class Minotaur:

    def __init__(self):
        self.pos = None
        while self.pos is None:
            i = random.randint(0, len(maze.Maze().maze) - 1)
            j = random.randint(0, len(maze.Maze().maze[0]) - 1)
            if maze.Maze().maze[i][j] == ' ':
                self.pos = [i, j]
                maze.Maze().maze[i][j] = 'M'
                print(self.pos)
    