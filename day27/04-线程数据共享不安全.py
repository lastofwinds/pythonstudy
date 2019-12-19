'''锁:解决数据不安全问题'''

from threading import Thread
import time
from multiprocessing import Lock
num = 100

def func(t_lock):
    global num
    # num -= 1
    t_lock.acquire()
    mid = num
    mid = mid - 1

    time.sleep(0.00001)
    num = mid
    t_lock.release()
if __name__ == '__main__':
    t_lock = Lock()  #锁对象，同步锁
    t_lst = []
    for i in range(10):
        t = Thread(target=func,args=(t_lock,))
        t.start()
        t_lst.append(t)
    [tt.join() for tt in t_lst]
    print('主线程>>>',num)



