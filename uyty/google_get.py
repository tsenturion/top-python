import requests

def fetch_google():
    url = 'https://www.google.com'
    try:
        response = requests.get(url)
        
        print("Status Code:", response.status_code)
        print("\nHeaders:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        print("\nFirst 500 characters of HTML:")
        print(response.text[:500])
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    fetch_google()