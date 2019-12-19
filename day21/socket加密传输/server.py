import socketserver   #对socket进行封装
import os

class MyTcp(socketserver.BaseRequestHandler):  #定义处理类，继承于BaseRequestHandler
    def handle(self):                          #与所有客户端交互在handle中完成 重写此函数
        while True:
            try:
                self.data = self.request.recv(1024).strip()  #接收消息
                print(self.client_address[0], "write") #显示用户IP
                print(self.data)                    #打印传输数据

                if not self.data:
                    self.request.send(self.data.upper())  #返回大写

            except ConnectionRefusedError as e:   #抓住异常抛出
                print('error', e)
                break

host,port = "localhost",999             #初始化服务端socket(ip.port)

server = socketserver.ThreadingTCPServer((host, port), MyTcp)   #多线程实例化 一个server对象
server.serve_forever()      #处理请求永远执行

server.close()

