import json


def replace_effects_in_file(file_path, old_effect, new_effect):
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        if 'effects' in item:
            item['effects'] = [new_effect if effect == old_effect else effect for effect in item['effects']]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


"""old_effect = 'Повышение искусства лучника'
new_effect = 'Повышение навыка: стрельба'"""
"""old_effect = 'Повышение навыка: лугкая броня'
new_effect = 'Повышение навыка: легкая броня'"""
old_effect = 'Повышение искусства убеждать'
new_effect = 'Повышение искусства торговли'
replace_effects_in_file('data.json', old_effect, new_effect)
"""replace_effects_in_file('ingredients.json', old_effect, new_effect)
replace_effects_in_file('ingredients2.json', old_effect, new_effect)
replace_effects_in_file('ingredients3.json', old_effect, new_effect)"""
