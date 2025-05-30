import json

# Загрузка данных из positive_negative_data.json
with open('positive_negative_data.json', 'r', encoding='utf-8') as f:
    positive_negative_data = json.load(f)

# Загрузка данных из data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Список элементов, которые нужно переместить в конец
items_to_move = ["Арония", "Вредозобник", "Гнилая чешуйка", "Смертная плоть", "Человеческое сердце",
                 "Ядовитый колокольчик"]

# Отфильтруем элементы, которые нужно переместить, и оставим остальные
items_moved = [item for item in data if item['name'] in items_to_move]
items_remaining = [item for item in data if item['name'] not in items_to_move]

# Перемещаем элементы в конец
updated_data = items_remaining + items_moved


# Функция для определения состояния эффекта
def get_effect_state(effects, positive_effects, negative_effects):
    has_positive = any(effect in positive_effects for effect in effects)
    has_negative = any(effect in negative_effects for effect in effects)

    if has_positive and has_negative:
        return 0
    elif has_positive:
        return 1
    elif has_negative:
        return -1
    else:
        return 0  # Если эффекты не определены как положительные или отрицательные


# Добавляем поле effect_state в каждый объект
for item in updated_data:
    item['effect_state'] = get_effect_state(item['effects'], positive_negative_data['positive_effects'],
                                            positive_negative_data['negative_effects'])

# Сохраняем обновленный data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=4)

print("Элементы перемещены в конец, и поле effect_state добавлено.")