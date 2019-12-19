import socketserver
import socket
import struct
import json

tcp_server = socket.socket()


ip_port = ('127.0.0.1', 8080)
tcp_server.bind(ip_port)
tcp_server.listen()


# 客户端上传文件路径
client_file_path = r'D:\python study\day22\ftp功能\uploads'
conn,addr = tcp_server.accept()

# 接收文件信息长度转换的4字节数据
file_info_stru = conn.recv(4)

# 解包文件信息的长度
file_info_len = struct.unpack('i',file_info_stru)[0]

# 然后接受文件的描述信息
client_file_info = conn.recv(file_info_len).decode('utf-8')

# 将接收到的json字符串反序列化
abc_file_info = json.loads(client_file_info)
print('abc_file_info>>>',abc_file_info)
client_file_size = abc_file_info['file_size']

recv_all_size = 0

# 拼接全路径

client_full_path = client_file_path + '\\' + abc_file_info['file_name']
with open(client_full_path,'wb') as f:
    while recv_all_size < client_file_size:
        everr_recv_data = conn.recv(1024)
        f.write(everr_recv_data)
        recv_all_size += len(everr_recv_data)

conn.send('上传成功！'.encode('utf-8'))
conn.close()
tcp_server.close()


