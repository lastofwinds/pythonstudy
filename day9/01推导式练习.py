#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# lst = ['abcd','efg','xy','ab','people','number']
# lst1 = [i.upper() for i in lst if int(len(i)) >= 3]
# print(lst1)

# 2.求(x,y)中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
# 方法一
# lstx = [i for i in range(6) if i%2 == 0]
# lsty = [i for i in range(6) if i%2 == 1]
# print([tuple(lstx),tuple(lsty)])

# 方法二
# lst = [(x,y) for x in range(6) for y in range(6) if x%2 == 0 and  y%2 == 1]
# print(lst)

# 3.求M中3，6，9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# lst = [i[-1] for i in M]
# print(lst)

# 4.求出50以内被3整除的数的平方，并放入到一个列表中
# lst = [i*i for i in range(1,51) if i%3 == 0]
# print(lst)

# 5.构建一个列表:[python1期,python2期,python3期,python4期]
# lst = ["python%s" % i for i in range(1,11)]
# print(lst)

# 6.构建一个列表:[(0,1),(1,2),(2,3),(3,4),(4,5)]
# lst = [tuple([i,i+1]) for i in range(6)]
# print(lst)

# 7.构建一个列表:[0,2,4,6,8,10,12,14,16,18]
# lst = [i for i in range(19) if i%2 ==0]
# print(lst)

# 8.有一个列表ll = ['alex','wusir','oldboy','太白']将其构造成这种列表['alex0','wusir1','oldboy2','太白3']
# ll = ['alex','wusir','oldboy','太白']
# ll2 = [(ll[i] + "%s") % i for i in range(len(ll))]
# print(ll2)

# 9.有数据类型:将以下数据通过列表推导式转换成下面的类型:
# [[15123131.89,100],[15123141.89,200],[15123161.89,300]]

# x = {
#     'name': 'alex',
#     'Values': [
#         {
#             'timestamp': 15123131.89,
#             'values': 100
#         },
#         {
#             'timestamp': 15123141.89,
#             'values': 200
#         },
#         {
#             'timestamp': 15123161.89,
#             'values': 300
#         }
#     ]
# }
#
# lst = [[i.get('timestamp'),i.get('values')] for i in x.get('Values')]
# print(lst)

