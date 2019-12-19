from multiprocessing import Process
import os


def func1():
    print('子进程',os.getpid())
    print('子进程的父进程',os.getpid())
    print(123)


if __name__ == '__main__':
    print('准备开始其他进程了.')
    print('主进程的父进程ID号>>>',os.getpid())
    print('主进程ID号>>>', os.getpid())

    p1 = Process(target=func1,)
    p1.start()

    print('到这里结束.')
