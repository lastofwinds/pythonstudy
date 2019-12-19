'''
使用RLock方法递归锁
'''


from threading import Thread,Lock,RLock #递归锁
import time

class MyThread(Thread):
    def __init__(self,lockA,lockB):
        super().__init__()
        self.lockA = lockA
        self.lockB = lockB

    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        self.lockA.acquire()
        print('我拿了A锁')

        self.lockB.acquire()
        print('我是f1')
        self.lockB.release()
        self.lockA.release()


    def f2(self):
        self.lockB.acquire()

        time.sleep(0.5)
        print('我拿了B锁')

        self.lockA.acquire()
        print('我是f2')
        self.lockA.release()
        self.lockB.release()


if __name__ == '__main__':
    # lockA = Lock()
    # lockB = Lock()

    # lockA = lockB = Lock()
    lockA = lockB = RLock()
    t1 = MyThread(lockA,lockB)
    t1.start()

    t2 = MyThread(lockA,lockB)
    t2.start()

    print('我是master')

