import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.settimeout(3)

server_address = ("localhost", 12345)
message = 'Hello, server!'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    try:
        print(f"Попытка {attempt}: Отправка сообщения '{
            message}' на сервер {server_address}")
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(1024)
        if data.decode() == 'ACK':
            print("Сообщение успешно доставлено!")
            break
        else:
            print("Ошибка доставки сообщения.")

    except socket.timeout:
        print(f"Попытка {attempt}: Таймаут при отправке сообщения.")
        print("Повторная попытка отправки...")

    except Exception as e:
        print(f"ошибка клиента: {e}")
        break

else:
    print(f'сервер не ответил после {max_attempts} попыток')
        