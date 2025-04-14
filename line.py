from point import Point

class Line:

    def __init__(self, Point1, Point2):
        self.p1 = Point1
        self.p2 = Point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
    

