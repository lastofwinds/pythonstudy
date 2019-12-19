import json
from multiprocessing import Process,Lock
import time
import random

def get_ticket(i,ticket_lock):
    ticket_lock.acquire()  #锁控制,只有一个人可以拿到，同步效率低，但是保证了数据安全

    with open('ticket','r') as f:
        last_ticket_info = json.load(f)
    last_ticket = last_ticket_info['count']

    if last_ticket > 0:
        time.sleep(random.random())
        last_ticket = last_ticket - 1
        last_ticket_info['count'] = last_ticket
        with open('ticket','w') as f:
            json.dump(last_ticket_info,f)
        print('%s号抢到了, 丫nb!' % i)
    else:
        print('%s号亲,没票啦,明年再来!' % i)

    ticket_lock.release()
if __name__ == '__main__':
    ticket_lock = Lock()
    for i in range(10):
        p = Process(target=get_ticket,args=(i,ticket_lock,))
        p.start()

