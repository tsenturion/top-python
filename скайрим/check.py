import json

with open('data.json', 'r', encoding='utf-8') as f_data:
    data = json.load(f_data)

with open('question.json', 'r', encoding='utf-8') as fq:
    question_data = json.load(fq)

excluded_names = set(question_data.keys())

invalid_ingredients = [
    ingredient['name'] for ingredient in data if 'effects' not in ingredient or len(ingredient['effects']) != 4
]

if invalid_ingredients:
    print("Следующие ингредиенты НЕ содержат ровно 4 эффекта:", invalid_ingredients)
else:
    print("Все ингредиенты содержат ровно 4 эффекта.")

seen = {}
duplicates = set()

unique_ingredients = []
for ingredient in data:
    key = (ingredient['name'], frozenset(ingredient['effects']))
    if key[0] in seen:
        if seen[key[0]] == key[1]:
            duplicates.add(ingredient['name'])
    else:
        seen[key[0]] = key[1]
        unique_ingredients.append(ingredient)

if duplicates:
    print("Найдены дубликаты:", duplicates)
else:
    print("Дубликаты не найдены.")

all_ingredients = []

with open('ingredients.json', 'r', encoding='utf-8') as f1, \
        open('ingredients2.json', 'r', encoding='utf-8') as f2, \
        open('ingredients3.json', 'r', encoding='utf-8') as f3:
    ingredients1 = json.load(f1)
    ingredients2 = json.load(f2)
    ingredients3 = json.load(f3)

    all_ingredients = ingredients1 + ingredients2 + ingredients3

all_names = {ingredient['name'] for ingredient in all_ingredients if ingredient['name'] not in excluded_names}

data_names = {ingredient['name'] for ingredient in data}

missing_names = all_names - data_names

if missing_names:
    print("Отсутствуют следующие имена в data.json:", missing_names)
else:
    print("Все имена из всех трех файлов (без учета question.json) присутствуют в data.json.")
