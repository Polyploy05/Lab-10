'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/8/2026
Group: 12
Description: Creates & initializes the hero class and creates the functions as to how the Hero moves
'''
import maze

class Hero():
    
    def __init__(self):
        self.new_maze = maze.Maze()

        #Finding the starting position 's'
        start = self.new_maze.search_maze('s')
        self.pos = start
        
        #placing the hero
        self.new_maze.maze[self.pos[0]][self.pos[1]] = 'H'
        
    
    
    def go_up(self):
        #Hero moves up
        new_row = self.pos[0] - 1
        new_col = self.pos[1] 

        current_obj = self.new_maze[new_row][new_col]
        if current_obj == '*':
            return '*'
        else:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = [new_row, new_col]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'H'
            return current_obj

    
    def go_down(self):
        #Hero goes down
        new_row = self.pos[0] + 1
        new_col = self.pos[1] 

        current_obj = self.new_maze[new_row][new_col]
        if current_obj == '*':
            return '*'
        else:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = [new_row, new_col]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'H'
            return current_obj

    def go_left(self):
        #Hero goes left
        new_row = self.pos[0] 
        new_col = self.pos[1] - 1

        current_obj = self.new_maze[new_row][new_col]
        if current_obj == '*':
            return '*'
        else:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = [new_row, new_col]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'H'
            return current_obj
    
    
    def go_right(self):
        #Hero goes right

        new_row = self.pos[0]
        new_col = self.pos[1] + 1

        current_obj = self.new_maze[new_row][new_col]
        if current_obj == '*':
            return '*'
        else:
            self.new_maze.maze[self.pos[0]][self.pos[1]] = ' '
            self.pos = [new_row, new_col]
            self.new_maze.maze[self.pos[0]][self.pos[1]] = 'H'
            return current_obj
