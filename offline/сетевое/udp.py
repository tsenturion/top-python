"""
user datagram protocol
протокол без установления соединения
скорость и низкие накладные расходы
допустимы потери, но важна скорость доставки
серверу приходится определять, от кого пришло сообщение
широковещательные и мультикаст-сообщения
MTU
"""
"""
отличия от tcp на уровне кода
нет listen accept connect
sendto и recvfrom вместо send recv
"""
import socket

socket.settimeout(5)

"""
broadcast
multicast
"""
socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#255.255.255.255

