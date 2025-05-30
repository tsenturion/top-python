import requests
import json

data = {"username": "student", "exam": "http_test"}

response = requests.post("https://httpbin.org/post", data=data)

print("Статус-код:", response.status_code)

json_response = response.json()
print("Ответ JSON от сервера:")
print(json.dumps(json_response, indent=4))
