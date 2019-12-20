#协程：单线程下实现并发

#并发：伪并行，遇到IO就切换，单核下多个任务之间切换执行，在高速切换后
# 基本都是IO操作，所以看起来效率高了


# 并行：多核CPU真正的同时执行
# 串行：一个任务执行完成执行另外一个任务

# 多线程多进程下的任务切换+保存状态是操作系统


# import time
#
# def func1():
#     time.sleep(1)
#     print('func1')
#
# def func2():
#     time.sleep(2)
#     print('func2')
#
# if __name__ == '__main__':
#     func1()
#     func2()

import time

def consumer():
    '''任务1：接收数据，处理数据'''
    while True:
        x = yield
        print('处理了数据:',x)

def producer():
    '''任务2：生产数据'''
    g = consumer()
    next(g)

    for i in range(3):
        g.send(i)
        print('发送了数据:',i)

start = time.time()

# 串行的执行方式
producer()
stop = time.time()
diff = stop - start
print(diff)


