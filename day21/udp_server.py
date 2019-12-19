#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_

import socket

udp_server = socket.socket(type=socket.SOCK_DGRAM)  #dgram:datagram 数据报

ip_port = ('192.168.5.16',8001)
udp_server.bind(ip_port)

from_client_msg,client_addr = udp_server.recvfrom(1024)

print(from_client_msg)
print(client_addr)

udp_server.sendto(b'udp_server: hello,world.',client_addr)

udp_server.close()

