'''线程池与进程池效率对比，线程池效率高很多'''

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread
import time

def func(n):
    # print(n)
    # time.sleep(1)
    print(n,current_thread().ident)
    return n**2

if __name__ == '__main__':
    t_s_time = time.time()
    t_p = ThreadPoolExecutor(max_workers=50)
    # t_p = ProcessPoolExecutor(max_workers=50)
    # t_p.submit(func,1)

    t_res_lst = []

    for i in range(10000):
        res_obj = t_p.submit(func,i)
        t_res_lst.append(res_obj)
    # t_p.submit(func,'changxiong')
    # map_res = t_p.map(func,range(10))   #map映射异步执行

    # print(map_res)
    # for i in map_res:
    #     print(i)

    t_p.shutdown()
    print('t_res_lst',t_res_lst)
    for e_res in t_res_lst:
        print(e_res.result())
    t_e_time = time.time()

    t_dif_time = t_e_time - t_s_time
    print(t_dif_time)



