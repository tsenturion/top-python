import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(">>", msg.decode())
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))

recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
recv_thread.start()

while True:
    msg = input()
    if msg.lower() == 'выход':
        break
    client_socket.send(msg.encode())

client_socket.close()
