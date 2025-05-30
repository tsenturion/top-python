import socket

HOST = '127.0.0.1'  # Адрес сервера
PORT = 6000         # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        message = input("Введите сообщение ('exit' для выхода): ")
        client_socket.sendto(message.encode('utf-8'), (HOST, PORT))

        if message.strip().lower() == 'exit':
            print("Завершение клиента.")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Ответ от сервера: {data.decode('utf-8')}")