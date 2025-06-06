import requests

url = "https://www.google.com"
response = requests.get(url)

print("Статус-код:", response.status_code)
print("\nЗаголовки ответа:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\nПервые 500 символов HTML-контента:")
print(response.text[:500])
