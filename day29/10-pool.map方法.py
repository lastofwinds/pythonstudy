'''
    Pool.map:
        都是multiprocessing模块中方法，相较多线程，多进程，使用map代码更简单，map也是调用其它模块完成任务
'''


from multiprocessing import Pool
from time import sleep

class Formap:
    def __init__(self):
        self.name = "未命名"

    def forSquare(self,i):
        sleep(i)
        return i ** 2    #return返回值

if __name__ == '__main__':
    classformap = Formap()
    p = Pool(2)

    lst = [2,4,6]
    rLst = p.map(classformap.forSquare, lst)

    print(rLst)    #返回值会进入列表

    p.close()
    p.join()

