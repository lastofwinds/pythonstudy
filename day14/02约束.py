#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
    约束
        在类继承时，继承后的类有一个书写标准，
        就是按照父类给出的模子去写，如果不是这个标准就抛出异常。
'''

'''约束一：通过抛异常'''
# class Base:
#     def login(self):
#         raise NotImplementedError("没有实现login方法")
#
#     def kantie(self):
#         raise NotImplementedError("没有实现看帖功能")
#
#
# class Normal(Base):
#     def login(self):
#         print("普通人登录")
#
# class Member(Base):
#     def denglu(self):
#         print("吧务登录")
#
# class Admin(Base):
#     def login(self):
#         print("管理员登录")
#
#
# l1 = Normal()
# l2 = Member()
# l3 = Admin()
#
# l1.login()
# l2.login()
# l3.login()


'''异常二：抽象类'''
# from abc import ABCMeta,abstractmethod
# class Animal(metaclass=ABCMeta):  #在父类中写出metaclass=xxx,抽象类，类中存在抽象方法，类一定是抽象类
#     @abstractmethod  #抽象方法
#     def eat(self):  #抽象概念
#         pass
#
# class Cat(Animal):
#     def eat(self):  #具体实现
#         print("猫吃鱼...")
#
#
# e1 = Cat()
# e1.eat()


'''
from abc import ABCMeta,abstractmethod  #导入模块
    抽象类方法
        抽象方法：不用给出方法，写个pass即可
        抽象类： 
            语法：类(metaclass=ABCMeta)
            概念：如果类中包含了抽象方法，这个类一定是抽象类
            特点：抽象类一般不创建对象，抽象类中可以存在正常方法
'''


