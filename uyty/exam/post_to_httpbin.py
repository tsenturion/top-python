import requests

url = "https://httpbin.org/post"
data = {
    "username": "student",
    "exam": "http_test"
}
try:
    response = requests.post(url, json=data)

    print(f"Status code: {response.status_code}\n")
    try:
        json_response = response.json()
        print("Answer:")
        print(json_response)
        print("\n")
        if 'json' in json_response and json_response['json'] == data:
            print("Server received the data")
        else:
            print("server did NOT received the data")
            
    except ValueError:
        print("Error, can't read the JSON")

except requests.exceptions.RequestException as e:
    print(f"ERROR: {e}")