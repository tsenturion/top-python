import socket

HOST = '127.0.0.1'
PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = input("Enter message: ")
            s.sendto(message.encode(), (HOST, PORT))
            data, _ = s.recvfrom(1024)
            response = data.decode()
            print(f"Echo from server: {response}")
            if message.lower() == 'exit':
                print("Exit command sent. Closing client.")
                break

if __name__ == "__main__":
    main()
