#!/usr/bin/env python
# -*- coding: utf-8 -*-


#生成器
# 1.生成器
# 2.生成器函数
# 3.生成器表达式

# def goods():
#     lst = []
#     for i in range(1000):
#         lst.append("衣服%s" % i)
#     return lst
#
# li1 = goods()
# print(li1)

#生成器本质是迭代器
# def func():
#     print("linux is very good.")
#     return "bingo."
# ret = func()
# print(ret)    #这里会返回return值
#
# def func1():
#     print("python is very good.")
#     yield "bingo."   # return换成yield,执行生成器函数的时候返回生成器，而不是执行这个函数
# ret1 = func1()
# print(ret1)     #yield语句会返回函数内存地址，给你的是一个生成器
#
# ret1.__next__()  #在生成器后使用__next__才开始执行函数
# ret1.__next__()

# 例如：
# def func():
#     print("打开手机")
#     print("打开陌陌")
#     print("打开微信")
#     yield "手机"
#     print("约妹纸")
#     print("出来喝茶")
#     print("出来吃饭")
#     yield "电脑"
#
#
# ret = func()
# ret.__next__()   #在生成器中可以使用yield语句进行分段处理,找不到最后的yield会报错，所以yield要放在函数尾部
# ret.__next__()
# ret.__next__()

#生成器优点:1.节省内存，2.惰性机制，3.只能往前走
#
# def func():
#     print("1")
#     a = yield "1.1"
#     print("2",a)
#     b = yield "2.1"
#     print("3",b)
#     yield "4"
#
# gen = func()
# ret = gen.__next__()
# print(ret)
# ret = gen.send("3.2")   #往上一个yield生成器中传值
# print(ret)   #a变量是yield时，在前面被执行掉，后面就会抛出none


# send()和__next__()的区别
# send不可以用在开头
# send可以给上一个yield传值，并且不能给最后一个yield传值


# def func():
#     yield "李彦宏"
#     yield "马化腾"
#     yield "马云"
#
# gen = func()
# print("__iter__" in dir(gen))
#
# # for el in gen:
# #     print(el)
#
# lst = list(gen)  #把生成器中的数据拿出来组合成一个列表
# print(lst)


#生成器表达式
# def add(a,b):
#     return a + b
#
# def test():
#     for r_i in range(4):
#         yield r_i
#
# g = test() #惰性机制会返回一个生成器
#
# # for n in [2,10]:
# #     g = (add(n,i) for i in g)  #循环的内部也是一个生成器
#
# n = 2
# g = (add(n,i) for i in (add(n,i) for i in g))
# print(list(g))