import socket

HOST = '127.0.0.1'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Server started on {HOST}:{PORT}, waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"Client: {message}")
                if message.lower() == 'exit':
                    print("Exit command received. Closing connection.")
                    break
                response = input("Server: ")
                conn.sendall(response.encode())
                if response.lower() == 'exit':
                    print("Exit command sent. Closing connection.")
                    break

if __name__ == "__main__":
    main()
