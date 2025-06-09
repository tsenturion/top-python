"""
proxy
суррогат или заместитель

subject - общий интерфейс
realSubject - реальный объект
proxy - заместитель

decorator
"""

class Image:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"[Image] загрузка {self.filename}")

    def display(self):
        print(f"[Image] отображение {self.filename}")

class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = Image(self.filename)
        self._real_image.display()

img = ImageProxy("1.jpg")
print('объект создан без загрузки')
img.display()

class Document:
    def delete(self):
        print('док удален')

class SecureDocumentProxy:
    def __init__(self, real_doc, user_role):
        self._real_doc = real_doc
        self._user_role = user_role

    def delete(self):
        if self._user_role != 'admin':
            print('запрещено')
        else:
            self._real_doc.delete()


doc = Document()
proxy = SecureDocumentProxy(doc, 'guest')
proxy.delete()

