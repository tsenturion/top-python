import socket

def start_server():
    host = '127.0.0.1'
    port = 6000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Echo Server started on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        if message.lower() == 'exit':
            print(f"Client {addr} disconnected.")
            break
        print(f"Received from {addr}: {message}")
        server_socket.sendto(data, addr)

    server_socket.close()

if __name__ == "__main__":
    start_server()