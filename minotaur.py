

import random
import maze

class Minotaur:

    def __init__(self):
        self.new_maze = maze.Maze()
        self.pos = None
        while self.pos is None:
            i = random.randint(0, len(maze.Maze().maze) - 1)
            j = random.randint(0, len(maze.Maze().maze[0]) - 1)
            if maze.Maze().maze[i][j] == ' ':
                self.pos = [i, j]
                maze.Maze().maze[i][j] = 'M'
                print(self.pos)
    
    def move(self):

        #Finds the hero's position as well as all 4 possibel moves for the minotaur
        pos_hero = self.new_maze.search_maze('H')
        pos_left = [self.pos[0], self.pos[1] - 1]
        pos_right = [self.pos[0], self.pos[1] + 1]
        pos_up = [self.pos[0] - 1, self.pos[1]]
        pos_down = [self.pos[0] + 1, self.pos[1]]
        spaces = [pos_left, pos_right, pos_up, pos_down]
        valid_spaces = []
        #Check for walls. If none, add to valid
        for space in spaces:
            if self.new_maze.maze[space[0]][space[1]] != "*":
                valid_spaces.append(space)
        
        #Move logic. The minotaur will detect if the hero is above, below, or to the side of the hero.
        #It attempts to move in the direction of the hero, so long as it is a valid move.
        if pos_hero[0] < self.pos[0] and pos_up in valid_spaces:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = pos_up
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            return current_obj
        elif pos_hero[0] > self.pos[0] and pos_down in valid_spaces:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = pos_down
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            return current_obj
        elif pos_hero[1] < self.pos[1] and pos_left in valid_spaces:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = pos_left
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            return current_obj
        elif pos_hero[1] > self.pos[1] and pos_right in valid_spaces:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = pos_right
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            return current_obj
        #If unable to move directly towards the hero, move randomly.
        else:
            random_space = random.choice(valid_spaces)
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = random_space
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            return current_obj
