from cell import Cell
from point import Point
from line import Line
from window import Window

if __name__ == "__main__":
    win = Window(800, 600)
    win.draw_line(Line(Point(100, 200), Point(400, 300)), "red")
    cell = Cell(100, 200, 100, 200, win)  # Celda de 100x100 píxeles
    cell.has_right_wall = False  # Quitamos la pared derecha
    cell.draw()
    cell2 = Cell(150, 250, 120, 200, win)  # Celda de 100x100 píxeles
    cell2.has_right_wall = False  # Quitamos la pared derecha
    cell2.has_left_wall = False  # Quitamos la pared derecha
    cell2.draw()
    win.wait_for_close()  # Funciona perfectamente.


