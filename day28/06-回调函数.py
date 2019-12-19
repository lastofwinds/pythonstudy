'''回调函数'''


from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread
import time

def func1(n):
    time.sleep(1)
    # print(n,current_thread().ident)
    return n**2

def func2(n):
    print('>>>>',n.result())
    print('current_thread>>>>',current_thread().getName())

if __name__ == '__main__':
    t_p = ProcessPoolExecutor(max_workers = 4)
    t_p.submit(func1,2).add_done_callback(func2)

    print('主线程结束')



