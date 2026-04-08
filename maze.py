'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/8/2026
Group: 12
Description: Creates the maze class. Initializes the maze function. 
'''

class Maze():
    _instance = None
    _initialized = False

    
    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super(Maze, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.maze = []
            with open("minomaze.txt", 'r') as f: # put maze file
            #Copies all maze elements into a fresh 2D list
                for line in f:
                    row = list(line.rstrip('\n'))
                    if row:
                        self.maze.append(row)
            self._initialized = True


    def __getitem__(self, row):
        return self.maze[row]
    
    def __len__(self):
        return len(self.maze)


    def __str__(self):
        return '\n'.join(''.join(row) for row in self.maze)
    

    def search_maze(self, char):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == char:
                    return [i, j]
        return None

