import socket

def start_client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Подключено к серверу {host}:{port}")

    while True:
        # Отправляем сообщение
        message = input("Введите сообщение: ")
        client_socket.send(message.encode())

        if message.lower() == 'exit':
            print("Клиент завершает работу.")
            break

        # Получаем ответ от сервера
        data = client_socket.recv(1024).decode()
        print(f"Сервер: {data}")

        if data.lower() == 'exit':
            print("Сервер запросил отключение.")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()