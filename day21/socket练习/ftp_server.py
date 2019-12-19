#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socket
import struct
import json

tcp_server = socket.socket()
ip_port = ('127.0.0.1', 8080)
tcp_server.bind(ip_port)

tcp_server.listen()
conn, addr = tcp_server.accept()

# 首先接受到的文件信息长度转换出来的4个字节的数据
file_info_stru = conn.recv(4)


#解包文件信息的长度
file_info_len = struct.unpack('i', file_info_stru)[0]

client_file_info = conn.recv(file_info_len).decode('utf-8')

abc_file_info = json.loads(client_file_info)
print('abc_file_infp>>>', abc_file_info)

client_file_size = abc_file_info['file_size']