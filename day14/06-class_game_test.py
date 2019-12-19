#!/usr/bin/env python
# coding = utf-8
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置:",self.x, self.y)

class Goldfish(Fish):
    pass

class Garp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #引用父类中的子类方法
        #Fish.__init__(self)
        #强引用子类方法
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了,吃不下了...")

fish = Fish()
fish.move()

goldfish = Goldfish()
goldfish.move()

salmon = Salmon()
salmon.move()

shark = Shark()
shark.eat()
shark.move()
