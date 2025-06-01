import socket

HOST = '127.0.0.1'
PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f'UDP эхо-сервер запущен на {HOST}:{PORT}')

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    print(f'Получено сообщение от {addr}: {message}')

    if message.strip().lower() == 'exit':
        print('Получена команда завершения. Сервер выключается.')
        break

    sock.sendto(data, addr)  # эхо: возвращаем ту же строку

sock.close()
print('Сервер завершил работу.')
