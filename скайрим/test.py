import json

# Чтение данных из positive_negative_data.json
with open('positive_negative_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Чтение данных из effects.json
with open('effects.json', 'r', encoding='utf-8') as file:
    effects = json.load(file)

# Формируем множества эффектов
positive_effects_from_data = set(data['positive_effects'])
negative_effects_from_data = set(data['negative_effects'])
all_effects_from_data = positive_effects_from_data | negative_effects_from_data

effects_from_file = {effect['effect'] for effect in effects}

# Проверяем количество эффектов
if len(all_effects_from_data) == len(effects_from_file):
    print("Количество эффектов совпадает.")
else:
    print(f"Разное количество эффектов: {len(all_effects_from_data)} в positive_negative_data.json "
          f"и {len(effects_from_file)} в effects.json.")

# Проверяем, какие эффекты есть в одном файле, но отсутствуют в другом
missing_in_effects_json = all_effects_from_data - effects_from_file
missing_in_data_json = effects_from_file - all_effects_from_data

if missing_in_effects_json:
    print("Эти эффекты есть в positive_negative_data.json, но отсутствуют в effects.json:")
    for effect in missing_in_effects_json:
        print(effect)
else:
    print("Все эффекты из positive_negative_data.json есть в effects.json.")

if missing_in_data_json:
    print("Эти эффекты есть в effects.json, но отсутствуют в positive_negative_data.json:")
    for effect in missing_in_data_json:
        print(effect)
else:
    print("Все эффекты из effects.json есть в positive_negative_data.json.")
