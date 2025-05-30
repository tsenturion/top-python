import socket

HOST = '127.0.0.1'
PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"UDP Echo Server started on {HOST}:{PORT}")
        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode()
            print(f"Received from {addr}: {message}")
            s.sendto(data, addr)
            if message.lower() == 'exit':
                print("Exit command received. Shutting down server.")
                break

if __name__ == "__main__":
    main()
