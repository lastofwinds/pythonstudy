#!/usr/bin/env python
#-*- coding: utf-8 -*-


# pickle 就是把python对象写入到文件中的一种解决方案，但是写入到文件的是bytes，所以这东西不是给人看的，是机器识别的

# 1.dumps 序列还，把对象转换成bytes
# 2.loads 反序列化，把bytes转换成对象
# 3.dump  序列化，把对象转换成bytes并写入文件
# 4.load  反序列化，读取文件中bytes，转换成对象


import pickle

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def catchMouse(self):
        print(self.name,self.age,"抓老鼠")
#
#
# c = Cat("jerry", 18)
# c.catchMouse()
#
#
# # dumps把对象转换成bytes  #序列化（二进制）
# bs = pickle.dumps(c)
# print(bs)
#
#
#
# # loads把bytes转换成对象  #反序列化（对象）
# ccc = pickle.loads(bs)
# ccc.catchMouse()


#
# dic = {"jay": "周杰伦", "jj": "林俊杰"}
#
# bs = pickle.dumps(dic)
# print(bs)
#
#
# d = pickle.loads(bs)
# print(d)


# c = Cat("jerry",18)
# f = open("pickle test",mode="wb")
# pickle.dump(c, f)
#
# f.close()

#
# f = open("pickle test",mode="rb")
# c = pickle.load(f)
# c.catchMouse()

#
# lst = [Cat("猫1",10),Cat("猫2",9),Cat("猫3",8),Cat("猫5",9)]
# f = open("pickle test",mode="wb")
#
# for el in lst:
#     pickle.dump(el,f)
#
# f.flush()
# f.close()


f = open("pickle test", "rb")
while True:
    try:
        c1 = pickle.load(f)
        c1.catchMouse()
    except EOFError:
        break



