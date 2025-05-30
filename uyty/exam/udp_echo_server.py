import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = server.recvfrom(1024) 
    print("received message: %s" % data.decode())
    if data.decode().lower() == "exit":
        break
    else:
        server.sendto(data, addr)