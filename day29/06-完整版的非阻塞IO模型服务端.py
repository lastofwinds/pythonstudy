'''
    非阻塞IO模型
        缺点：
            1.循环调用recv()将大幅提高CPU占用率，在低配主机上很容易卡死
            2.任务完成的响应延迟增大了，因为每过一段时间才去轮询一次read操作，而任务可能在两次轮询
            之间的任意时间完成，这会导致整体数据吞吐量的降低。
'''

import socket
import time

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8003))
server.listen(5)

server.setblocking(False)  #设置不阻塞
r_list = [] #存储所有来请求server端的conn连接
w_list = {} #用来存储所有已经有了请求数据conn的请求数据

while 1:
    try:
        conn,addr = server.accept()  #阻塞住，等待，否则报错
        r_list.append(conn)   #为了将连接保存起来，不然下次循环的时候，上次的连接就丢失了

    except BlockingIOError:
        #非阻塞IO的精髓在于完全没有阻塞
        print('在做其他事情')

    del_rlist = []
    for conn in r_list:
        try:
            data = conn.recv(1024)  #阻塞住
            if not data:
                conn.close()
                del_rlist.append(conn)
                continue
            w_list[conn] = data.upper()
            # conn.send(b'hh')
        except BlockingIOError:  #如果没有收成功，则继续下一个套接字的接收
            continue
        except ConnectionResetError:  #当套接字出现异常，则关闭，加入删除列表，等待删除
            conn.close()
            del_rlist.append(conn)

    #遍历写列表，依次取出套接字发送内容
    del_wlist = []
    for conn,data in w_list.items():
        try:
            conn.send(data)
            del_wlist.append(conn)
        except BlockingIOError:
            continue

    for conn,data in del_rlist:
        r_list.remove(conn)

    for conn in del_wlist:
        w_list.pop(conn)
