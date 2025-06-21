import socket

server = socket.socket()
hostname = "127.0.0.1"
port = 5000
server.bind((hostname, port))
server.listen(5)
print("Server is working")
isrunning = True
con, addr = server.accept()
print("Client connected, address: ", addr)
while isrunning:
    client_message = con.recv(1024)
    message = client_message.decode()
    if not message or message.lower() == "exit":
        isrunning = False
        break
    else:
        print(f"Client-{addr}: {message}")
        answer = f"Message is: {message}"
        print(answer)
        con.send(answer.encode())
con.close()
server.close()