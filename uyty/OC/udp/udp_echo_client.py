import socket

def run_udp_client():
    host = '127.0.0.1'
    port = 5001
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            server_address = (host, port)
            print(f"UDP Client ready to send to {host}:{port}")
            
            while True:
                message = input("You: ")
                s.sendto(message.encode(), server_address)
                if message.lower() == 'exit':
                    print("Client initiated termination.")
                    break
                
                data, _ = s.recvfrom(1024)
                response = data.decode()
                if response.lower() == 'exit':
                    print("Server requested termination.")
                    break
                print(f"Server: {response}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        print("UDP Client disconnected.")

if __name__ == "__main__":
    run_udp_client()