
'''进程池的作用：并行 并发 同步 异步 阻塞 非阻塞 互斥 死锁'''
# import time
# from multiprocessing import Process,Pool

# def func(n):
#     time.sleep(1)
#     print(n)
#
#
# if __name__ == '__main__':
#     pool = Pool(4)  #设置进程数量，如果不设置，默认是CPU数量
#     pool.map(func,range(100))  #map自带join功能，异步执行任务，参数是可迭代对象



'''在少量进程执行的时候，较小的进程池的性能要比多进程好，性能相对稳定，可根据硬件配置调整进程池数量'''
# import time
# from multiprocessing import Process,Pool
# def func(n):
#     for i in range(100):
#         n += 1
#     print(n)
#
# if __name__ == '__main__':
#     pool_start_time = time.time()
#     pool = Pool()
#     pool.map(func,range(100))
#
#     pool_end_time = time.time()
#     pool_dif_time = pool_end_time - pool_start_time
#
#     lst = []
#     p_s_time = time.time()
#     for i in range(100):
#         p = Process(target=func,args=(i,))
#         p.start()
#
#         lst.append(p)
#     [p.join() for p in lst]
#     p_e_time = time.time()
#
#     pd_time = p_e_time - p_s_time
#
#     print('进程池执行时间>>>',pool_dif_time)
#     print('多进程执行时间>>>',pd_time)



'''在进程较多，进程池较小的时候，多进程效率就比较明显，进程池效率就下降了'''
# import time
# from multiprocessing import Process,Pool
# def func(i):
#     time.sleep(0.5)
#     print(i**2)
#
# if __name__ == '__main__':
#     pool = Pool(4)
#     pool_s_time = time.time()
#     pool.map(func,range(100))
#     pool_e_time = time.time()
#     pool_dif_time = pool_e_time - pool_s_time
#
#     p_lst = []
#     p_s_time = time.time()
#     for i in range(100):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#
#     [p.join() for p in p_lst]
#     p_e_time = time.time()
#     p_dif_time = p_e_time - p_s_time
#
#     print('进程池执行时间:',pool_dif_time)
#     print('多进程运行时间:',p_dif_time)


# 注意：综合以上几点，可以发现进程池与多进程各有优势，多进程遵循语言的底层算法（列表数据执行），
# 进程池则是自定义进程的量进行执行，和硬件性能成正比


'''进程池同步方法: apply'''
# import time
# from multiprocessing import Process,Pool
#
# def func(i):
#     time.sleep(0.5)
#     return i**2
#
# if __name__ == "__main__":
#     p = Pool(4)
#     for i in range(10):
#         res = p.apply(func,args=(i,))  #同步执行的方法，会等待任务的返回结果
#         print(res)
#
#     print('主进程结束')  #等待子进程结束，再输出



'''进程池异步方法: apply_async'''
# import time
# from multiprocessing import Process,Pool
#
# def func(i):
#     time.sleep(0.5)
#     return i**2
#
# if __name__ == "__main__":
#     p = Pool(4)
#     ret_lst = []
#     for i in range(10):
#         res = p.apply_async(func,args=(i,))   #异步执行,res是对象
#         ret_lst.append(res)
#
#     for i in ret_lst:
#         print(i.get())
#
#     print('主进程结束')   #如果没有i.get()方法，则主进程不会等待子进程执行完就会结束



'''如果不加close和join，程序会直接随主进程结束运行，不会等待打印i，加join后可以感知进程的运行'''
# import time
# from multiprocessing import Process,Pool
#
# def func(i):
#     time.sleep(0.5)
#     print(i)
#     return i**2
#
# if __name__ == "__main__":
#     p = Pool(4)
#     res_lst = []
#     for i in range(10):
#         res = p.apply_async(func,args=(i,))
#         res_lst.append(res)
#         # print(res)  # 打印异步的多个对象
#
#     p.close()  #不是关闭进程池，而是不允许其他任务来使用进程池
#     p.join()  #这是感知进程池中任务的方法，等待进程池任务执行完
#
#     for el in res_lst:
#         print('结果>>>',el.get())
#
#     print("主进程结束")



'''回调函数:callback'''
# import os
# from multiprocessing import Process,Pool
#
# def func1(n):
#     print('func1',os.getpid())
#     return n*n
#
# def func2(nn):
#     print('func2',os.getpid())
#     print(nn)
#
# if __name__ == "__main__":
#     print("主进程:",os.getpid())
#     p = Pool(4)
#     p.apply_async(func1,args=(10,),callback=func2)  #将func1的返回结果传参给func2,func2在主进程进行，如果func1是以多个参数传递过去，传给func2的就是一个元组
#     p.close()
#     p.join()


