'''
    阻塞IO

'''

import socket
import time

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('127.0.0.1',8083))
server.listen(5)
print('卡哪儿了')
server.setblocking(False)

rlist = []

while 1:
    try:
        conn,addr = server.accept()
        rlist.append(conn)
        print('来自%s的链接请求' % addr)
    except BlockingIOError:
        print('去买点药')

    time.sleep(0.1)

    for con in rlist:
        from_client_msg = con.recv(1024)
        print(from_client_msg)

# conn.recv(1024)
# print('不卡了,你来玩')
