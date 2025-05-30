import socket

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)
        print(f"Сервер запущен на {HOST}:{PORT}, ожидаем подключение...")

        conn, addr = server_sock.accept()
        with conn:
            print(f"Клиент подключен: {addr}")

            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f"Клиент: {data}")
                if data.strip().lower() == 'exit':
                    print("Клиент завершил соединение.")
                    break

                response = input("Вы (сервер): ")
                conn.sendall(response.encode())

                if response.strip().lower() == 'exit':
                    print("Завершение работы сервера.")
                    break

if __name__ == '__main__':
    start_server()
