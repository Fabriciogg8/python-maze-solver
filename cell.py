from line import Line
from point import Point

class Cell:

    def __init__(self, x1, x2, y1, y2,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.visited = False
        self._win = win
    
    def draw(self):
        """Draws the cell walls, drawing white lines where walls are missing"""
        if self._win is None:
            return
    
         # Draw walls or white lines where walls are missing
        walls = [(self.has_left_wall, Line(Point(self._x1, self._y1), Point(self._x1, self._y2))),
            (self.has_right_wall, Line(Point(self._x2, self._y1), Point(self._x2, self._y2))),
            (self.has_top_wall, Line(Point(self._x1, self._y1), Point(self._x2, self._y1))),
            (self.has_bottom_wall, Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        ]
        

        for has_wall, line in walls:
            color = "black" if has_wall else "white"
            self._win.draw_line(line, color)
    
    def draw_move(self, to_cell, undo=False):
        """Draws the movement between the centers of two cells."""
        color = "red" if not undo else "gray"
    
        # Calcula los puntos centrales de ambas celdas
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
    
        # Dibuja la línea entre los puntos centrales
        self._win.draw_line(Line(self_center, to_cell_center), color)   

    
