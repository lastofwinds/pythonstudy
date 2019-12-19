#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1.写函数传入一个n，返回n的阶乘
# 例如:cal(7)计算7*6*5*4*3*2*1
# def cal(n):
#     sum = 1
#     for i in range(n, 0, -1):
#         sum *= i
#     return sum
# print(cal(5))


#2.写函数，返回一个扑克牌，里面有52项，每一项是一个元组
# 例如: [('红心',2),('梅花',2),...('黑桃','A')]
# st = ['红桃','黑桃','梅花','方块']
# num = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# #笛卡儿积
# def dke():
#     result = []
#     for house in st:
#         for numd in num:
#             result.append((house,numd))
#     return result
# dke()


#3.99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s * %s = %s" % (i,j,i*j),end=" ")
#     print()


#4.打印出*
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

