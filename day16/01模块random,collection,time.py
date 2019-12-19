#!/usr/bin/env python
#-*- coding: utf-8 -*-



'''
    random模块
    collections模块
    time模块
    os模块
    sys模块
'''


# 1.collections模块
#     collections模块主要封装了一些关于集合类的相关操作,比如，我们学过的iterable，
# 除了这些之外，collections还提供了一些除了基本类型以外的
#
# counter计数器


# s = "fadsfoaijgoijnoghoahjopqenlokjvfdnafdsaa"
# dic = {}
#
# for c in s:
#     dic[c] = dic.get(c,0) + 1
# print(dic)


# from collections import Counter
# c = Counter(s)
# print(c)

'''deque: 双向队列'''
# 双向队列中，可以从前往后，也可以从后往前处理队列
from collections import deque

d = deque() #创建一个双向队列

d.append("lina")
d.append("pake")
d.append("elis")

print(d)
d.appendleft("xuke")
print(d)


print(d.pop())
print(d.popleft())


'''namedtuple：命名元组，类似于数学中的坐标'''
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# p = Point(1,2)

# from collections import namedtuple
#
# po = namedtuple("Point",["x","y"])
# p = po(1,2)
#
# print(p)

'''OrderedDict: 字典是原来的两倍'''
# from collections import OrderedDict
#
# od = OrderedDict({"a":1,"b":2,"c":3})
# print(od.get("b"))
# print(od["b"])


'''defaultDict: 默认字典，当key不存在时，返回默认值'''
from collections import defaultdict
d = defaultdict()
d["刘伟"] = "奥特曼"
print(d["刘伟"])




