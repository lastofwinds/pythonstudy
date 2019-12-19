'''线程和进程很像，一个进程最少有一个线程，进程是资源层面的，线程负责实际的操作，可以理解为进程的子集'''


# 线程创建方式一
# import time
# from threading import Thread
#
# def func(n):
#     time.sleep(1)  #子线程运行太快了，如果不加time.sleep，会在打印前就跑完
#     print(123)
#
# if __name__ == "__main__":
#     t = Thread(target=func,args=(1,))
#     t.start()
#     t.join()   #阻塞，等待子线程跑完再执行主线程下面的内容
#     print('主进程')


# 线程创建方式二
# from threading import Thread
#
# class MyThread(Thread):
#     def __init__(self,n):
#         super().__init__()
#         self.n = n
#
#     def run(self):
#         print('换汤不换药')
#         print('self.n>>>',self.n)
#
# if __name__ == "__main__":
#     t = MyThread('你好')
#     t.start()
#     t.join()
#     print('主进程结束')



