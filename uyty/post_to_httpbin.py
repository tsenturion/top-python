import requests

data = {"username": "student", "exam": "http_test"}
response = requests.post('https://httpbin.org/post', data=data)

print("Статус-код:", response.status_code)
json_response = response.json()
print("Ответ в формате JSON:")
print(json_response)

print("\nДанные, полученные сервером:")
print(json_response['form'])