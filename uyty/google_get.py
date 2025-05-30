 

url = "https://www.google.com"

try:
    # Отправляем GET-запрос
    response = requests.get(url)
    
    # Выводим статус-код ответа
    print(f"Статус-код ответа: {response.status_code}\n")
    
    # Выводим заголовки ответа
    print("Заголовки ответа:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("\n")
    
    # Выводим первые 500 символов HTML-контента
    print("Первые 500 символов HTML-контента:")
    print(response.text[:500])

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")