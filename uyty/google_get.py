import http.client
import ssl

def fetch_google_homepage():
    # Создаем SSL-контекст
    context = ssl.create_default_context()

    # Устанавливаем HTTPS-соединение
    conn = http.client.HTTPSConnection("www.google.com", context=context)
    
    # Отправляем GET-запрос
    conn.request("GET", "/")

    # Получаем ответ
    response = conn.getresponse()
    
    # Читаем тело ответа
    body = response.read().decode('utf-8', errors='replace')

    # Выводим информацию
    print("Статус-код:", response.status)
    print("\nЗаголовки:")
    for header, value in response.getheaders():
        print(f"{header}: {value}")

    print("\nПервые 500 символов HTML-контента:")
    print(body[:500])

    conn.close()

if __name__ == '__main__':
    fetch_google_homepage()
