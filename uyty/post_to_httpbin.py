import requests

def send_post_request():
    url = "https://httpbin.org/post"
    data = {
        "username": "student",
        "exam": "http_test"
    }

    try:
        response = requests.post(url, data=data)

        print(f"Статус-код ответа: {response.status_code}\n")

        json_data = response.json()
        print("Ответ в формате JSON:")
        print(json_data)

        
        print("\nПолученные сервером данные (form):")
        print(json_data.get("form"))

    except requests.RequestException as e:
        print(f"Произошла ошибка при выполнении POST-запроса: {e}")

if __name__ == '__main__':
    send_post_request()
