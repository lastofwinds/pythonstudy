'''线程池与进程池效率对比，线程池效率高很多'''

'''回调函数'''
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread
import time

def func1(n):
    # time.sleep(1)
    print(n,current_thread().ident)
    return n**2

def func2(n):
    print('>>>>>',n)
    print('>>>>>',n.result())
    print('current_thread>>>',current_thread().getName())


if __name__ == '__main__':
    t_p = ThreadPoolExecutor(max_workers=10)
    # t_p = ProcessPoolExecutor(max_workers=10)
    t_p.submit(func1,2).add_done_callback(func2)  #回调func2

    t_res_lst = []

    for i in range(100):
        res_obj = t_p.submit(func1,i)
        t_res_lst.append(res_obj)
    # t_p.submit(func,'changxiong')
    # map_res = t_p.map(func,range(10))   #map映射异步执行

    # t_p.shutdown()
    # print('t_res_lst',t_res_lst)
    for e_res in t_res_lst:
        print(e_res.result())

