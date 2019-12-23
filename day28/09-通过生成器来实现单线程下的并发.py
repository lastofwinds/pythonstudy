
# import time
#
# def consumer():
#     while True:
#         x = yield
#         time.sleep(1)
#         print('处理了数据:',x)
#
# def producer():
#     g = consumer()
#     next(g)
#     for i in range(3):
#         g.send(i)
#         print('发送了数据:',i)
#
# start = time.time()
# producer()
# stop = time.time()

# 串行的执行方式
# res = producer()
# consumer(res)
# stop = time.time()

# diff = stop - start
# print(diff)


# import time
#
# def consumer():
#     for i in range(3):
#         time.sleep(1)
#         print('处理了数据:',i)
#
# def producer():
#     for i in range(3):
#         print('发送了数据:',i)
#
# start = time.time()
# consumer()
# producer()
# stop = time.time()
# print(stop - start)



# import time
#
# def consumer():
#     for i in range(4):
#         x = yield
#         time.sleep(1)
#         print('处理了数据:',i)
#
# def producer():
#     g = consumer()  #调用内含迭代器的函数
#     next(g)  #执行迭代器
#     for i in range(3):
#         g.send(i)
#         print('发送了数据',i)
#
# start = time.time()
# producer()
# stop = time.time()
#
# print(stop - start)


