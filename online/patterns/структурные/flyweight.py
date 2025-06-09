"""
внутреннее состояние
внешнее

+
экономия памяти
производительность
централизация логики

-
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
