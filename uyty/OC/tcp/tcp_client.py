import socket

def run_tcp_client():
    host = '127.0.0.1'
    port = 5000
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Connected to TCP server at {host}:{port}")
            
            while True:
                message = input("You: ")
                s.sendall(message.encode())
                if message.lower() == 'exit':
                    print("Client initiated termination.")
                    break
                
                data = s.recv(1024).decode()
                if not data or data.lower() == 'exit':
                    print("Server requested termination.")
                    break
                print(f"Server: {data}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        print("TCP Client disconnected.")

if __name__ == "__main__":
    run_tcp_client()