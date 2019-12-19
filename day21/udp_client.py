#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_

import socket

udp_client = socket.socket(type=socket.SOCK_DGRAM)  #dgram:datagram 数据报

server_ip_port = ('192.168.5.16',8001)

udp_client.sendto(b'udp_client: hello hum.',server_ip_port)

from_server_msg,server_addr = udp_client.recvfrom(1024)

print(from_server_msg)
print(server_addr)

