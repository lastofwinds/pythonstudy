#!/usr/bin/env python
# -*- coding: utf-8 -*-


#闭包
#全局变量可能会被修改,全局变量是不安全的,可能会被其他函数所更改
# a = 10
# def func():
#     global a  #会修改全局变量
#     a = 20
#     print(a)
#
# func()   #如果优先执行，会修改掉全局变量，导致全局变量a的值变为函数内部a的值
# print(a)


#在外层变量中声明一个变量，在内层函数使用或者返回这个变量
#闭包
# 1.可以保护变量
# 2.可以让变量常驻内存
# def outer():
#     a = 10
#     def inner():
#         print(a)
#
#     return inner
# ret = outer()
# ret()
#
# print(ret.__closure__)


#闭包练习
# from urllib.request import urlopen
#
# def func():
#     content = urlopen("http://www.xiaohuar.com/").read()
#     def inner():   #闭包可以大大提高执行效率，但相应会常驻内存（下次执行会更快），占用内存资源
#         return content
#     return inner()
# print(func())

#如果在拿视频文件时，需要加入写的方法，for line in filename，迭代写入比较好，视频文件一般比较大

