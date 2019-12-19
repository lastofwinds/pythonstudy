#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


# 1.socket常用操作：
# sk.bind(address)
#     s.bind(address)
#         将套接字绑定到地址，address地址的格式却决于地址族，在AF_INET下，以元组的形式表示出来(host,port)
#
# sk.listen(backlog)
#     开始监听传入连接,backlog指定在拒绝连接之前，可以挂起的最大连接量
#
#         backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
#         这个值不能无限大，因为要在内核中维护连接队列
#
# sk.setblocking(bool)
#     是否阻塞(默认为True)，如果设置False，那么accept和recv时会报错
#
#
# sk.accept()
#     接受连接并返回(conn, addr)，其中conn是新的套接字对象，可以用来接受和发送数据。address是连接客户端的地址
#     接受TCP
#     客户链接（阻塞式）等待连接到来
#
# sk.connect(address)
#     连接到address处的套接字，一般，address的格式为元组(hostname,port)，如果连接出错，返回socket.error
#
# sk.connect_ex(address)
#     同上，不过会有返回值，连接成功时返回0，失败返回编码
#
# sk.close()
#     关闭套接字
#
# sk.recv(bufsize[,flag])
#     接受套接字的数据，数据以字符串形式返回，bufsize指定最多可以接受的数量，flag提供有关消息的其他信息，通常可以忽略
#
# sk.recvfrom(bufsize[,flag])
#     与recv()类似，但返回值是(data,address)。其中data是包含接受数据的字符串，address是发送数据的套接字地址
#
# sk.send(string[,flag])
#     将string中的数据发送到连接的套接字，返回值是要发送的字节数量，改数量可能小于string的字节大小，即：内容可能不会全部发送出去
#
# sk.sendall(string[.flag])
#     将string中的护具发送到连接的套接字，但在返回之前会尝试发送所有数据，成功返回None，失败返回异常
#
#
# sk.sendto(string[,flag]，address)
#     将数据发送到套接字，address是形式为(ipaddr,port)的元组，指定远程地址，返回值是发送的字节数，该函数主要用于UDPxieyi1
#
# sk.settimeout(timeout)
#     设置套接字操作的超时期，timeout是一个浮点数，会返回秒，值为None表示没有超时，一般超时期应该在刚创建套接字时设置
#
# sk.getpeername()
#     返回连接套接字的远程地址，返回值通常是元组(ipaddr,port)
#
#
# sk.getsockname()
#     返回连接套接字自己的地址，通常是元组同上
#
# sk.fileno()
#     套接字文件描述符


# 2.粘包

# 缓冲区：暂时存放传输数据的，防止你的程序在发送数据的时候卡住，提高代码运行效率
# 输入缓冲区:revc
# 输出缓冲区:send
#
# 缓冲区有长度限制
# MTU:最大输出单元，网络层限制是1500B，每次发送数据的时候最好低于
#
#
# 粘包现象：
#         1.连续发送小的数据，间隔时间很短，有可能一次就接受到这几个连续的拼接在一起的小数据，#原因：为了提高TCP传输效率，内部提供
#     Nagel算法，就是为了避免连续发送的小包，尽量一次少次传输完
#
#         2.当你一次接受的数据长度小于你一次发送的数据长度，那么一次接受完剩下的数据会在下一次接受数据的时候被一起接受。面向流传输
#
#     注意：粘包的根本原因是双方互不清楚对方的数据长度







