"""
Добавьте в сообщение клиента уникальный идентификатор (например, номер пакета).

Пусть сервер записывает, какие пакеты он уже видел, и не отвечает на повторные.

Добавьте на клиенте время отправки и получения, чтобы измерять задержку.

Реализуйте механизм, при котором клиент ждет разные ответы — например, "OK" или "ERROR" в зависимости от содержимого.
"""
import socket
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))
processed_ids = set()
print("Сервер запущен. Ожидание сообщений...")
while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Получено сообщение от {client_address}: {message}")

        message_parts = message.split(":")
        message_id = message_parts[0]
        message_content = message_parts[1] if len(message_parts) > 1 else ""

        if message_id in processed_ids:
            print(f"получено повторное сообщение с идентификатором {message_id}. Пропускаем...")
            continue
        
        processed_ids.add(message_id)

        if "ERROR" in message_content:
            response = "ERROR"
        else:
            response = "OK"
        
        server_socket.sendto(response.encode(), client_address)
        
    except Exception as e:
        print(f"Ошибка на сервере: {e}")