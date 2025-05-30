import socket

def start_server():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Сервер запущен на {host}:{port}. Ожидание подключения клиента...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Клиент подключён: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Клиент отключился.")
                    break
                message = data.decode()
                print(f"Клиент: {message}")
                if message.lower() == 'exit':
                    print("Завершение по команде клиента.")
                    break
                response = input("Сервер: ")
                conn.sendall(response.encode())
                if response.lower() == 'exit':
                    print("Завершение по команде сервера.")
                    break

if __name__ == "__main__":
    start_server()
    