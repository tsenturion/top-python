import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-16') as f:
        return json.load(f)



def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def remove_ingredients(data, ingredients_to_remove):
    return [item for item in data if item['name'] not in ingredients_to_remove]


ingredients_to_remove = {
    "Измельченная соль пустоты",
    "Корень жарницы",
    "Морозная соль Фаренгара",
    "Прах Берита"
}

files = ['ingredients.json', 'ingredients2.json', 'ingredients3.json']

for file in files:
    data = load_json(file)
    filtered_data = remove_ingredients(data, ingredients_to_remove)
    save_json(file, filtered_data)

    found = {item['name'] for item in data if item['name'] in ingredients_to_remove}
    print(f"Удаленные ингредиенты из {file} :", found)
