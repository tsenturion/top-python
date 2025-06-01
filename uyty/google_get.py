import requests

url = "https://www.google.com"

try:
    response = requests.get(url)

    # Статус-код ответа
    print(f"Статус-код ответа: {response.status_code}")

    # Заголовки ответа
    print("Заголовки ответа:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Первые 500 символов HTML-контента (без парсинга)
    print("\nПервые 500 символов HTML-контента:")
    print(response.text[:500])

except Exception as e:
    print(f"Ошибка: {e}")
