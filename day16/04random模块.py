#!/usr/bin/env python
#-*- coding: utf-8 -*-


import random

# print(random.random())
print(random.randint(1,100)) #1-100之间随机整数

print(random.randrange(1,5,3)) #1-5之间，步长为3的数

print(random.uniform(1,3)) #随机输出1-3之间的小数

print(random.choice([1,2,3,4,5]))  #随机选一个

print(random.sample(["刘伟","大秧歌","已","fdasf"],3)) #随机选三个

print(random.sample(list(range(1,37)),7))  #在列表中随机选择7个

lst = [2,3,4,5,5,6,7,8,9]
random.shuffle(lst) #洗牌 列表数据顺序打乱
print(lst)


