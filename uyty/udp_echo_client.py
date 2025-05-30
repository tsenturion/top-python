import socket

HOST = '127.0.0.1'
PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Введите сообщение ('exit' для выхода): ")
    sock.sendto(msg.encode(), (HOST, PORT))

    if msg.strip().lower() == 'exit':
        print("Завершение клиента.")
        break

    data, _ = sock.recvfrom(1024)
    print(f"Ответ от сервера: {data.decode()}")

sock.close()