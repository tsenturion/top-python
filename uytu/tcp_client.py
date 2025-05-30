import socket

HOST = '127.0.0.1'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = input("Client: ")
            s.sendall(message.encode())
            if message.lower() == 'exit':
                print("Exit command sent. Closing connection.")
                break
            data = s.recv(1024)
            response = data.decode()
            print(f"Server: {response}")
            if response.lower() == 'exit':
                print("Exit command received. Closing connection.")
                break

if __name__ == "__main__":
    main()
