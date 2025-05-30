import socket

HOST = '127.0.0.1'
PORT = 5000

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((HOST, PORT))
        print(f"Подключено к серверу {HOST}:{PORT}")

        while True:
            message = input("Вы (клиент): ")
            client_sock.sendall(message.encode())

            if message.strip().lower() == 'exit':
                print("Завершение работы клиента.")
                break

            data = client_sock.recv(1024).decode()
            if not data:
                print("Сервер отключился.")
                break

            print(f"Сервер: {data}")
            if data.strip().lower() == 'exit':
                print("Сервер завершил соединение.")
                break

if __name__ == '__main__':
    start_client()
