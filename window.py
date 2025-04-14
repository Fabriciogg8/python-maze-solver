from line import Line
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")  # Título genérico
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False # Variable para controlar el estado de ejecución
        self.root.protocol("WM_DELETE_WINDOW", self.close)  # Conexión al cerrar

    def redraw(self):
        self.root.update_idletasks()  # ✅ Llama desde root
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
        