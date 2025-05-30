import requests

responce = requests.get("https://www.google.com.")

if responce.status_code == 200:
    print(responce.status_code)
    for header, value in responce.headers.items():
        print(f"{header}: {value}")
    print(responce.text[:500])
else:
    print("Error: ", responce.status_code)