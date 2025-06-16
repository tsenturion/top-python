import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 6000         # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP сервер запущен на {HOST}:{PORT}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Получено от {client_address}: {message}")

        if message.strip().lower() == 'exit':
            print("Команда 'exit' получена. Завершение сервера.")
            break

        server_socket.sendto(data, client_address)
        print(f"Отправлено обратно: {message}")