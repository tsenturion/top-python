import socket

HOST = '127.0.0.1'
PORT = 6000

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
        while True:
            message = input("Клиент: ")
            client_sock.sendto(message.encode(), (HOST, PORT))
            if message.lower() == 'exit':
                print("Клиент завершает работу.")
                break
            data, _ = client_sock.recvfrom(1024)
            print(f"Сервер: {data.decode()}")

if __name__ == "__main__":
    start_client()
