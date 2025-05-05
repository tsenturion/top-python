import socket

HOSTNAME = 'localhost'  # можно заменить на имя удалённого хоста
PORT = 12345

try:
    server_ip = socket.gethostbyname(HOSTNAME)
    print(f"[i] IP сервера: {server_ip}")
except socket.gaierror:
    print("[!] Не удалось разрешить имя хоста")
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_ip, PORT))
    print(f"[+] Подключено к серверу {server_ip}:{PORT}")
    
    while True:
        msg = input("Введите сообщение (или 'exit' для выхода): ")
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode('utf-8'))
