'''信号量：控制同时能够进入锁内去执行代码的线程数量，维护了一个计数器，
刚开始创建信号量时候假如设置4个房间，进入一次acquire就减一，出来一个就
+1，如果计数器为0，那么其他任务等待。这样其他的任务和正在执行的任务是一个
同步的状态，而进入acquire里面去执行的那4个任务是异步执行的
'''


from threading import Thread, Semaphore
import time

def func1(s):
    s.acquire()
    time.sleep(2)

    print('大保健')
    s.release()

if __name__ == '__main__':
    s = Semaphore(4)
    for i in range(10):
        t = Thread(target=func1,args=(s,))
        t.start()




