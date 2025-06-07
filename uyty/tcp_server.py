import socket

def start_server():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер запущен на {host}:{port}. Ожидание подключения...")

    conn, addr = server_socket.accept()
    print(f"Подключен клиент: {addr}")

    while True:
       
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Клиент: {data}")

        if data.lower() == 'exit':
            print("Клиент запросил отключение.")
            conn.send("Сервер завершает работу.".encode())
            break

     
        message = input("Сервер, введите ответ: ")
        conn.send(message.encode())

        if message.lower() == 'exit':
            print("Сервер завершает работу.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()