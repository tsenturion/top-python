import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    print(f"Подключено к серверу {HOST}:{PORT}")

    while True:
        msg = input("Ваше сообщение: ")
        sock.sendall(msg.encode())
        if msg.strip().lower() == "exit":
            print("Завершение клиента.")
            break

        data = sock.recv(1024)
        if not data:
            print("Сервер отключился.")
            break
        reply = data.decode()
        print(f"Сервер: {reply}")
        if reply.strip().lower() == "exit":
            print("Сервер завершил работу.")
            break
