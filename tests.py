import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def setUp(self):
        # Configuración común para los tests que necesitan ventana
        self.win = Window(800, 600)

    def test_maze_create_cells_no_window(self):
        """Test creación de celdas sin ventana"""
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_with_window(self):
        """Test creación de celdas con ventana"""
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_dimensions_small(self):
        """Test con dimensiones pequeñas"""
        m1 = Maze(50, 50, 1, 1, 100, 100, self.win)
        self.assertEqual(len(m1._cells), 1)
        self.assertEqual(len(m1._cells[0]), 1)
    
    def test_maze_dimensions_large(self):
        """Test con dimensiones grandes"""
        m1 = Maze(10, 10, 20, 30, 15, 15, self.win)
        self.assertEqual(len(m1._cells), 30)
        self.assertEqual(len(m1._cells[0]), 20)
    
    def test_maze_cell_positions(self):
        """Verifica posiciones correctas de las celdas"""
        m1 = Maze(100, 100, 2, 2, 50, 50, self.win)
        
        # Verificar posición de la celda (0,0)
        cell_00 = m1._cells[0][0]
        self.assertEqual(cell_00._x1, 100)
        self.assertEqual(cell_00._y1, 100)
        self.assertEqual(cell_00._x2, 150)
        self.assertEqual(cell_00._y2, 150)
        
        # Verificar posición de la celda (1,1)
        cell_11 = m1._cells[1][1]
        self.assertEqual(cell_11._x1, 150)
        self.assertEqual(cell_11._y1, 150)
        self.assertEqual(cell_11._x2, 200)
        self.assertEqual(cell_11._y2, 200)

    def test_break_entrance_and_exit_single_cell(self):
        """Test with a 1x1 maze"""
        m1 = Maze(0, 0, 1, 1, 10, 10, self.win)
        m1._break_entrance_and_exit()
        
        # En un laberinto 1x1, la misma celda es entrada y salida
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[0][0].has_bottom_wall)
        
    def tearDown(self):
        """Limpieza después de cada test"""
        if hasattr(self, 'win'):
            self.win.close()

    def test_maze_generation(self):
        """Test de generación del laberinto con seed fija"""
        m1 = Maze(0, 0, 5, 5, 10, 10, seed=42)
        
        # Verificar que todas las celdas fueron visitadas durante la generación
        for column in m1._cells:
            for cell in column:
                # Después de _reset_cells_visited, todas deben estar no visitadas
                self.assertFalse(cell.visited)
        
        # Verificar que algunas paredes fueron rotas
        walls_broken = False
        for column in m1._cells:
            for cell in column:
                if not cell.has_left_wall or not cell.has_right_wall or \
                not cell.has_top_wall or not cell.has_bottom_wall:
                    walls_broken = True
                    break
        self.assertTrue(walls_broken)

    def test_maze_reproducibility(self):
        """Test que verifica que con la misma seed se genera el mismo laberinto"""
        m1 = Maze(0, 0, 5, 5, 10, 10, seed=123)
        m2 = Maze(0, 0, 5, 5, 10, 10, seed=123)
        
        # Comparar todas las paredes de todas las celdas
        for i in range(5):
            for j in range(5):
                cell1 = m1._cells[i][j]
                cell2 = m2._cells[i][j]
                self.assertEqual(cell1.has_left_wall, cell2.has_left_wall)
                self.assertEqual(cell1.has_right_wall, cell2.has_right_wall)
                self.assertEqual(cell1.has_top_wall, cell2.has_top_wall)
                self.assertEqual(cell1.has_bottom_wall, cell2.has_bottom_wall)
                
    def test_reset_cells_visited(self):
        """Test to ensure _reset_cells_visited resets all cells' visited status."""
        # Crea un laberinto pequeño para la prueba
        maze = Maze(0, 0, 3, 3, 10, 10)

        # Simula celdas visitadas
        for column in maze._cells:
            for cell in column:
                cell.visited = True

        # Llama al método _reset_cells_visited
        maze._reset_cells_visited()

        # Verifica que todas las celdas tengan visited=False
        for column in maze._cells:
            for cell in column:
                assert not cell.visited, "El estado 'visited' no se restableció correctamente." 
    
    def test_solve_maze(self):
        # Laberinto simple 2x2 sin paredes internas
        m = Maze(0, 0, 2, 2, 10, 10, self.win)
        
        # Quitar todas las paredes internas
        m._cells[0][0].has_right_wall = False
        m._cells[1][0].has_left_wall = False
        m._cells[0][0].has_bottom_wall = False
        m._cells[0][1].has_top_wall = False
        
        self.assertTrue(m.solve())

    def test_unsolvable_maze(self):
        # Laberinto 2x2 completamente cerrado
        m = Maze(0, 0, 2, 2, 10, 10, self.win)
        
        # Forzar que todas las paredes internas existan
        m._cells[0][0].has_right_wall = True
        m._cells[1][0].has_left_wall = True
        m._cells[0][0].has_bottom_wall = True
        m._cells[0][1].has_top_wall = True
        m._cells[1][0].has_bottom_wall = True
        m._cells[1][1].has_top_wall = True
        m._cells[0][1].has_right_wall = True
        m._cells[1][1].has_left_wall = True
        
        # Resetear el estado de visitadas por si acaso
        m._reset_cells_visited()
        
        self.assertFalse(m.solve())

if __name__ == "__main__":
    unittest.main()