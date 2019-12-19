from multiprocessing import Process
import time

#
# def func1():
#     time.sleep(2)
#     global global_num
#     global_num = 0
#     print('子进程全局变量>>>', global_num)
#
# if __name__ == '__main__':
#     p1 = Process(target=func1,)
#     p1.start()
#     # time.sleep(3)
#     print('子进程执行')
#     p1.join()  #阻塞住,等待p1子进程执行结束,主进程的程序才能从这里继续往下执行
#     print('主进程的全局变量', global_num)


# def func1(n):
#     time.sleep(n)
#     print('func1',n)
#
# def func2(n):
#     time.sleep(n)
#     print('func2',n)
#
# def func3(n):
#     time.sleep(n)
#     print('func3',n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func1, args=(1,))
#     p2 = Process(target=func2, args=(2,))
#     p3 = Process(target=func3, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()



def func1(n):
    print(n)

if __name__ == '__main__':
    pro_list = []
    for i in range(10):
        p1 = Process(target=func1,args=(i,))
        p1.start()

        pro_list.append(p1)
        # p1.join()

    for p in pro_list:
        p.join()  #设置join后阻塞，主进程会等待p1进程执行完，才会执行

    print('主进程结束')

