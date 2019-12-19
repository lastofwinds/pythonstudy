import time
from multiprocessing import Process
from threading import Thread

def func(n):
    num = 0
    for nl in range(n):
        num += nl
    print('num',num)


if __name__ == '__main__':
    t_s_time = time.time()
    t_lst = []
    for i in range(10):
        t = Thread(target=func,args=(10,))
        t.start()
        t_lst.append(t)
    [tt.join() for tt in t_lst]

    t_e_time = time.time()
    t_dif_time = t_e_time - t_s_time


    p_s_time = time.time()
    p_lst = []
    for x in range(10):
        p = Process(target=func,args=(10,))
        p.start()
        p_lst.append(p)
    [pp.join() for pp in p_lst]
    p_e_time = time.time()
    p_dif_time = p_e_time - p_s_time

    print('线程>>>>',t_dif_time)
    print('进程>>>>',p_dif_time)
    print('主线程结束')


