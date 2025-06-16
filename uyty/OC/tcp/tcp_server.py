import socket

def run_tcp_server():
    host = '127.0.0.1'
    port = 5000
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            print(f"TCP Server started on {host}:{port}. Waiting for connection...")
            
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode()
                    if not data or data.lower() == 'exit':
                        print("Client requested termination.")
                        break
                    print(f"Client: {data}")

                    response = input("You: ")
                    conn.sendall(response.encode())
                    if response.lower() == 'exit':
                        print("Server initiated termination.")
                        break
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("TCP Server shutdown.")

if __name__ == "__main__":
    run_tcp_server()