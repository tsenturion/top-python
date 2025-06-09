"""
заголовок
содержимое
автор
версия

clone()
"""

import copy

class Document:
    def __init__(self, title, content, author, version=1):
        self.title = title
        self.content = content
        self.author = author
        self.version = version

    def clone(self, new_content=None, new_author=None):
        new_doc = copy.deepcopy(self)
        new_doc.version += 1

        if new_content:
            new_doc.content = new_content
        if new_author:
            new_doc.author = new_author

        return new_doc

    def __str__(self):
        return (
            f"Документ v{self.version}: '{self.title}'\n" +
            f"Автор: {self.author}\n" +
            f"Содержимое: {self.content}\n"
        )
if __name__ == "__main__":
    original_doc = Document("Отчет 2202", "первая версия отчета", "ива иванов")
    print(original_doc)

    updated_doc = original_doc.clone(new_content='обновленная версия отчета')
    print(updated_doc)

    another_doc = updated_doc.clone(new_author="петр петров")
    print(another_doc)
