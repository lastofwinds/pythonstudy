#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.类变量和实例变量的区别？
# 类变量是某个类(公用)
# 实例变量是调用后生成的实例


# 2.super的作用？


# 3.isinstance() 和 type区别？
# type直接针对数据类型判断
# isinstance 可以判断出对象以及对象的父类

# def func(arg):
#     if callable(arg):
#         return arg()
#     else:
#         print(arg)
# func(3)

# 4.isinstance判断对象类型
# *args动态传参,接收到的是一个元组
# from types import FunctionType,MethodType
# class Foo:
#     pass
#
# class Person:
#     def eat(self):
#         pass
#
# def func(*args):
#     fun_count = 0
#     method_count = 0
#     foo_object = 0
#     for el in args:
#         if isinstance(el,FunctionType):
#             fun_count += 1
#         elif isinstance(el,MethodType):
#             method_count += 1
#         elif type(el) == Foo:
#             foo_object += 1
#         else:
#             print(el)
#     return fun_count,method_count,foo_object
# print(func(Person.eat))  #执行Person.eat寻找实例对象类型，触发isinstance类型判断
#
# a,b,c = func(Person.eat,Person().eat,func,Foo())  #解构
# print(a,b,c)


# 5.如果有以下handle.py文件，请在run.py中补充代码实现：
# 5.1获取handle中所有成员名称: dir(handle)
# 5.2获取handle中名字叫Base的成员
# 5.3检查其他成员是否是Base类的子类(不包含Base),如果是则创建对象并添加到objs列表中

# 见模块内容:
# handle.py
# run.py



