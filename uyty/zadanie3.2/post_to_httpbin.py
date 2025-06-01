import requests

url = "https://httpbin.org/post"
data = {"username": "student", "exam": "http_test"}

try:
    response = requests.post(url, json=data)
    print(f"Статус-код ответа: {response.status_code}")

    # Ответ в формате JSON
    print("Ответ сервера в формате JSON:")
    print(response.json())

    # Проверка, что сервер получил наши данные
    if response.json().get("json") == data:
        print("Сервер получил отправленные данные!")
    else:
        print("Данные не совпадают или сервер не вернул их как ожидалось.")

except Exception as e:
    print(f"Ошибка: {e}")
