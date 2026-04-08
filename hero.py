'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/8/2026
Group: 12
Description: Creates & initializes the hero class and creates the functions as to how the Hero moves
'''
import maze

class Hero():
    
    def __init__(self):
        self.maze = Maze()

        #Finding the starting position 's'
        start = self.maze.search_maze('s')
        self.row = start[0]
        self.col = start[1]
        
        #placing the hero
        self.maze[self.row][self.col] = 'H'
        
    
    
    def go_up(self):
        new_row = self.row - 1
        new_col = self.col

        #Find bounds
        if new_row < 0:
            return '*'

        target = self.maze[new_row][new_col]

        if target == '*':
            return '*'
        #Moves Hero
        self.maze[self.row][self.col] = ''
        self.row = new_row
        self.col = new_col
        self.maze[self.row][self.col = 'H'

        return target
    def go_down(self):
        new_row = self.row + 1
        new_col = self.col 

        if new_row >= len(self.maze):
            return '*'

        target = self.maze[new_row][new_col]

        if target == '*'
            return '*'

        self.maze[self.row][self.col] = ''
        self.row = new_row
        self.col = new_col 
        self.maze[self.row][self.col] = 'H'
    def go_left(self):
        new_row = self.row
        new_col = self.col - 1

        if new_col < 0:
            return '*'

        target = self.maze[new_row][new_col]

        if target == '*'
            return '*'

        self.maze[self.row][self.col] = ''
        self.row = new_row
        self.col = new_col
        self.maze[self.row][self.col] = 'H'

        return target
    def go_right(self):
        new_row = self.row
        new_col = self.col + 1

        if new_col >= len(self.maze[new_row]):
            return '*'

        target = self.maze[new_row][new_col]

        if target == '*':
            return '*'

        self.maze[self.row][self.col] = ''
        self.row = new_row
        self.col = new_col
        self.maze[self.row][self.col] = 'H'

        return target
        
