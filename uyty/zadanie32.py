import requests

url = "https://httpbin.org/post"
data = {
    "username": "student",
    "exam": "http_test"
}

response = requests.post(url, data=data)

print("Статус-код:", response.status_code)

json_response = response.json()
print("\nОтвет в формате JSON:")
print(json_response)

print("\nПодтверждение полученных данных сервером:")
print(json_response.get("form"))
