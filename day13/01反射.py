#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.issubclass type isinstance
# 2.如何分辨方法和函数
# 3.反射

'''issubclass子类判断，issubclass可以递归判断出子类继承'''
# class Animal:
#     pass
# class Cat(Animal):
#     pass
# class BosCat(Cat):
#     pass
#
# print(issubclass(Cat,Animal))
# print(issubclass(BosCat,Cat))
# print(issubclass(BosCat,Animal))


'''type直接给出对象的类'''
# def add(a,b):
#     if (type(a) == int or float) and (type(b) == int or float):
#         return a + b
#     else:
#         print("Format error...type must be int...")


'''isinstance判断对象是什么类型的,只能判断自己对应的类，可以判断出对象的父类，无法判断出子类'''
# class Animal:
#     pass
# class Cat(Animal):
#     pass
# class BosCat(Cat):
#     pass
#
# a = Animal()
# print(isinstance(a,Animal))
# print(isinstance(a,Cat)) #不能判断子类


'''如果需要用程序来判断，需要用到FunctionType,MethodType'''
# class Foo:
#     def run(self):
#         print("在运行...")
#
#     def class_method(cls):
#         pass
#
#     def age(self):
#         return 10
#
#
# from types import FunctionType,MethodType
# def func(arg):
#     print(isinstance(arg,FunctionType))
#     print(isinstance(arg,MethodType))

# func(Foo.class_method)
# func(Foo.age)


# 反射练习
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print("人喜欢吃东西%s ..." % self.name)
#
# p = Person('刘伟')
#
# eat = getattr(p,'eat')  #反射用法：获取函数功能，传入参数
# func = getattr(Person,'eat') #这个获取的是对象中的eat函数
# eat()
# func(p)




