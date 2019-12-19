import socket,hashlib

client = socket.socket()
client.connect(('localhost', 999))


while True:
    cmd = input("windowsCmd>>: ".strip())
    if len(cmd) == 0:
        continue

    if cmd.startswith("get"):
        client.send(cmd.encode('utf-8'))    #发送命令
        server_response = client.recv(1024)     #接收server端回复

        print("文件大小",server_response.decode('utf-8'))   #打印server端信息，文件大小
        client.send(b"ready....")   #回复server端

        size = int(server_response.decode('utf-8'))     #文件大小

        receive_size = 0    #接收size累加
        filename = cmd.split()[1]  #文件名

        f = open('lala','wb')   #打开文件
        m = hashlib.md5()       #创建md5对象

        while receive_size < size:  #信息传输总量叠加
            if(size - receive_size > 1024):
                a = 1024

            else:
                a = size - receive_size
                print(a,size,receive_size)

            data = client.recv(a)
            receive_size += len(data)   #接收client传输的信息
            m.update(data)   #md5加密用update函数
            f.write(data)

        print('file rece done.')
        new_file_md5 = m.hexdigest()

        f.close()
        server_file_md5 = client.recv(1024)
        print('server file',server_file_md5)
        print('clien file',new_file_md5)

client.close()


