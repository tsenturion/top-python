"""
context - контекст - основной
state interface - базовое состояние
concrete states - конкретные состояния

"""


from abc import ABC, abstractmethod

class EditorState(ABC):
    @abstractmethod
    def type_char(self, context, char: str):
        pass

"""class InsertState(EditorState):
    def type_char(self, context, char: str):
        context.text = context.text[:context.cursor] + char + context.text[context.cursor:]
        context.cursor += 1
        print(f'[Insert] {context.text}')
"""
class OverwriteState(EditorState):
    def type_char(self, context, char: str):
        if context.cursor < len(context.text):
            context.text = context.text[:context.cursor] + char + context.text[context.cursor + 1:]
        else:
            context.text += char
        context.cursor += 1
        print(f"[Overwrite] {context.text}")


class TextEditor:
    def __init__(self):
        self.text = ''
        self.cursor = 0
        self._state: EditorState = InsertState()

    def set_state(self, state: EditorState):
        self._state = state

    def type_char(self, char: str):
        self._state.type_char(self, char)

class InsertState(EditorState):
    def type_char(self, context, char: str):
        if char == "#":
            context.set_state(OverwriteState())
            print("переход в OverwriteState")
        else:
            context.text = context.text[:context.cursor] + char + context.text[context.cursor:]
            context.cursor += 1

editor = TextEditor()
editor.type_char("H")
editor.type_char("e")
editor.type_char("l")
editor.type_char("l")
editor.type_char("o")

editor.cursor = 0
editor.set_state(OverwriteState())
editor.type_char("h")
editor.type_char("i")

state = {
    "insert": insert_func,
    "overwrite": overwrite_func
}