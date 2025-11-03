import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"Сервер запущен на {HOST}:{PORT}. Ожидание клиента...")
    conn, addr = server_sock.accept()
    print(f"Подключён клиент {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Клиент отключился.")
                break
            msg = data.decode()
            print(f"Клиент: {msg}")
            if msg.strip().lower() == "exit":
                print("Получен exit, завершение.")
                break

            reply = input("Ваш ответ: ")
            conn.sendall(reply.encode())
            if reply.strip().lower() == "exit":
                print("Завершение по команде exit.")
                break
