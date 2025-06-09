import requests

def google_request():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        
        print(f"Status Code: {response.status_code}\n")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        print("\nFirst 500 characters of HTML:")
        print(response.text[:500])
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    google_request()