import socket

client = socket.socket()
hostname = "127.0.0.1"
port = 5000
client.connect((hostname, port))
print("Connected")
isrunning = True
while isrunning:
    message = input("> ")
    if message.lower() == "close":
        break
    else: 
        client.send(message.encode())
        data = client.recv(1024)
        print("Server sent: ", data.decode())
client.close()
