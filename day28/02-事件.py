'''
    线程的一个关键特性是每个线程都是独立运行且状态不可预测，如果程序中的其他线程需要通过
判断某个线程的状态来确定自己下一步的操作，这是线程同步就变得很棘手，为了解决这些问题，我们
需要使用threading库中的Event对象，对象包含一个可由线程设置的信号标志，它允许线程等待某些事件
发生，在初始情况下，Event对象中的信号标志被设置为假，如果有线程等待一个Event对象，而Event
对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真，一个线程如果将一个Event对象的信号
标志设置为真，它唤醒所有等待这个Event对象的线程，如果一个线程等待一个已经设置为真的Event对象，
那么它将忽略这个事件，继续执行
'''


# 事件的基本方法

# event.isSet(): 返回event状态值
# event.wait(): 如果event.isSet() = False将阻塞线程
# event.set(): 如果event的状态值为True 所有阻塞池线程激活进入就绪状态，等待操作系统调度
# event.clear(): 恢复event状态值为False

from threading import Thread,Event

e = Event()

e.set()
print('在这里等待')
e.wait()
print('还没好')


