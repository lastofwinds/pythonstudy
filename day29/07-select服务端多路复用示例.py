'''select多路复用'''

from socket import *
import select

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8093))

server.listen(5)
server.setblocking(False)

rlist = [server,]
wlist = []

del_list = []
wdict = {}

while 1:
    print('laikankan')
    r1,w1,x1 = select.select(rlist,wlist,[],)

    print(r1)
    print(rlist)

    for s in r1:   #循环所有动静的对象
        if s == server:
            conn,addr = s.accept()
            print('来自%s:%s' % (addr[0],addr[1]))
            rlist.append(conn)
        else:
            data = s.recv(1024)
            if not data:
                s.close()
                rlist.remove(s)
            wdict[s] = data.upper()
            wlist.append(s)

            print(data)

    for w in w1:
        w.send(b'linux is very good')
