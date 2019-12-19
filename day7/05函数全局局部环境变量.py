#!/usr/bin/env python
# -*- coding: utf-8 -*-

#global全局环境变量设置
# a = 10
# def func():
#     global a   #设置全局环境变量，将函数内部变量设置为全局
#     a = 20   #所有的a都是外面的了
#     print(a)  #现在只有看的权利
#
# print(a)
# func()
# print(a)


#nolocal找局部变量，离他最近的上层变量
# def func():
#     def func0():
#         a = 50
#         def func1():
#             nonlocal a
#             a = 60
#             print("我是func1:",a)
#             def func2():
#                 a = 70
#                 print("我是func2:",a)
#             func2()
#         print("我是func0:",a)
#         func1()
#         print("我是func0:", a)
#     func0()
# func()


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s" % (i,j,i*j),end='\t')
#     print()

