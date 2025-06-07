import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6000

 
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    MESSAGE = input("> ")
    if MESSAGE.lower() == "exit":
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        break
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
    message, addr = sock.recvfrom(1024)
    print(message.decode())
