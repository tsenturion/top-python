from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json

def send_post_request():
    url = "https://httpbin.org/post"
    data = {
        "username": "student",
        "exam": "http_test"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Python-urllib'
    }
    
    try:
        encoded_data = urlencode(data).encode('utf-8')
        req = Request(url, data=encoded_data, headers=headers, method='POST')
        
        with urlopen(req) as response:
            
            print(f"Status Code: {response.status}")
            
           
            result = json.loads(response.read().decode('utf-8'))
            print("\nResponse JSON:")
            print(json.dumps(result, indent=2))
            
            
            if result.get('json') == data:
                print("\nData was successfully received by the server!")
            else:
                print("\nOriginal data:", data)
                print("Received data:", result.get('json'))
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_post_request()