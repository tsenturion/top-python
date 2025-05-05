import socket

HOST = '0.0.0.0'  # слушать на всех интерфейсах
PORT = 12345      # любой свободный порт

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[+] Сервер запущен на порту {PORT}, ожидаем подключения...")

    while True:
        conn, addr = server_socket.accept()  # addr = (ip, port)
        print(f"[+] Подключение от {addr[0]}:{addr[1]}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[{addr[0]}] Сообщение: {data.decode('utf-8')}")
