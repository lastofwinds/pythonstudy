#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip_port = ('192.168.5.16', 8001)

client.connect(server_ip_port)

while True:
    msg = input("client: ")
    client.send(msg.encode('utf-8'))

    from_server_msg = client.recv(1024)
    from_server_msg = from_server_msg.decode('utf-8')
    print('server_msg: %s' % from_server_msg)

client.close()
