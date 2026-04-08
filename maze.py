'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/8/2026
Group: 12
Description: Creates the maze class. As a singleton, it is only initialized once and all other instances of the maze will reference the same maze. 
It reads the maze from a text file and stores it as a 2D list. Overites str, getitem, and len for easy access and printing. 
Also has a search function to find the location of any character in the maze.
'''

class Maze():
    _instance = None
    _initialized = False

    
    def __new__(cls, *args):
        #Checks if an instance of the maze already exists. If not, creates one. Else, returns the existing instance.
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
        #Prints out the maze without list formatting, 1 row per line
        return '\n'.join(''.join(row) for row in self.maze)
    

    def search_maze(self, char):
        #Searches the maze for a character and returns its position as a list [row, col]. If not found, returns None.
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == char:
                    return [i, j]
        return None


