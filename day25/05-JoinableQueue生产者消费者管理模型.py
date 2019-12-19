from multiprocessing import Process,Queue,JoinableQueue
import time

'''JoinableQueue进程队列'''
def producer(q):
    for i in range(1,11):
        time.sleep(0.5)
        print('生产了包子%s'%i)
        q.put(i)
    q.join()    #阻塞等待
    print('等待')

def consumer(q):
    while 1:
        time.sleep(1)
        s = q.get()

        print('消费者吃了%s' % s)
        q.task_done()

if __name__ == '__main__':
    #通过队列来模拟缓冲区,大小设置为20
    q = JoinableQueue(20)
    #生产者进程
    pro_p = Process(target=producer, args=(q,))
    pro_p.start()

    #消费者进程
    con_p = Process(target=consumer, args=(q,))
    con_p.daemon = True
    con_p.start()

    pro_p.join()

    print('主进程结束')

