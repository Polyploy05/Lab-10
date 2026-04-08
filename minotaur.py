'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/8/2026
Group: 12
Description: Creates the minotaur for use in the maze. Sets itself to a random location in the maze.
When moving, it always knows where the hero is and will move towards the hero if possible. If not, it will move randomly.
'''

import random
import maze

class Minotaur:

    def __init__(self):
        #New maze instance to access the maze and find a random location for the minotaur
        self.new_maze = maze.Maze()
        self.pos = None
        while self.pos is None:
            #Find a location. If empty, place the minotaur there. Else, keep looking.
            i = random.randint(0, len(self.new_maze.maze) - 1)
            j = random.randint(0, len(self.new_maze.maze[0]) - 1)
            if self.new_maze.maze[i][j] == ' ':
                self.pos = [i, j]
                self.new_maze.maze[i][j] = 'M'
    
    def move_minotaur(self):
        '''The move function for the minotaur. It will always know where the hero is and will move towards the hero if possible. If not, it will move randomly.
        It does this by accesing the maze and searching for all possible moves. It then checks if any of those moves are in the direction of the hero. 
        If so, it adds those moves to a list of good moves and picks one. If no good moves exist, it moves randomly.'''    

        #Finds the hero's position as well as all 4 possible moves for the minotaur
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
        #Logs all of these moves as good moves.
        good_moves = []
        if pos_hero[0] < self.pos[0] and pos_up in valid_spaces:
            good_moves.append(pos_up)
        if pos_hero[0] > self.pos[0] and pos_down in valid_spaces:
            good_moves.append(pos_down)
        if pos_hero[1] < self.pos[1] and pos_left in valid_spaces:
            good_moves.append(pos_left)
        if pos_hero[1] > self.pos[1] and pos_right in valid_spaces:
            good_moves.append(pos_right)

        #If no good moves exist, move randomly. Else, move to a random good move.
        if len(good_moves) == 0:
            random_space = random.choice(valid_spaces)
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = random_space
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            print(self.pos)
            return current_obj
        else:
            move = random.choice(good_moves) 
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = move
            current_obj = self.new_maze.maze[self.pos[0]][self.pos[1]]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'M'
            print(self.pos)
            return current_obj
