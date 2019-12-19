#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''try基本语法'''
# try:
#     raise 抛出异常
# except 异常类 as e:
#     异常的处理
# except 异常类 as e:
#     异常的处理
# else:
#     如果上面的代码没有错误，执行这里的代码
# finally:
#     收尾


# try 处理异常
'''异常一：0不能作为除数测试'''
# def exceptsum(a,b):
#     try:
#         ret = a/b
#         return ret
#     except ZeroDivisionError as e:  #计算异常
#         print(e)
#         print("出错了,0不能是除数...")
#     except FileNotFoundError as e:  #文件异常捕捉
#         print(e)
#         print("出错了,文件找不到...")
#     except StopIteration as e:  #循环体中异常捕捉
#         print(e)
#         print("出错了,0不能是除数...")
#     except Exception as e:    #所有异常的父类，可以捕获所有异常
#         print(e)
#         print("出错了.0不能是除数")
#
# ret = exceptsum(1,0)
# print(ret)


# raise 抛出异常
'''异常二: 计算两个整数的加法'''
# def add(a,b):
#     if type(a) != int or type(b) != int:
#         raise TypeError("我这里只要int,不要别的类型")
#     return a + b
#
# add(333,"abc")

'''异常三: 自定义异常'''
# class GenderError(Exception):
#     pass
#
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
# def man_bathhouse(per):
#     if per.gender != "man":
#         raise GenderError("这里是男澡堂...")
#     else:
#         pass
#
# # p1 = Person("alex","不详")
# p2 = Person("ben","man")
# # man_bathhouse(p1)
#
# man_bathhouse(p2)




