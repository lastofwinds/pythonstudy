#!/usr/bin/env python
#-*- coding: utf-8 -*-


# python本身就是多态
# class Animals:
#     def eat(self):
#         print("所有动物都会吃...")
#
# class Haski(Animals):
#     def eat(self):
#         print("疯了一样吃...")
#
# class Monkey(Animals):
#     def eat(self):
#         print("龇牙咧嘴吃...")
#
# class Tiger(Animals):
#     def eat(self):
#         print("跟猫一样吃...")
#
# class Siyangyuan():
#     def weiAnimals(self,ani):  #多态性，可扩展性，主要针对某个大类统一的动作处理
#         ani.eat()
#
# syy = Siyangyuan()
#
# hou = Monkey()
# hsq = Haski()
# lh = Tiger()
#
# syy.weiAnimals(hsq)
# syy.weiAnimals(hou)

# 对象访问
# class Car:
#     def run(self,speed):
#         print("the car run %s km/h." % speed)
#
# c = Car()
# c.run(180)  #实例化对象访问内部函数
# Car.run(c,180)  #多一层访问，自己作为参数访问自己+其他参数


