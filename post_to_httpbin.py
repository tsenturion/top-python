import urllib.request
import json

def main():
    url = "https://httpbin.org/post"
    payload = {
        "username": "student",
        "exam": "http_test"
    }

    # Преобразуем словарь в JSON и кодируем в байты
    data = json.dumps(payload).encode('utf-8')

    # Устанавливаем заголовки запроса
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Создаём объект запроса
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            response_data = response.read().decode('utf-8')
            response_json = json.loads(response_data)

            print(f"Статус-код ответа: {status_code}\n")
            print("Ответ в формате JSON:")
            print(json.dumps(response_json, indent=4, ensure_ascii=False))

            # Подтверждение получения данных сервером
            if response_json.get("json") == payload:
                print("\n✅ Сервер успешно получил отправленные данные.")
            else:
                print("\n⚠️ Сервер не получил ожидаемые данные.")

    except urllib.error.HTTPError as e:
        print(f"HTTP ошибка: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Ошибка URL: {e.reason}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
