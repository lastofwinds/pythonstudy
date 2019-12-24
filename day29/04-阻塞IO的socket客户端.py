import socket
import time

ip_port = ('127.0.0.1',8083)


client = socket.socket()
client.connect(ip_port)


while 1:
    client.send(b'dayangge henweisuo')
    time.sleep(0.1)

