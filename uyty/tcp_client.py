import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))
    print("Подключено к серверу.")

    while True:
        message = input("Клиент: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("Клиент завершает соединение.")
            break

        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Сервер: {data}")
        if data.lower() == 'exit':
            print("Сервер завершил соединение.")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
