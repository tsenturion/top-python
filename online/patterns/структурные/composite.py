"""
компонент
leaf
composite
client

decorator
bridge
chain of responsibility
"""

class FileSystemComponent:
    def display(self, indent=0):
        raise NotImplementedError

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"File {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children  = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self, indent=0):
        print(' ' * indent + f"Folder {self.name}")
        for child in self.children:
            child.display(indent + 2)

root = Folder("root")
root.add(File("1.txt"))
root.add(File("2.txt"))

sub = Folder("src")
sub.add(File('3.txt'))
sub.add(File('4.txt'))

nested = Folder("tests")
nested.add(File("5.txt"))
nested.add(File("6.txt"))

sub.add(nested)
root.add(sub)

root.display()