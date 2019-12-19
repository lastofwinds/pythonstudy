import queue

q = queue.LifoQueue() #先进先出的是队列
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())

