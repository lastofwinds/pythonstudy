import socket
from threading import Thread

class MyServer():

    '''构造函数,相关参数变量'''
    def __init__(self,ip_port):
        # super().__init__()
        self.ip_port = ip_port
        self.ready()

    '''准备网络编程参数'''
    def ready(self):
        self.socket = socket.socket()
        self.socket.bind(self.ip_port)
        self.socket.listen()
        self.run()

    '''运行服务端允许被连接'''
    def run(self):
        while 1:
            self.conn, self.addr = self.socket.accept()
            self.thread_start(self.conn)

    '''开启多线程功能'''
    def thread_start(self,conn):
        t = Thread(target=self.recv_data, args=(conn,))
        t.start()
        return self.conn

    '''接收数据'''
    def recv_data(self,conn):
        from_client_msg = conn.recv(1024).decode('utf-8')
        print('>>>',from_client_msg)
        conn.send('按住你躁动的小尾巴'.encode('utf-8'))

if __name__ == '__main__':
    ip_port = ('127.0.0.1',8001)
    MyServer(ip_port,)


