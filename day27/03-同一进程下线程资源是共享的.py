import time
from multiprocessing import Process
from threading import Thread


num = 100
def func():
    global num
    num = 0

if __name__ == '__main__':
    t = Thread(target=func,)
    t.start()
    t.join()
    print(num)
