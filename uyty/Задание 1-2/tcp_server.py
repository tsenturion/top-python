import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(1)
    print("Сервер запущен. Ожидание подключения...")

    conn, addr = server_socket.accept()
    print(f"Клиент подключился: {addr}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Клиент: {data}")
        if data.lower() == 'exit':
            print("Клиент завершил соединение.")
            break

        response = input("Сервер: ")
        conn.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            print("Сервер завершает соединение.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
