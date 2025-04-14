from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None,seed=None):
        """Initializes the maze with the given parameters."""
        self._x1 = x1  # Margen izquierdo del laberinto
        self._y1 = y1  # Margen superior del laberinto
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        """Creates all cells first, then draws them"""
        # Primero creamos todas las celdas
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                column.append(Cell(x1, x2, y1, y2, self._win))
            self._cells.append(column)
        
        # Luego las dibujamos todas
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        """Draws a single cell at position (i,j) and animates the process."""
        if self._win is None:  # No dibujar si no hay ventana
            return   
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        """Animates the drawing process."""
        if self._win is None:  # No animar si no hay ventana
            return           
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        """Breaks the entrance and exit walls of the maze."""
        if self._win is None:
            return
        # Break the entrance (top-left corner)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # Break the exit (bottom-right corner)  
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        """Recursively breaks walls between cells to create the maze."""
        self._cells[i][j].visited = True
        
        while True:
            to_visit = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < self._num_cols and 
                    0 <= nj < self._num_rows and 
                    not self._cells[ni][nj].visited):
                    to_visit.append((ni, nj))
            
            if not to_visit:
                self._draw_cell(i, j)
                return
            
            ni, nj = random.choice(to_visit)
            
            # Asegurarse de romper ambas paredes
            if ni == i + 1:  # Derecha
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            elif ni == i - 1:  # Izquierda
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif nj == j + 1:  # Abajo
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif nj == j - 1:  # Arriba
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            
            # Dibujar los cambios
            self._draw_cell(i, j)
            self._draw_cell(ni, nj)
            
            self._break_walls_r(ni, nj) 

    def _reset_cells_visited(self):
        """Resets the visited status of all cells in the maze."""
        for column in self._cells:
            for cell in column:
                cell.visited = False
    
    def solve(self):
        """Solves the maze using a recursive backtracking algorithm (DFS)."""
        self._reset_cells_visited()
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        """Recursive function to solve the maze."""
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        
        # Si llegamos a la salida
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # Definimos posibles direcciones (izquierda, derecha, arriba, abajo)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            
            # Verificamos si la celda vecina es válida
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                neighbor = self._cells[ni][nj]
                
                # Verificamos si podemos movernos en esta dirección
                if not self._wall_between(current, neighbor, di, dj) and not neighbor.visited:
                    # Dibujamos el movimiento
                    current.draw_move(neighbor)
                    
                    # Llamada recursiva
                    if self._solve_r(ni, nj):
                        return True
                    
                    # Backtracking - dibujamos movimiento de deshacer
                    current.draw_move(neighbor, undo=True)
        
        return False

    def _wall_between(self, current, neighbor, di, dj):
        """Verify if there is a wall between two cells."""
        if di == 1:  # Derecha
            return current.has_right_wall and neighbor.has_left_wall
        elif di == -1:  # Izquierda
            return current.has_left_wall and neighbor.has_right_wall
        elif dj == 1:  # Abajo
            return current.has_bottom_wall and neighbor.has_top_wall
        elif dj == -1:  # Arriba
            return current.has_top_wall and neighbor.has_bottom_wall
        return True  # Por defecto, asumir que hay pared
    

