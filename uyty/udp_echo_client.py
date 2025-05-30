import socket

HOST = '127.0.0.1'
PORT = 6000

def start_udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
        while True:
            message = input("Вы (клиент): ")
            client_sock.sendto(message.encode(), (HOST, PORT))

            data, _ = client_sock.recvfrom(1024)
            print(f"Сервер: {data.decode()}")

            if message.strip().lower() == 'exit':
                print("Завершение работы клиента.")
                break

if __name__ == '__main__':
    start_udp_client()
