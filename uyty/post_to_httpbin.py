import http.client
import json
import ssl

def send_post_request():
    # Данные для отправки
    data = {
        "username": "student",
        "exam": "http_test"
    }
    json_data = json.dumps(data)

    # Настройка HTTPS-соединения
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection("httpbin.org", context=context)

    headers = {
        "Content-Type": "application/json"
    }

    # Отправка POST-запроса
    conn.request("POST", "/post", body=json_data, headers=headers)

    # Получение ответа
    response = conn.getresponse()
    response_data = response.read().decode()

    # Вывод результатов
    print("Статус-код:", response.status)

    try:
        response_json = json.loads(response_data)
        print("\nJSON-ответ:")
        print(json.dumps(response_json, indent=4))

        print("\nПодтверждение данных от сервера:")
        print(response_json.get("json"))

    except json.JSONDecodeError:
        print("\nОшибка при разборе JSON.")
        print(response_data)

    conn.close()

if __name__ == '__main__':
    send_post_request()
