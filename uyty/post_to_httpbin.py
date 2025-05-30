import requests
import json

def post_data():
    url = 'https://httpbin.org/post'
    data = {
        "username": "student",
        "exam": "http_test",
        "result": "excellent"
    }
    
    try:
        response = requests.post(url, json=data)
        
        print("Status Code:", response.status_code)
        
        json_response = response.json()
        print("\nJSON Response:")
        print(json.dumps(json_response, indent=2))
        
        if json_response.get('json') == data:
            print("\nServer successfully received our data!")
        else:
            print("\nData was not properly received by server.")
            
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    post_data()