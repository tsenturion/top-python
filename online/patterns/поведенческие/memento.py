"""
memento
originator - создатель - создатель состояния
memento - снимок
caretaker - опекун - хранитель - менеджер состояний

undo/redo

преимущества
инкапсуляция
гибкость 
простота отмены изменений

недостатки 
память
сложность

отличие от других паттернов
command сохраняет инструкцию, а мементо хранит состояние объекта
state переключает состояние объекта
prototype клонирует объект
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

    # redo через второй стек, при отмене снимок перемещаетс из стека undo в стек redo и наоборот при повторе

editor = TextEditor()
history = History()
editor.write('hi')
history.backup(editor.save())

editor.write(', hiiii')
history.backup(editor.save())

editor.write('undone')
# нет сохраненных состояний
m = history.undo()
if m:
    editor.restore(m)

m = history.undo()
if m:
    editor.restore(m)

m = history.undo()
if m:
    editor.restore(m)
# нет сохраненных состояний

# безопасность 

class _Memento:
    ...

@property
def _state(self):
    ...


'''
memento
редактор заметок с отменой и повтором
сохранять состояние
с реализацией undo/redo
'''
class Memento:
    def __init__(self, text: str):
        self._text = text

    def get_saved_text(self):
        return self._text

class NoteEditor:
    def __init__(self):
        self._text = ''

    def add_text(self, new_text: str):
        self._text += new_text
        print(f"добавлено {new_text}")

    def save(self) -> Memento:
        return Memento(self._text)

    def show(self):
        print(f"текущая заметка {self._text}")

    def restore(self, memento: Memento):
        self._text = memento.get_saved_text()
        print('состояние восстановлено')

class HistoryManager:
    def __init__(self):
        self._undo_stack: list[Memento] = []
        self._redo_stack: list[Memento] = []

    def backup(self, memento: Memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def undo(self, current_state: Memento) -> Memento | None:
        if not self._undo_stack:
            print('нечего отменять')
            return None
        self._redo_stack.append(current_state)
        return self._undo_stack.pop()

    def redo(self, current_state: Memento) -> Memento | None:
        if not self._redo_stack:
            print('нечего повторять')
            return None
        self._undo_stack.append(current_state)
        return self._redo_stack.pop()

print('--------------------------------------------')
editor = NoteEditor()
history = HistoryManager()

#состояния
history.backup(editor.save())
editor.add_text('1')

history.backup(editor.save())
editor.add_text('2')

history.backup(editor.save())
editor.add_text('3')


#отмена
memento = history.undo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

memento = history.undo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

#повтор
memento = history.redo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

memento = history.redo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

"""
memento
сохранение состояние персонажа Player в игре

хар-ки
level
health
experience
gold

во время игры
повысить уровень
(получить или) потерять здоровье
получить опыт
получить или потерять деньги

user может сохранять и откратываться

Player - Originator
level
health
experience
gold

level_up()
take_damage(amount)
gain_experience(point)
add_gold(amount)
spend_gold(amount)
heal(amount)
save_state() - возвращает объект Memento
restore_state(memento) - восстанавливает состояние из объекта Memento

PlayerMemento - Memento
хранит снимок состояния игрока
не дает изменять состояние игрока

Caretaker
управляет созданием и восстановлением снимков состояния игрока
save(player)
undo(player)
(redo(player))

json
StateStorage
"""
print('--------------------------------------------')
import json
from copy import deepcopy
from collections import deque

class PlayerMemento:
    def __init__(self, state: dict):
        self._state = deepcopy(state)

    def get_state(self):
        return self._state

class Player:
    def __init__(self):
        self.level = 1
        self.health = 100
        self.experience = 0
        self.gold = 0

    def level_up(self):
        self.level += 1
    
    def gain_experience(self, points):
        self.experience += points
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
    
    def heal(self, amount):
        self.health = min(100, self.health + amount)
    
    def add_gold(self, amount):
        self.gold += amount
    
    def spend_gold(self, amount):
        if amount > self.gold:
            raise ValueError('Недостаточно золота')
        self.gold -= amount
    
    def save_state(self):
        return PlayerMemento(self.__dict__)
    
    def restore_state(self, memento: PlayerMemento):
        self.__dict__ = deepcopy(memento.get_state())

    def __str__(self):
        return f"\nуровень: {self.level}\n" \
                f"здоровье: {self.health}\n" \
                f"опыт: {self.experience}\n" \
                f"золото: {self.gold}\n"

class Caretaker:
    def __init__(self, max_history=5):
        self.undo_stack = deque(maxlen=max_history)
        self.redo_stack = deque(maxlen=max_history)

    def save(self, player: Player):
        self.undo_stack.append(player.save_state())
        self.redo_stack.clear()

    def undo(self, player: Player):
        if not self.undo_stack:
            print('нечего отменять')
            return
        
        self.redo_stack.append(player.save_state())
        last_state = self.undo_stack.pop()
        player.restore_state(last_state)
    
    def redo(self, player: Player):
        if not self.redo_stack:
            print('нечего повторять')
            return
        
        self.undo_stack.append(player.save_state())
        next_state = self.redo_stack.pop()
        player.restore_state(next_state)

class StateStorage:
    @staticmethod
    def save_to_file(memento: PlayerMemento, filename='player_state.json'):
        with open(filename, 'w') as f:
            json.dump(memento.get_state(), f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def load_from_file(filename='player_state.json') -> PlayerMemento:
        with open(filename, 'r') as f:
            return PlayerMemento(json.load(f))


player = Player()
caretaker = Caretaker()

print('Initial state:', player)
caretaker.save(player)

player.level_up()
player.gain_experience(150)
caretaker.save(player)

player.take_damage(30)
player.add_gold(100)
caretaker.save(player)

player.take_damage(90)
player.spend_gold(50)
print('Current state before undo:', player)

caretaker.undo(player)
print('Current state after undo 1:', player)

caretaker.undo(player)
print('Current state after undo 2:', player)

caretaker.redo(player)
print('Current state after redo 1:', player)

StateStorage.save_to_file(player.save_state(), 'save.json')
print('Сохранено состояние игрока в файл save.json')

loaded_memento = StateStorage.load_from_file('save.json')
player.restore_state(loaded_memento)
print('Загружено состояние игрока из файла:', player)