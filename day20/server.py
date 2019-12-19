#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('192.168.5.16', 8001) #创建一张电话卡

# 绑定IP地址和端口
server.bind(ip_port)

# 监听IP地址和端口
server.listen(5)  #开机
conn, addr = server.accept()  #等待电话接入


while True:
    from_client_msg = conn.recv(1024)
    from_client_msg = from_client_msg.decode('utf-8')

    print('client_msg: %s' % from_client_msg)
    msg = input('server: ')

    conn.send(msg.encode('utf-8'))


conn.close()
server.close()