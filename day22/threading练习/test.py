import threading


# def fun(n):
#     print('>>>>',n)
#
# if __name__ == '__main__':
#     t = threading.Thread(target=fun,args=(13,))
#     t.start()
#     print('程序结束')


import time
def work(number):
    print('worker')
    time.sleep(number)
    return

for i in range(11):
    t = threading.Thread(target=work,args=(i,))
    t.start()
