from threading import Thread
import threading
from multiprocessing import Process
import os


def work():
    import time
    time.sleep(3)
    print(threading.current_thread().getName())


if __name__ == '__main__':
    t = Thread(target=work)
    t.start()

    print(threading.current_thread())
    print(threading.current_thread().getName())
    print(threading.current_thread().ident)
    print(threading.get_ident())
    print(threading.active_count())
    print(threading.enumerate())

    print('主线程/主进程')
