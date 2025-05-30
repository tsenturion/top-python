import socket

def run_udp_server():
    host = '127.0.0.1'
    port = 5001
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((host, port))
            print(f"UDP Server started on {host}:{port}. Waiting for messages...")
            
            while True:
                data, addr = s.recvfrom(1024)
                message = data.decode()
                print(f"Client [{addr}]: {message}")
                
                if message.lower() == 'exit':
                    print("Client requested termination.")
                    break
                
                response = input("You: ")
                s.sendto(response.encode(), addr)
                if response.lower() == 'exit':
                    print("Server initiated termination.")
                    break
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("UDP Server shutdown.")

if __name__ == "__main__":
    run_udp_server()