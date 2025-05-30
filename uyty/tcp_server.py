import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 5000         # Порт сервера

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f'Сервер запущен на {HOST}:{PORT}, ожидаем подключения...')
        conn, addr = s.accept()
        with conn:
            print(f'Клиент подключён: {addr}')
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f'Клиент: {data}')
                if data.lower() == 'exit':
                    print('Клиент завершил соединение.')
                    break
                reply = input('Вы: ')
                conn.sendall(reply.encode())
                if reply.lower() == 'exit':
                    print('Вы завершили соединение.')
                    break

if __name__ == '__main__':
    start_server()
