import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)  # исправлено: timeout задается для client_socket

server_address = ("localhost", 12345)
max_attempts = 3

while True:
    message_base = input("Введите сообщение (или 'exit' для выхода): ")
    if message_base.lower() == 'exit':
        print("Завершение программы.")
        break

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
