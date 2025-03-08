import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

data.sort(key=lambda x: x["name"])
for item in data:
    item["effects"].sort()

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные успешно отсортированы и сохранены в effects.json")
