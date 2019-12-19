#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1.写一个函数，传入函数中多个实参（均为可迭代对象如字符串，列表，元组，集合等）
#将每个实参的每个元素依次添加到函数的动态参数args里
#例：传入函数两个参数[1,2,3](22,33)最终args为(1,2,3,22,33)

# lst = [1,2,3]
# tun = (22,33)
#
# def func(*args):
#     lst1 = []
#     for i in args:
#         for n in i:
#             lst1.append(n)
#     tu = tuple(lst1)
#     print(tu)
#
# func(lst,tun)


#2.写函数，传入函数中多个实参(实参均为字典)，将每个实参的键值对依次添加到函数的动态参数
# kwargs里面，例如
# 传入函数两个参数{'name': 'alex'} {'age': 1000}最终kwargs为{'name': 'alex','age': 1000}

# def func(**kwargs):
#     print(kwargs)
# func(name='alex',age=1000)   #指定变量写法
# func(**{'name': 'alex','age':'1000'})   #键值对写法


#3.写函数接受两个数字参数，将较小的数字返回
#方式一
# a = 10
# b = 20
# def func(*args):
#     return a if a < b else b
#
# print(func(b,a))

#方式二
# def func(a,b):
#     return a if a < b else b
# print(func(10,20))


#4.写函数，接收一个参数
# (此参数类型必须是可迭代对象的每个元素以'_'连接，形成新的字符串，并返回)
#例如传入一个可迭代对象为[1,'老男孩'，'武sir']返回的结果为 '1_老男孩_武sir'
# lst = ['linux','老男孩','武sir']  #字符串拼接，可以使用join
# string = "_"
# def func(*args):
#     newstr = ""
#     for i in args:
#         newstr = string.join(i)
#     print(newstr)
# func(lst)

# lst = ['linux','老男孩','武sir']
# def func(the):
#     return "_".join(the)
# print(func(lst))

# lst = [1,'老男孩','武sir']  #数字转化成字符串后，才可以拼接
# def func(the):
#     result = ""
#     for el in the:
#         result += str(el) + "_"
#     return result[:-1]
#
# print(func(lst))

# lst = [1,'老男孩','武sir']
# def func(the):
#     for i in range(len(the)):
#         el = str(the[i])
#         the[i] = el
#
#     return "_".join(the)
# print(func(lst))


