import http.client
import json

def main():
    host = "httpbin.org"
    url = "/post"
    data = {"username": "student", "exam": "http_test"}
    headers = {"Content-Type": "application/json"}

    # Преобразуем словарь в строку JSON
    json_data = json.dumps(data)

    # Устанавливаем HTTPS-соединение
    conn = http.client.HTTPSConnection(host, 443)
    conn.request("POST", url, body=json_data, headers=headers)
    response = conn.getresponse()

    # Статус-код ответа
    print(f"Status code: {response.status}")

    # Получаем и декодируем ответ
    resp_data = response.read().decode()
    try:
        resp_json = json.loads(resp_data)
    except json.JSONDecodeError:
        resp_json = None

    # Ответ в формате JSON (красиво)
    print("\nJSON response:")
    print(json.dumps(resp_json, indent=2, ensure_ascii=False))

    # Подтверждение, что сервер получил отправленные данные
    if resp_json and "json" in resp_json and resp_json["json"] == data:
        print("\nДанные успешно получены сервером!")
    else:
        print("\nОшибка: отправленные данные не были получены сервером!")

    conn.close()

if __name__ == "__main__":
    main()
