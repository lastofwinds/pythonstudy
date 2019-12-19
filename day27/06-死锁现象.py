'''死锁：线程互调，如果不就会形成一个等待循环

f1 拿到a锁释放a锁，f2拿到了a锁，
f2拿到b锁释放b锁，f1拿到b锁
但是又碰到f2拿到a锁，f1等待f2释放a锁，
f1拿到b锁，f2等待f1释放b锁，就这样和谐的等待，陷入死锁

不过使用join()方法可以解决线程阻塞问题
'''


from threading import Thread,Lock
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
    lockA = Lock()
    lockB = Lock()

    t1 = MyThread(lockA,lockB)
    t1.start()

    t2 = MyThread(lockA,lockB)
    t2.start()

    print('我是master')

