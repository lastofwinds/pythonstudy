#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            from_client_data = self.request.recv(1024).decode('utf-8')

        # self.request   #conn链接通道

            print(from_client_data)
            server_input = input('xiaoming: ')

            self.request.send(server_input.encode('utf-8'))
            # self.request.close()

if __name__ == "__main__":
    ip_port = ('127.0.0.1', 8080)

    socketserver.TCPServer.allow_reuse_address = True

    server = socketserver.ThreadingTCPServer(ip_port,MyServer)
    server.serve_forever()







