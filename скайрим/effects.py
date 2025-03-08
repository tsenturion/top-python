import json
from collections import defaultdict

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

effects_dict = defaultdict(list)

for item in data:
    for effect in item['effects']:
        effects_dict[effect].append(item['name'])

effects_data = [{'effect': effect, 'names': ingredients} for effect, ingredients in effects_dict.items()]

with open('effects.json', 'w', encoding='utf-8') as file:
    json.dump(effects_data, file, ensure_ascii=False, indent=4)

print("Файл effects.json успешно создан.")
