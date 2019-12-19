#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socket
tcp_client = socket.socket()
server_ip_port = ('127.0.0.1', 8080)
tcp_client.connect(server_ip_port)

while True:
    client_msg = input('xiaoli: ')

    tcp_client.send(client_msg.encode('utf-8'))

    from_server_msg = tcp_client.recv(1024).decode()
    print(from_server_msg)

tcp_client.close()



