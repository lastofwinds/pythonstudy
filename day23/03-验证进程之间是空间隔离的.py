from multiprocessing import Process
import time

'''进程之间空间是隔离的,不共享资源'''
global_num = 100
#
# def func1():
#     global global_num
#     global_num = 0
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func1,)
#     p1.start()
#
#     time.sleep(1)
#     print('主进程的全局变量>>>',global_num)


def func1():
    time.sleep(2)
    global global_num
    global_num = 0
    print('子进程全局变量>>>', global_num)

if __name__ == '__main__':
    p1 = Process(target=func1,)
    p1.start()
    # time.sleep(3)
    p1.join()
    print('主进程的全局变量', global_num)


