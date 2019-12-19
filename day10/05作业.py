#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.用map来处理字符串列表，把列表中所有人都变成sb，例如alex_sb
# 方法一
# name = ['oldboy','alex','wusir']
# def nameList(name):
#     return name + "_sb"
#
# print(list(map(nameList,name)))

# 方法二
# name = ['oldboy','alex','wusir']
# lst = list(map(lambda n:n+"_sb",name))
# print(lst)


# 2.用map来处理下述1st，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾

# lst = [{'name':'alex'},{'name':'y'}]
#
# ll = list(map(lambda dic:{'name': dic['name']+"sb"},lst))
# print(ll)


# 3.用filter来处理，得到股票价格大于20的股票名字
# shares = {
#     'IBM': 36.6,
#     'Lenovo': 23.3,
#     'oldboy': 21.2,
#     'ocean': 10.2
# }
#
# print(list(filter(lambda k: shares[k] > 20,shares)))
# print(list(filter(lambda v: v > 20,shares.values())))


# 4.有下面字典，得到购买每只股票的总价格，并且放在一个迭代器中:
# 结果：list一下[9110,0,27161.0,....]
# portfolio = [
#     {'name': 'IBM','shares': 100,'price': 91.1},
#     {'name': 'AAPL','shares': 50,'price': 543.22},
#     {'name': 'FB','shares': 200,'price': 21.09},
#     {'name': 'HPQ','shares': 35,'price': 31.75},
#     {'name': 'YHOO','shares': 45,'price': 16.35},
#     {'name': 'ACME','shares': 75,'price': 115.65}
# ]

#
# print(list(map(lambda dic:dic['price'] * dic['shares'],portfolio)))
# print(list(filter(lambda dic: dic['price'] > 100,portfolio)))


# 5.有以下三种数据类型,写出（每个元组第一个元素>2,第三个*至少是4个）
# 例如：[(3,'wusir','****'),(4,'太白','*******')]
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','*******')
#
# print(list(filter(lambda tu: tu[0] > 2 and len(tu[2]) >=4,zip(l1,l2,tu))))


# 6.对以下列表进行排序
# lst = [
#     {'sales_volumn': 9},
#     {'sales_volumn': 58},
#     {'sales_volumn': 272},
#     {'sales_volumn': 456},
#     {'sales_volumn': 440},
#     {'sales_volumn': 239}
# ]
#
# print(sorted(lst,key=lambda dic:dic['sales_volumn']))
# print(list(map(lambda dic:dic['sales_volumn'],lst)))




