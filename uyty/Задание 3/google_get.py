import requests

response = requests.get('https://www.google.com')

print("Статус-код:", response.status_code)
print("Заголовки ответа:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\nПервые 500 символов HTML-контента:")
print(response.text[:500])
