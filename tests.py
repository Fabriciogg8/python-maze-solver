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
    
    def tearDown(self):
        """Limpieza después de cada test"""
        if hasattr(self, 'win'):
            self.win.close()


if __name__ == "__main__":
    unittest.main()