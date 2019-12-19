#!/usr/bin/env python
# -*- coding: utf-8 -*-

#逻辑顺序调用
# def func1():
#     print("我是func1")
#
# def func2():
#     print("我是func2")
#     func1()
#
# def func3():
#     func2()
#     print("我是func3")
#
# func3()

#函数嵌套
# def outer():
#     def inner():
#         print("我是内部")
#     print("我是外部")   #优先调用外部函数
#     inner()    #再调用内部函数
#
# outer()

#函数嵌套练习
# def outer():
#     print("我是外面的.")
#     def inner_1():
#         print("我是inner1.")
#         def inner_2():
#             print("我是inner2.")
#         inner_2()
#     def inner_3():
#         inner_1()
#         print("我是inner3")
#     inner_3()
# outer()

