from multiprocessing import Process
import time
import os


def func1():
    time.sleep(2)
    print(os.getpid())
    print('子进程')


if __name__ == '__main__':
    p1 = Process(target=func1,)
    p1.start()

    # p1.terminate()  #在关闭进程时，不会立刻关闭，有段缓冲时间
    # time.sleep(1)
    p1.join()
    print('进程是否还在:', p1.is_alive())  #检测进程是否还存活
    print(p1.pid)
    print('主进程结束')


