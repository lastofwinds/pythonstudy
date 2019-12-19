import time
from multiprocessing import Process
import os


'''进程讲解一'''
# def func1(n):
#     time.sleep(1)
#     print(n)
#
# def func2(n):
#     time.sleep(1)
#     print(n)
#
# def func3(n):
#     time.sleep(1)
#     print(n)
#
# def func4(n):
#     time.sleep(1)
#     print(n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func1,args=(1,))  #创建进程的方式一
#     p2 = Process(target=func2, args=(2,))
#     p3 = Process(target=func3, args=(3,))
#     p4 = Process(target=func4, args=(4,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     print('主进程结束')


'''进程讲解二'''
# class MyProcess(Process):     #创建进程的方式二
#
#     def __init__(self, n,name):
#         super().__init__()
#         self.n = n
#         self.name = name
#
#     def run(self):    #定义一个类继承，必须写一个run方法，使用init函数魔法方法
#         # print(1+1)
#         # print(123)
#         print('子进程的进程ID',os.getpid())
#         print('你看看n>>>',self.n)
#
#
# if __name__ == '__main__':
#     p1 = MyProcess(100,name='子进程1')
#     p1.start()   #给操作系统一个指令，子进程创建好。要执行调用run方法
#
#     print('p1-name', p1.name)
#     print('p1-pid', p1.pid)
#     print('主进程结束')


