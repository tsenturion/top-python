

"""ip = socket.gethostbyname("google.com")
print(ip)
"""
"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = s.recv(4096)
print(response.decode())
s.close()"""
"""
hostname = 'google.com'
ip_address = socket.gethostbyname(hostname)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, 80))
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client_socket.send(request.encode())

respone = client_socket.recv(4096)
print("ответ сервера", respone.decode(errors='ignore'))

client_socket.close()"""

"""server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9000))
server_socket.listen(1)
print('("0.0.0.0", 9000)')

conn, addr = server_socket.accept()
print(f'ip {addr[0]} порт {addr[1]}')

data = conn.recv(1024)
print('получено', data.decode())
conn.send('принято'.encode())

conn.close()
server_socket.close()"""

"""hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"локальный ip {local_ip}")

info = socket.getaddrinfo('localhost', 0)
for entry in info:
    print(entry[4][0])

import ipaddress
addr = ipaddress.ip_address('192.168.1.10')
print(addr.is_private)"""

'''
клиент узнает ip адрес сервера по имени хоста (DNS)
сервер выводит ip адрес каждого подключившего клиента
сообщения передаются по TCP
логируется ip и порт всех входящих соединений
socket
'''
import socket
