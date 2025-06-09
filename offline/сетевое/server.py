"""
добавьте в сообщение клиента уникальный идентификатор, например номер пакета
сервер записывает, какие пакеты уже видел и не отвечает на повторные

на клиенте
время отправки и получения - измерять задержку
ожидает разные ответы - OK / ERROR в зависимости от содержимого
"""

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
processed_ids = set()
print('запущен и ждет сообщений')

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f'[{client_address}] => {message}')

        message_parts = message.split(':')
        message_id = message_parts[0]
        message_content = message_parts[1] if len(message_parts) > 1 else ''

        if message_id in processed_ids:
            print(f"повторное сообщение с ID {message_id}. игнорируем")
            continue

        processed_ids.add(message_id)

        if 'ERROR' in message_content:
            response = "ERROR"
        else:
            response = "OK"

        server_socket.sendto(response.encode(), client_address)

    except Exception as e:
        print(f"ошибка на сервере {e}")