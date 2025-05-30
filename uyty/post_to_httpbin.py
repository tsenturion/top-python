import requests

# URL для POST-запроса
url = 'https://httpbin.org/post'

# Произвольные данные для отправки
data = {
    "username": "student",
    "exam": "http_test"
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Вывод статус-кода ответа
print("Статус-код ответа:", response.status_code)

# Вывод ответа в формате JSON
print("\nОтвет в формате JSON:")
print(response.json())

# Подтверждение, что данные были получены сервером
if response.status_code == 200:
    response_data = response.json()
    received_data = response_data.get('json', {})
    if received_data == data:
        print("\nПодтверждение: сервер успешно получил данные")
    else:
        print("\nДанные на сервере не соответствуют отправленным")
else:
    print("\nОшибка при отправке данных на сервер")