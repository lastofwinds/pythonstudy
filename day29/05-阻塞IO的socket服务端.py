'''
    阻塞IO服务端
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
rl = []

while 1:
    try:
        conn,addr = server.accept()
        print(addr)
        rlist.append(conn)
        print('来自%s:%s的链接请求' % (addr[0],addr[1]))
    except BlockingIOError:
        print('去买点药')

    time.sleep(0.1)
    print('rlist',rlist,len(rlist))

    for con in rlist:
        try:
            from_client_msg = con.recv(1024)
        except BlockingIOError:
            continue
        except ConnectionResetError:
            con.close()
            rl.append(con)
        print('>>>>',rl)
    for remove_con in rl:
        rlist.remove(remove_con)
    rl.clear()


