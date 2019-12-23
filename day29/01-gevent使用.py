
# 并发执行的效率(在没有IO的情况下，两个纯计算的任务)
import time
from threading import Thread,current_thread

# def func1():
#     num2 = 0
#     for i in range(1000001):
#         num2 += i
#         yield
#         # print('执行到下一个yield', current_thread().name)
#
# def func2():
#     g = func1()
#     next(g)
#     sum = 0
#     for i in range(1000000):
#         sum += i
#         next(g)
#
# s_t = time.time()
# func2()
# print('协程的时间',time.time() - s_t)



# 串行执行的效率
# def func1():
#     num2 = 0
#     for i in range(1000001):
#         num2 += i
#
# def func2():
#     sum = 0
#     for i in range(1000000):
#         sum = sum + i
#
# s_t = time.time()
# func1()
# func2()
# print('串行的时间',time.time() - s_t)
