"""
memento
originator - создатель - создатель состояния
memento - снимок
caretaker - опекун - хранитель - менеджер состояний

undo/redo
"""
"""
инкапсуляция
"""
class Memento:
    def __init__(self, text: str, cursor_position: int):
        self._text = text
        self._cursor_position = cursor_position

    def get_saved_state(self):
        return self._text, self._cursor_position

class TextEditor:
    def __init__(self):
        self._text = ''
        self._cursor = 0

    def write(self, text: str):
        self._text = self._text[:self._cursor] + text + self._text[self._cursor:]
        self._cursor += len(text)
        print(f"текст после ввода {self._text}")

    def move_cursor(self, pos: int):
        self._cursor = max(0, min(pos, len(self._text)))

    def save(self) -> Memento:
        print('создание снимка')
        return Memento(self._text, self._cursor)

    def restore(self, memento: Memento):
        self._text, self._cursor = memento.get_saved_state()
        print(f'восстановление состояния {self._text} курсор {self._cursor}')

class History:
    def __init__(self):
        self._states: list[Memento] = []

    def backup(self, memento: Memento):
        self._states.append(memento)
        print('состояние сохранено в историю')

    def undo(self) -> Memento | None:
        if self._states:
            m = self._states.pop()
            print('отмен последнего действия')
            return m
        print('история пуста')
        return None


editor = TextEditor()
history = History()
editor.write('hi')
history.backup(editor.save())

editor.write(', hiiii')
history.backup(editor.save())

editor.write('undone')

m = history.undo()
if m:
    editor.restore(m)

m = history.undo()
if m:
    editor.restore(m)