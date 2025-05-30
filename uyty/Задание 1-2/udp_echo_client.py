import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 6000)

    while True:
        message = input("Клиент: ")
        client_socket.sendto(message.encode('utf-8'), server_address)
        if message.lower() == 'exit':
            print("Клиент завершает работу.")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Сервер: {data.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    main()
