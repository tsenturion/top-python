import socket

def start_client():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Подключено к серверу {host}:{port}")
        while True:
            message = input("Клиент: ")
            client_socket.sendall(message.encode())
            if message.lower() == 'exit':
                print("Завершение по команде клиента.")
                break
            data = client_socket.recv(1024)
            if not data:
                print("Сервер отключился.")
                break
            response = data.decode()
            print(f"Сервер: {response}")
            if response.lower() == 'exit':
                print("Завершение по команде сервера.")
                break

if __name__ == "__main__":
    start_client()