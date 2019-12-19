from multiprocessing import Process,Semaphore,Event

import time,random

# e = Event() #创建一个时间对象
# print(e.is_set())  #is_set查看一个事件的状态,默认为False,可以通过set方法改为True
#
# print('look here!')
#
# # e.set() #将is_set()状态改为True
# # print(e.is_set()) #is_set 查看一个事件状态....
# # e.clear() 将is_set状态改为False(清除前面设置的状态，回归初始状态)
# # print(e.is_set()) #is_set 查看一个事件的状态...
#
# # e.wait() #根据is_set状态结果决定是否在这阻塞,is_set() = False就阻塞,is_set() = True不阻塞
# print('give me!')

'''进程池由来的原因'''

# 原因一：程序实际处理过程中，忙时会有成千上万的任务，闲时任务很少，在给定进程池后，任务少则在进程池中，
# 取出对应进程进行处理，任务多时一样，但是在进程池空间进程不够时，只能让前面的进程执行完放入进程池，
# 后面的进程才能执行，这样降低了操作系统的调度难度
#
# 原因二：在成千上万进程出现时，难道我们要去创建上万进程吗？创建进程需要消耗时间，销毁进程也需要消耗时间，
# 这是操作系统和硬件无法接受的，也不会支持这无上限的进程执行


'''通过Event完成红绿灯'''

def traffic_lights(e):
    while 1:
        print('红灯啦')
        time.sleep(5)
        e.set()

        print('绿灯亮了,走起')
        time.sleep(3)
        e.clear()

def car(i,e):
    if not e.is_set():  #新来的车查看状态是红灯
        print('我们在等待')
        e.wait()
        print('走起')
    else:
        print('终于可以走了')

if __name__ == '__main__':
    e = Event()

    hld = Process(target=traffic_lights,args=(e,))
    hld.start()

    while 1:
        time.sleep(0.5)
        #创建10个车
        for i in range(10):
            time.sleep(random.randrange(1,3))
            p1 = Process(target=car,args=(i,e,))
            p1.start()




