import requests
import json


url = 'https://httpbin.org/post'


data = {
    "username": "student",
    "exam": "http_test"
}


response = requests.post(url, json=data)


print(f"Status Code: {response.status_code}")


json_response = response.json()
print("\nJSON Response:")
print(json.dumps(json_response, indent=2))


received_data = json_response.get('json', {})
if received_data == data:
    print("\nData was successfully received by the server!")
else:
    print("\nServer received different data or there was an error.")