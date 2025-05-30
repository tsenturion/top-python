import socket

HOST = '127.0.0.1'
PORT = 6000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        server_sock.bind((HOST, PORT))
        print(f"UDP сервер запущен на {HOST}:{PORT}")

        while True:
            data, addr = server_sock.recvfrom(1024)
            message = data.decode()
            print(f"Получено от {addr}: {message}")
            if message.lower() == 'exit':
                print("Получена команда exit. Сервер завершает работу.")
                break
            server_sock.sendto(data, addr)

if __name__ == "__main__":
    start_server()
