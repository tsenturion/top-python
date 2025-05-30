import urllib.request
import urllib.error

def main():
    url = 'https://www.google.com'
    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.status
            headers = response.getheaders()
            content = response.read().decode('utf-8', errors='replace')

            print(f"Статус-код ответа: {status_code}\n")
            print("Заголовки ответа:")
            for key, value in headers:
                print(f"{key}: {value}")
            print("\nПервые 500 символов HTML-контента:")
            print(content[:500])
    except urllib.error.HTTPError as e:
        print(f"HTTP ошибка: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Ошибка URL: {e.reason}")

if __name__ == "__main__":
    main()