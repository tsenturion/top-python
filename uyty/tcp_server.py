import socket

def start_server():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}. Waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        # Receive data from client
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Client disconnected.")
            break
        print(f"Client: {data}")

        # Send response
        response = input("You: ")
        conn.send(response.encode())
        if response.lower() == 'exit':
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()