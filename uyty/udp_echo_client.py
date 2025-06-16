import socket

HOST = '127.0.0.1'
PORT = 6000

def start_udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = input("Вы: ")
            s.sendto(message.encode(), (HOST, PORT))

            if message.lower() == 'exit':
                print("Вы завершили соединение.")
                break

            data, _ = s.recvfrom(1024)
            print("Сервер:", data.decode())

if __name__ == '__main__':
    start_udp_client()
