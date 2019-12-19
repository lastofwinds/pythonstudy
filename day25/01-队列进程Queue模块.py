from multiprocessing import Process,Queue

# 先进先出
q = Queue(3)

q.put(1)
q.put(2)
print(q.full())
q.put(3)


# q.put(4)  #队列超出，put插入数据的时候会阻塞
print(q.full())   #判断队列是否已满

print(q.get())  #队列中第一个放入的数据会最先读到
print(q.get())
print(q.get())

# print('>>>',q.empty())  #判断队列是否为空
# print(q.get())   #队列为空，get取数据时，会阻塞

while 1:
    try:
        q.get(False)
        q.get_nowait()
    except:
        print('队列为空...')
        break


