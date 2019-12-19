from multiprocessing import Process,Queue
import time


def girl(q):
    print('来自boy的信息', q.get())
    print('来自校领导的凝视',q.get())

def boy(q):
    q.put('约吗?')


if __name__ == '__main__':
    q = Queue(5)


    boy_p = Process(target=boy, args=(q,))
    girl_p = Process(target=girl, args=(q,))
    boy_p.start()
    girl_p.start()

    time.sleep(0.5)
    q.put("好好工作,别乱搞.")

