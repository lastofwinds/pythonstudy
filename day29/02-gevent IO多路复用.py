'''gevent IO多路复用'''

from gevent import monkey
monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(2)
    time.sleep(2)

    print('%s eat 2' % name)

def play(name):
    print('%s play 1' % name)
    # gevent.sleep(2)
    time.sleep(2)
    print('%s play 2' % name)

g1 = gevent.spawn(eat,'egon')  #异步执行这个eat任务，后面egon就是传给他的参数
g2 = gevent.spawn(play,name='egon')

# g1.join()
# g2.join()

gevent.joinall([g1,g2])

print('主')


