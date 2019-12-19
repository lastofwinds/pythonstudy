from multiprocessing import Process,Semaphore
import time
import random


'''异步执行会将多进程随机分配到不同空间(每个空间的进程数不确定)，乱序执行'''
def dbj(i,s):
    s.acquire()
    print('%s 号来洗脚' %i)
    time.sleep(random.randrange(1,3))
    s.release()

if __name__ == '__main__':
    s = Semaphore(4)   #创建一个计数器,每次acquire就减一，直到0,那么上面的任务只有4个在异步执行,后面的进程需要等待
    for i in range(10):
        p1 = Process(target=dbj,args=(i,s,))
        p1.start()


