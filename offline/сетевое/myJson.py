from json import *
test_data_learn = {
    "name": 'alice',
    "age": '23',
}
"""
dumps - сериализация dict в .json
dump - сериализация dict в .json и запись в файл
loads - десериализация .json в dict
load - десериализация .json из файла в dict
"""
test_json_data = dumps(test_data_learn, indent=4, sort_keys=True, ensure_ascii=False)
"""with open('test_json_data.json', 'w', encoding='utf-8') as file:
    dump(test_data_learn, file, indent=4)"""
data = loads(test_json_data)
with open('test_json_data.json', 'r', encoding='utf-8') as file:
    data2 = load(file)
    print(data2)