

import maze
import minotaur
import hero

def main():
    #Objects creation
    maze = maze.Maze()
    minotaur = minotaur.Minotaur()
    hero = hero.Hero()

    #Game Loop
    while True:
        #Displays the Maze
        print(maze)

        #User input
        move = input("Move (w/a/s/d):).lower()

        #Move Hero
        if move == 'w':
            result = hero.go_up()
        elif move == 's':
            result = hero.go_down()
        elif move == 'a':
            result = hero.go_left()
        elif move == 'd':
            result = hero.go_right()
        else:
            print("Invalid input.")
            continue

        #Check result after hero move
        if result == 'f':
            print(maze)
            print("You escaped the maze! You win!")
            break
        elif result == 'M':
            print(maze)
            print("The Minotaur got you! You lost!")
            break

        #Minotaur Moves AFTER valid hero move
        result = minotaur.move_minotaur()

        #Check result after minotaur move
        if result =='H':
            print(maze)
            print("The Minotaur caught you! You lost!")
            break
            
if __name__ == "__main__":
    main()
