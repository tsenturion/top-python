import socket

HOST = '127.0.0.1'  # Адрес сервера
PORT = 5000         # Порт сервера

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f'Подключено к серверу {HOST}:{PORT}')
        while True:
            message = input('Вы: ')
            s.sendall(message.encode())
            if message.lower() == 'exit':
                print('Вы завершили соединение.')
                break
            data = s.recv(1024).decode()
            print(f'Сервер: {data}')
            if data.lower() == 'exit':
                print('Сервер завершил соединение.')
                break

if __name__ == '__main__':
    start_client()
