import requests

def get_google_homepage():
    url = "https://www.google.com"
    try:
        response = requests.get(url)

        print(f"Статус-код ответа: {response.status_code}")
        print("\nЗаголовки ответа:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\nПервые 500 символов HTML-контента:")
        print(response.text[:500])

    except requests.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

if __name__ == '__main__':
    get_google_homepage()
