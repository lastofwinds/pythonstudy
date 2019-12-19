#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 对象成员
# 1.变量
# 2.方法
# 3.属性


# class Person:
#     country = "中国"
#     def __init__(self,name,num,gender,birthday):
#         # 成员变量
#         self.name = name
#         self.num = num
#         self.gender = gender
#         self.birthday = birthday
#
#     # 对象来访问(成员方法)(实例方法)
#     def marray(self,duifang):
#         print("人会结婚%s" % duifang)
#     # 类中所有的成员都是方法
#
# alex = Person('alex',10086,'man',19780709)
# alex.country = '澳大利亚'  #修改alex country，也就是单独给alex赋予这个变量
# wusir = Person('wusir',10010,'man',19780710)
# print(alex.country)  #通用国家,可位于主类中
# print(wusir.country)


# 方法
# 1.成员方法  加了self的，调用时必须用对象去访问
# 2.类方法  当方法需要传递类名的时候，需要类方法，规范用法在上方加上装饰器@classmethod
# 3.静态方法  当你的方法不需要传递当前类的对象的时候，语法规则就是在方法上面加@staticmethod


# class Person:
#     def __init__(self):
#         pass
#
#     '''实例方法需要传递类对象'''
#     def think(self):
#         print("思考.")
#
#     '''静态方法'''
#     @staticmethod
#     def count(a,b):
#         print("计算...")
#         return a + b
#
#     '''类方法,第一个参数传递的是类名'''
#     @classmethod
#     def clsMethod(cls):
#         print(cls)  #打出类型
#         p = cls()  #创建一个动态对象
#         print("我是类方法")

# p = Person()
# p.think()
#
# Person.think(p)  #此处关于带有self的函数，调用时必须调用自身对象
#
# # 静态方法调用
# c = Person.count(1,2)
# print(c)
#
# # 静态内容用类名访问

# Person.clsMethod()


# 属性
# 用方法来描述我们的属性信息
# import datetime
# class Person:
#     def __init__(self,name,num,gender,birthYear):
#         self.name = name
#         self.num = num
#         self.gender = gender
#         self.birthYear = birthYear
#
#     '''当前方法是一个属性，方法的返回值是这个属性的值，方法必须要有返回值'''
#     @property
#     def age(self):
#         return datetime.datetime.now().year - self.birthYear
#
# p = Person('alex',10086,'未知',1989)
# print(p.age)  #可以直接返回属性，实际上访问的是age()方法，返回值就是属性值


# 私有
# class Tiger:
#     def __init__(self,name,waibiao,zuofeng,qingfu,money,fangchan):
#         self.name = name
#         self.waibiao = waibiao
#         self.zuofeng = zuofeng
#         '''私有: 变量前用双下划线时'''
#         self.__qingfu = qingfu
#         self.__money = money
#         self.__fangchan = fangchan
#
#     def buy(self):
#         print("我有%s" % self.__money)
#         self.__sel()
#
#     '''私有属性不可以访问,只能使用内部实例函数代理'''
#     def __sel(self):
#         print("我要卖掉%s套房" % self.__fangchan)
#
#
# lh = Tiger('alex','正直','刚正不阿','小潘潘',1000000,5)
# print(lh.name)
# print(lh.zuofeng)
#
# lh.buy()


# 在python中__开头的，表示私有
# __方法
# __变量
# __类变量



