from multiprocessing import Process,Queue
import time

def producer(q):
    for i in range(1,11):
        time.sleep(1)
        print('生产了包子%s'%i)
        q.put(i)

def consumer(q):
    while 1:
        time.sleep(2)   #消费者不一定能立刻消费掉信息,一般给定时间减轻服务器压力
        try:
            s = q.get(False)
            if s == None:
                break
            else:
                print('消费者吃了%s' % s)
        except:
            break

if __name__ == '__main__':
    q = Queue(20)
    pro_p = Process(target=producer,args=(q,))
    pro_p.start()

    con_p = Process(target=consumer, args=(q,))
    con_p.start()
