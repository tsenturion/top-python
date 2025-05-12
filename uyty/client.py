import socket

def main():
    hostname = input("Введите адрес сервера (имя или IP): ").strip()
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"{hostname} → {ip_address}")
    except socket.gaierror:
        print("Ошибка: не удалось разрешить адрес")
        return

    port = 9000

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, port))

        message = input("Введите сообщение для отправки: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Ответ сервера: {response}")

        client_socket.close()
    except Exception as e:
        print(f"Ошибка при подключении: {e}")

if __name__ == "__main__":
    main()
