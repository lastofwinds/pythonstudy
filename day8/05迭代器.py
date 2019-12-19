#!/usr/bin/env python
# -*- coding: utf-8 -*-


#迭代器
# iterable可迭代的数据类型: str,list,tuple,dict,set,open(),range()
# dir() 可以查看某数据类型中可以执行的方法
# s = "alex"
# print(dir(s))  在字符串中发现__iter__没有__next__
# a = 123
# print(dir(a))   在int中没有__iter__没有__next__,不可迭代对象
# lst = [1,2,3]
# print(dir(lst))   在字符串中发现__iter__没有__next__

#判断一个文件是否为可迭代对象
# f = open("./file/peoplelist",mode="r",encoding="utf-8")
# print("__iter__" in dir(f))
#
# 返回True

# lst = [1,2,3]
# it = lst.__iter__()  #iterator迭代器
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())  #当迭代对象遍历完，继续迭代会报错

# lst = [1,2,3,4,5,6]
# it = lst.__iter__()  #调用迭代功能
#
# while True:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         print("it's over.")
#         break
#
# for i in lst:
#     print(i)
# else:
#     print("it's over.")

