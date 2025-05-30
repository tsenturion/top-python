import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 6000))
    print("UDP сервер запущен и ожидает сообщений...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Получено от {addr}: {message}")
        if message.lower() == 'exit':
            print("Завершение работы сервера.")
            break
        server_socket.sendto(data, addr)

    server_socket.close()

if __name__ == "__main__":
    main()
