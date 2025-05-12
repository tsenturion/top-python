"""
Добавьте в сообщение клиента уникальный идентификатор (например, номер пакета).

Пусть сервер записывает, какие пакеты он уже видел, и не отвечает на повторные.

Добавьте на клиенте время отправки и получения, чтобы измерять задержку.

Реализуйте механизм, при котором клиент ждет разные ответы — например, "OK" или "ERROR" в зависимости от содержимого.
"""
import socket
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))
print("Сервер запущен. Ожидание сообщений...")
while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Получено сообщение от {client_address}: {message}")

        ack = "ACK"
        server_socket.sendto(ack.encode(), client_address)
    except Exception as e:
        print(f"Ошибка на сервере: {e}")