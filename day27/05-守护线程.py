from threading import Thread
import time
from multiprocessing import Lock,Process

def func(n):
    time.sleep(5)
    print(n)


if __name__ == '__main__':
    # t = Thread(target=func,args=('我是子线程',))
    # t.start()

    p = Process(target=func,args=('我是子进程',))
    p.start()
    # print('主进程结束')

    print('主线程结束')

