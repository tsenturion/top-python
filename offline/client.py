import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)

server_address = ('localhost', 12345)
message_base = 'привет сервер'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    message_id = f"{attempt}"
    message = f"{message_id}:{message_base} {attempt}"
    try:
        start_time = time.time()

        print(f"попытка {attempt}: отправка сообщения с ID {message_id}")
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(1024)

        end_time = time.time()
        delay = end_time - start_time

        print(f"ответ от сервера: {data.decode()}")
        print(f"задержка: {delay:.4f} с")

        if data.decode() == 'OK':
            print('успешно обработано сервером')
            break
        elif data.decode() == "ERROR":
            print("ошибка при обработке сообщения на сервере")
            break

    except socket.timeout:
        print("ответ от сервера не получен, пробуем снова")

    except Exception as e:
        print(f"ошибка клиента {e}")
        break

else:
    print('сервер не ответил после 3 попыток')