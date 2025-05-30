import json

# Открываем файл data.json
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Функция для подсчета ключа "name" в каждом объекте
def count_names(data):
    count = 0
    for item in data:
        if "name" in item:
            count += 1
    return count

# Выводим количество
print(count_names(data))
