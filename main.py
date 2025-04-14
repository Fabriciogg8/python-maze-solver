from cell import Cell
from point import Point
from line import Line
from window import Window
from maze import Maze

if __name__ == "__main__":
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 40, 40, win)
    
    if maze.solve():
        print("¡Laberinto resuelto!")
    else:
        print("No se encontró solución")
    
    win.wait_for_close()
    
    


