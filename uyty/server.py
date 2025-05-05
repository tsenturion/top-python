import socket
import os

def read_line(conn):
    line = b''
    while True:
        char = conn.recv(1)
        if not char or char == b'\n':
            break
        line += char
    return line.decode('utf-8')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9000))
server_socket.listen(1)
print("Сервер запущен, ожидаем подключение...")

conn, addr = server_socket.accept()
print(f"Клиент подключился: {addr}")

command = read_line(conn).strip()
filename = read_line(conn).strip()

print(f"Получена команда: {command}")
print(f"Имя файла: {filename}")

if command == "UPLOAD":
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print("Файл успешно принят.")
    conn.sendall("Файл получен\n".encode('utf-8'))

elif command == "DOWNLOAD":
    if not os.path.exists(filename):
        error_message = "ОШИБКА: файл не найден\n"
        conn.sendall(error_message.encode('utf-8'))
        print("Запрошенный файл не найден.")
    else:
        with open(filename, 'rb') as f:
            while chunk := f.read(1024):
                conn.sendall(chunk)
        print("Файл отправлен клиенту.")

else:
    error_message = "ОШИБКА: неизвестная команда\n"
    conn.sendall(error_message.encode('utf-8'))

conn.close()
server_socket.close()
