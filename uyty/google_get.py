from urllib.request import urlopen, Request
from urllib.error import URLError

def fetch_google():
    url = "https://www.google.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    try:
        req = Request(url, headers=headers)
        with urlopen(req) as response:
            
            print(f"Status Code: {response.status}")
            
            
            print("\nHeaders:")
            for header, value in response.getheaders():
                print(f"{header}: {value}")
            
            
            html = response.read().decode('utf-8')
            print("\nFirst 500 characters:")
            print(html[:500])
    
    except URLError as e:
        print(f"Error: {e.reason}")

if __name__ == "__main__":
    fetch_google()