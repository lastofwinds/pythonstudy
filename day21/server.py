import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #允许IP地址和端口重用

ip_port = ('192.168.5.16', 8001) #创建一张电话卡

# 绑定IP地址和端口
server.bind(ip_port)

# 监听IP地址和端口
server.listen(5)  #开机
conn, addr = server.accept()  #等待电话接入

flag = 0

while not flag:
    user_info = conn.recv(1024).decode('utf-8')
    with open(r'D:\python study\day22\account', 'r', encoding='utf-8') as f:
        for i in f:
            if i.strip() == user_info:
                conn.send('登陆成功'.encode('utf-8'))
                flag = 1
                break
            else:
                conn.send('用户名或密码错误'.encode('utf-8'))

conn.close()
server.close()


