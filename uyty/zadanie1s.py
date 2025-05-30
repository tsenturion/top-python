import socket

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)
        print(f"Сервер запущен на {HOST}:{PORT}, ожидаем подключение...")

        conn, addr = server_sock.accept()
        print(f"Клиент подключился: {addr}")
        with conn:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f"Клиент: {data}")
                if data.lower() == 'exit':
                    print("Клиент завершил соединение.")
                    break
                reply = input("Сервер: ")
                conn.sendall(reply.encode())
                if reply.lower() == 'exit':
                    print("Завершение работы сервера.")
                    break

if __name__ == "__main__":
    start_server()
