
import maze

class Hero():
    
    def __init__(self):
        new_maze = maze.Maze()
        self.pos = new_maze.search_maze('s')
        new_maze[self.pos[0]][self.pos[1]] = 'H'
        
    
    
    def go_up(self):
        pass
    def go_down(self):
        pass
    def go_left(self):
        pass
    def go_right(self):
        pass
        
