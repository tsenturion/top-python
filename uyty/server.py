import socket
import threading
from datetime import datetime

LOG_FILE = "connections.log"

def log_connection(ip, port):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Подключение с IP: {ip}, порт: {port}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    print(log_entry.strip())

def handle_client(conn, addr):
    ip, port = addr
    log_connection(ip, port)

    try:
        data = conn.recv(1024).decode()
        print(f"Сообщение от клиента {ip}: {data}")
        response = f"Сообщение получено от IP: {ip}"
        conn.send(response.encode())
    except Exception as e:
        print(f"Ошибка при работе с клиентом {ip}: {e}")
    finally:
        conn.close()

def start_server():
    host = "0.0.0.0"  
    port = 9000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущен на {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
