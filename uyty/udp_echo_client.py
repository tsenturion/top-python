import socket

def start_client():
    host = '127.0.0.1'
    port = 6000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"UDP-клиент подключен к {host}:{port}")

    while True:
        message = input("Введите сообщение: ")
        client_socket.sendto(message.encode(), (host, port))

        if message.lower() == 'exit':
            print("Клиент завершает работу.")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Ответ от сервера: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()