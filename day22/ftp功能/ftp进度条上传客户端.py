import socket
import struct
import os
import json

tcp_client = socket.socket()
server_ip_port = ('127.0.0.1', 8080)
tcp_client.connect(server_ip_port)
read_size = 1024


file_info = {
    'file_path': r'D:\迅雷下载\archlinux-2019.12.01-x86_64.iso',
    'file_name': 'archlinux-2019.12.01-x86_64.iso',
    'file_size': None,
}

# 获取文件大小
file_size = os.path.getsize(file_info['file_path'])

# 将文件大小添加到文件信息的字典中
file_info['file_size'] = file_size

# 因为发送数据是字节类型，必须将字典转换为bytes类型，但是字典不能直接转换为bytes
# 所以我们使用json将字典类型文件信息数据转换为json字符串
file_info_json = json.dumps(file_info)

# 获取字符串的长度
file_info_len = len(file_info_json)

# 将长度打包成4个字节的数据
file_info_stru = struct.pack('i', file_info_len)

# 将打包好的4个字节数据和我的文件信息数据一起发送给服务器
tcp_client.send(file_info_stru)
tcp_client.send(file_info_json.encode('utf-8'))


all_file_data = b''
all_size_len = 0

with open(file_info['file_path'],'rb') as f:
    while all_size_len < file_size:
        every_read_data = f.read(read_size)
        all_file_data += every_read_data
        all_size_len += len(every_read_data)
        tcp_client.send(every_read_data)

        # 得到一个浮点数%
        percent_data = round(all_size_len/file_size,2) * 100
        print('\r%s%%'%percent_data,end='')


print(tcp_client.recv(1024).decode('utf-8'))
tcp_client.close()
