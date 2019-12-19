#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 继承，多重继承
# class Foo:
#     def func(self):
#         print("father...")
#
# class Foo2:
#     def requestMoney(self):
#         print("i need money...")
#
#     def play(self):
#         print("Foo2中的play")
#
# class Bar(Foo,Foo2): #继承+继承多个父类,MRO算法，C3算法
#     pass
#
# obj = Bar()
# obj.func()   #子类调用父类，因为继承了父类功能
# obj.requestMoney() #子类调用父类
# obj.play()


# 抽象宠物通用功能用于继承
# class Pet:
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print("%s eat..." % self.name)
#
#     def sleep(self):
#         print("%s sleep..." % self.name)
#
# class Cat(Pet):
#     def catchMouse(self):
#         print("%s like catch the mouse..." % self.name)
#
# class Dog(Pet):
#     def dismantling(self):
#         print("%s can dismantling things..." % self.name)
#
# c = Cat('tom')
# c.eat()
# c.sleep()
# c.catchMouse()
#
# d = Dog('peter')
# d.eat()
# d.sleep()
# d.dismantling()





