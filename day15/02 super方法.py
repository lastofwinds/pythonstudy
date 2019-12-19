#!/usr/bin/env python
#-*- coding: utf-8 -*-



class Animal:
    def eat(self):
        print("eat.....")

class Cat(Animal):
    def eat(self):   #这个函数会覆盖Animal中的函数，但是下面的super方法可以解决这一问题
        super().eat()    #super方法支持多个同样函数调用
        print("eat fish.....")

c = Cat()
c.eat()


