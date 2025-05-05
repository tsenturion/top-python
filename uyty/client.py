import socket
import os

def send_line(sock, line):
    sock.sendall(f"{line}\n".encode('utf-8'))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))

command = input("Введите команду (UPLOAD / DOWNLOAD): ").strip().upper()
filename = input("Введите имя файла: ").strip()

send_line(client_socket, command)
send_line(client_socket, filename)

if command == "UPLOAD":
    if not os.path.exists(filename):
        print("Файл не найден.")
        client_socket.close()
    else:
        with open(filename, 'rb') as f:
            while chunk := f.read(1024):
                client_socket.sendall(chunk)

        client_socket.shutdown(socket.SHUT_WR)  # Сообщаем серверу, что данные отправлены

        response = b''
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part

        print("Ответ сервера:", response.decode('utf-8'))

elif command == "DOWNLOAD":
    is_error = False
    with open(f"загружено_{filename}", 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            if data.startswith("ОШИБКА:".encode()):
                print(data.decode('utf-8'))
                is_error = True
                break
            f.write(data)
    if not is_error:
        print(f"Файл успешно сохранён как загружено_{filename}")


else:
    print("Неизвестная команда.")

client_socket.close()
