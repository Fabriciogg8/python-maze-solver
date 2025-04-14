# Maze Solver - Generador y Solucionador de Laberintos

## 📌 Descripción del Proyecto

Implementación de un generador y solucionador de laberintos utilizando:
- **Python** + **Tkinter** para la interfaz gráfica
- **DFS (Depth-First Search)** para generación y solución
- **Programación Orientada a Objetos** con clases bien definidas

## 🏗️ Estructura del Código

```markdown
maze_solver/
├── main.py            # Punto de entrada principal
├── maze.py            # Lógica principal del laberinto
├── cell.py            # Implementación de celdas individuales
├── window.py          # Manejo de la ventana gráfica
├── point.py           # Representación de coordenadas
├── line.py            # Dibujo de líneas/paredes
└── tests.py           # Pruebas unitarias
```

## 🚀 Cómo Ejecutar

1. **Requisitos**:
   ```bash
   Python 3.8+
   tkinter (normalmente incluido)
   ```

2. **Ejecución**:
   ```bash
   python main.py
   ```

3. **Configuración** (en `main.py`):
   ```python
   win = Window(800, 600)
   maze = Maze(
       x1=50, y1=50,            # Margenes
       num_rows=10, num_cols=10, # Tamaño
       cell_size_x=40,           # Ancho de celda
       cell_size_y=40,           # Alto de celda
       win=win,                  # Ventana
       seed=42                   # Opcional (para reproducibilidad)
   )
   maze.solve()  # Resolver automáticamente
   ```

## 🧩 Componentes Clave

### `Cell` (cell.py)
```python
class Cell:
    def __init__(self, x1, x2, y1, y2, win=None):
        # Paredes (inicialmente todas existen)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # Coordenadas y estado
        self._x1, self._x2 = x1, x2
        self._y1, self._y2 = y1, y2
        self.visited = False
```

### `Maze` (maze.py)
Principales métodos:
- `_create_cells()`: Genera la estructura de celdas
- `_break_walls_r()`: Rompe paredes para crear el laberinto
- `solve()`: Implementa DFS para resolverlo
- `_animate()`: Visualización paso a paso

## 🔍 Algoritmos Implementados

### Generación del Laberinto
1. **DFS Recursivo** con selección aleatoria de direcciones
2. Eliminación sistemática de paredes
3. Entrada/Salida automática (esquinas opuestas)

### Solución
1. **DFS con Backtracking**
2. Visualización:
   - 🟥 Rojo: Camino hacia adelante
   - ⬜ Gris: Retroceso (backtracking)

## 🧪 Pruebas Unitarias

Ejecutar tests:
```bash
python tests.py
```

Pruebas incluyen:
- Creación correcta de celdas
- Generación reproducible con seed
- Solución de laberintos simples
- Casos imposibles

## 🛠️ Posibles Mejoras

1. Más algoritmos de generación:
   ```python
   - Prim's Algorithm
   - Kruskal's Algorithm
   ```

2. Nuevos métodos de solución:
   ```python
   - BFS (Breadth-First Search)
   - A* (A-star)
   ```

3. Interacción de usuario:
   ```python
   - Resolución manual
   - Personalización de laberintos
   ```

## 📜 Licencia
MIT License - Libre uso y modificación

---