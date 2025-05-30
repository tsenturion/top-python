import socket

def start_client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    while True:
        # Send message
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break

        # Receive response
        data = client_socket.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Server disconnected.")
            break
        print(f"Server: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()