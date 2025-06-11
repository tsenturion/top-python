"""
термины:
intrinsic state внутреннее состояние
extrinsic state внешнее

используем когда: 
много мелких объектов
одинаковые свойства
память ценна
можем разделить общие данных и уникальные

+
экономия памяти
производительность
централизация логики

-
сложнее струтура 
нужно строго контролировать, что можно шарить
может понадобиться менеджер объектов (фабрика)
"""
# внутреннее состояние
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"рисуем {self.name} ({self.color}, {self.texture}) на ({x}, {y})")

# фабрика приспособленцев
class TreeFactory:
    _types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color, texture)
            print(f"создан тип дерева {name}")
        return cls._types[key]

# внешнее состояние
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.type = tree_type

    def draw(self):
        self.type.draw(self.x, self.y)

# контекст
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()

forest = Forest()
forest.plant_tree(10, 20, "дуб", 'зеленый', "гладкий")
forest.plant_tree(20, 20, "дуб2", 'зеленый', "гладкий")
forest.plant_tree(220, 20, "дуб2", 'зеленый', "гладкий")
forest.plant_tree(210, 20, "дуб2", 'зеленый', "гладкий")
forest.plant_tree(250, 20, "дуб2", 'зеленый', "гладкий")
forest.plant_tree(30, 20, "дуб", 'зеленый', "гладкий")

forest.draw()


"""
flyweight

фигуры - много на холсте - внутреннее состояние
круги
квадраты
треугольники

тип фигуры - фигуры
цвет
координаты на холсте x y - внешнее состояние

ShapeType - тип фигуры и цвет
ShapeFactory - создает и кеширует ShapeType
Shape - одна фигура: координаты и ссылка на ShapeType
Canvas - контейнер, все Shape. draw_all()
"""

class ShapeType:
    def __init__(self, shape_name: str, color: str):
        self.shape_name = shape_name
        self.color = color

    def draw(self, x, y):
        print(f"рисуем {self.shape_name.upper()} ({self.color}) на ({x} {y})")

class ShapeFactory:
    _types = {}

    @classmethod
    def get_shape_type(cls, shape_name, color):
        key = (shape_name, color)
        if key not in cls._types:
            cls._types[key] = ShapeType(shape_name, color)
            print(f"[Factory] новый тип {shape_name} {color}")
        return cls._types[key]

class Shape:
    def __init__(self, x, y, shape_type: ShapeType):
        self.x = x
        self.y = y
        self.shape_type = shape_type

    def draw(self):
        self.shape_type.draw(self.x, self.y)

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, x, y, shape_name, color):
        shape_type = ShapeFactory.get_shape_type(shape_name, color)
        shape = Shape(x, y, shape_type)
        self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            shape.draw()

canvas = Canvas()

canvas.add_shape(10, 20, "circle", 'red')
canvas.add_shape(10, 20, "circle", 'red')
canvas.add_shape(10, 20, "circle2", 'red')
canvas.add_shape(10, 20, "circle2", 'red')
canvas.add_shape(10, 20, "circle2", 'red')

canvas.draw_all()

"""
система отображения стикеров в мессенджере

10 стикеров:
отправитель
получатель
метка времени
графика

внутреннее состояние: изображение, имя
внешнее состояние: кто отправлял, кому, когда

StickerType внутр
StickerFactory хранит и переиспользует StickerType
StickerMessage содержит ссылку на StickerType внеш

"""