#!/usr/bin/env python
#-*- coding: utf-8 -*-


#1.随机生成4位验证码（包含数字字母）
#
# import random
#
# lst = []
# for i in range(48,58):
#     lst.append(chr(i))
#
# for i in range(ord("a"),ord("z") + 1):
#     lst.append(chr(i))
#
# for i in range(ord("A"),ord("Z") + 1):
#     lst.append(chr(i))
#
# print(lst)
# print(random.sample(lst,4))


# 2.模拟发红包，不需要考虑权重问题，纯随机，例如小红发了100块红包，发给30个人，请给出每个人的钱数

# import random
# money = 100
# ren = 30
# qian_money = 0
# lst = []
#
# for i in range(ren - 1):
#     m = random.uniform(0,money - qian_money)
#     qian_money += m
#     lst.append(m)
#
# lst.append(money - qian_money)
# print(lst)


import random

def qhb(money,ren):
    qian_money = 0
    lst = []
    for i in range(ren - 1):
        m = random.uniform(0,money - qian_money)
        qian_money += m
        lst.append(m)

    lst.append(money - qian_money)
    print(lst)

qhb(100,30)

