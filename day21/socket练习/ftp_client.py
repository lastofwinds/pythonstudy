#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socket
import struct
import os
import json

tcp_client = socket.socket()
server_ip_port = ('127.0.0.1', 8080)
tcp_client.connect(server_ip_port)


file_info = {
    'file_path': r'D:\python study\day22\socket练习',
    'file_name': 'php.ini',
    'file_size': None,
}

# 将文件大小添加到文件信息的字典里
file_info['file_size'] = file_size

file_size = os.path.getsize(file_info['file_path'])
# 通过json模块将字典类型的文件信息数据转换成json类型的字符串
file_info_json = json.dumps(file_info)
file_info_len = len(file_info_json)
file_info_stru = struct.pack('i', file_info_len)

tcp_client.sendall(file_info_stru)
tcp_client.sendall(file_info_json.encode('utf-8'))

all_file_size = 0
all_size_len = 0

with open(file_info['file_path'],'rb') as f:
    while all_size_len < file_size:
        every_read_data = f.read(read_size)
        all_file_size += every_read_data
        all_size_len += len()

tcp_client.send(all_file_data)
print(file_size)




