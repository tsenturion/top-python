"""
абстракция
расширенная абстракция
интерфейс реализации
конкретные реализации

adapter
decorator
strategy
absract factory
"""
class DrawingApi:
    def draw_circle(self, x: int, y: int, radius: int):
        raise NotImplemented

class OpenGLAPI(DrawingApi):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f"[OpenGl] {x, y, radius}")

class DirectXAPI(DrawingApi):
    def draw_circle(self, x: int, y: int, radius: int):
        print(f"[DirectX] {x, y, radius}")

class Shape:
    def __init__(self, drawing_api: DrawingApi):
        self.drawing_api = drawing_api

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, drawing_api: DrawingApi):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

circle1 = Circle(10, 20, 5, OpenGLAPI())
circle2 = Circle(100, 200, 50, DirectXAPI())

circle1.draw()
circle2.draw()
