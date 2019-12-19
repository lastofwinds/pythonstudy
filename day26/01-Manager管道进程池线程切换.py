#创建管道的类
# Pipe([duplex]): 在进程之间创建一条管道,并返回元祖(conn1,conn2),其中conn1,conn2表示管道两端的连接对象,强调一点
# 必须在产生Process对象之前产生管道


#参数介绍:
# dumplex:默认管道是全双工的,如果将duplex设置成False,conn只能用于接收,conn2只能用于发送


#主要方法
# conn1.recv():接受conn2.send(obj)发送的对象,如果没有消息可接受,recv方法会一直阻塞,如果连接的另一端
# 已经关闭,那么recv()方法会抛出Error
# conn1.send(obj):通过发送连接对象,obj的是与序列化兼容的任意对象


# conn1.poll([timeout]):如果连接上的数据可用,返回True,timeout指定等待的最长时限,如果省略此参数,方法将立即返回结果
# ，如果timeout设成None，操作将无限期地等待数据到达


# conn1.recv_bytes([maxlegth]):接收一条完整的字节信息,maxlength指定要接受的最大字节数，如果进入的消息
# 超过这个最大值，将引发IOError异常,并且在连接上无法进一步读取，如果连接另一端已经关闭，再也没数据，引发
# Error


# conn.send_bytes(buffer[,offset[,size]]):通过连接发送字节数据缓冲区,buffer是支持缓冲区接口的任意对象,offset
# 是缓冲区中字节偏移量,而size是要发送字节数,结果数据以单条消息的形式发出,然后调出c.recv_bytes()函数进行接受


# conn1.recv_bytes_into(buffer[,offset]):接收一条完整的字节消息,并把它保存在buffer对象中,该对象支持可写入的缓冲区
# offset指定缓冲区中放置消息处的字节位移，返回值是收到的字节数，如果消息长度大于可用缓冲区，引发BufferTooShort异常


from multiprocessing import Process,Pipe

# conn1,conn2 = Pipe()
# conn1.send('你好')
#
# print('>>>>>')
# msg = conn2.recv()
# print(msg)


# def func1(conn2):
#     msg = conn2.recv()
#     print(msg)
#
# if __name__ == '__main__':
#     conn1,conn2 = Pipe()
#     p = Process(target=func1,args=(conn2,))
#     p.start()
#
#     conn1.send('你好啊,维克托')


'''模拟管道异常'''
# def func(conn2):
#     while 1:
#         try:
#             msg = conn2.recv()
#             print(msg)
#         except EOFError:
#             print('对方管道已关闭')
#             conn2.close()
#             break
#
# if __name__ == '__main__':
#     conn1,conn2 = Pipe()
#     p = Process(target=func,args=(conn2,))
#     p.start()
#     conn1.send('你好啊')
#     conn1.close()

'''
manager数据共享
进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的，虽然进程间数据独立
但可以通过Manager实现数据共享,事实上Manager的功能不止于此
'''
# from multiprocessing import Process,Manager
#
# def func(m_dic):
#     m_dic['name'] = '大猪蹄子'
#
# if __name__ == '__main__':
#     m = Manager()
#     m_dic = m.dict({'name': '大佬'})
#     print('原始>>>',m_dic)
#
#     p = Process(target=func,args=(m_dic,))
#
#     p.start()
#     p.join()
#     print('主进程>>>>',m_dic)


