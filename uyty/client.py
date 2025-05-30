import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.timeout(3)

server_address = ("localhost", 12345)
message_base = 'Hello, server! это пакет с id'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    message_id = f'{attempt}'
    message = f'{message_base} {message_id}'
    try:
        start_time = time.time()

        print(f"Попытка {attempt}: Отправка сообщения '{message}' на сервер {server_address}")
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(1024)
        end_time = time.time()
        delay = end_time - start_time

        print(f"ответ от сервера: {data.decode()}")
        print(f"Задержка: {delay:.4f} секунд")

        if data.decode() == "OK":
            print(f"Сообщение '{message}' успешно отправлено и получено от сервера.")
            break
        elif data.decode() == "ERROR":
            print(f"Сообщение '{message}' не удалось отправить или получить от сервера.")
            break

    except socket.timeout:
        print(f"Попытка {attempt}: Таймаут при отправке сообщения.")
        print("Повторная попытка отправки...")

    except Exception as e:
        print(f"ошибка клиента: {e}")
        break

else:
    print(f'сервер не ответил после {max_attempts} попыток')
        