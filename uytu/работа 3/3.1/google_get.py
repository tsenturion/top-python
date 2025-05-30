import http.client

def main():
    # Устанавливаем HTTPS-соединение с Google
    conn = http.client.HTTPSConnection("www.google.com", 443)
    conn.request("GET", "/")
    response = conn.getresponse()
    
    # Статус-код ответа
    print(f"Status code: {response.status}")
    print()
    
    # Заголовки ответа
    print("Headers:")
    for header, value in response.getheaders():
        print(f"{header}: {value}")
    print()
    
    # Получаем первые 500 символов тела ответа
    body = response.read().decode(errors="replace")
    print("First 500 chars of HTML content:")
    print(body[:500])
    
    conn.close()

if __name__ == "__main__":
    main()
