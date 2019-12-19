#!/usr/bin/env python
# -*- coding: utf-8 -*-


# lambda 匿名函数
#     lambda 参数: 返回值

# sorted 排序
#     sorted(iterable,key=func,reverse=True)
#     执行流程:
#         把可迭代对象中的每个元素拿出，放到func中运行，返回一个数字，根据数字排序

# filter 筛选
#     filter(func,Iterable)
#     执行流程:
#         把可迭代对象中的每个元素拿出，放到func中运行，放到func中运行，返回True/False,根据True/False，决定数据
# map 映射
#     map(func,Iterable)
#     执行流程:
#         把可迭代对象中每个元素拿出，放到func中运行，返回数据就是结果


# lambda匿名函数
#
#         zrf = lambda x : x**3   #匿名函数lamdba 参数:返回值
#         print(zrf(2))
#
#         匿名函数练习
#         给函数传递两个参数a,b返回a+b的结果
#         sum = lambda a,b : a + b
#         c = sum(1,2)
#         print(c)

# sorted排序函数
#
#         lst = [1,2,5,4,7,11,6]
#         lst1 = sorted(lst)  #正序排列
#         print(lst1)
#
#         lst2 = sorted(lst,reverse=True) #倒叙排列
#         print(lst2)
#
#         lst = ["刘伟","david","刘能","周星驰","alex","发ge","周润发"]
#         lst1 = sorted(lst)   #默认字符串an优先
#
#         print(lst1)
#
#         def func(*args):
#             return args
#
#         x = func("abcf","中国","@#$","发ge","123")   #阿拉伯数字>特殊字符>字母>汉字,同类字符串按长度排序
#         y = sorted(x,key=func)
#         print(y)
#
#         # 使用lambda
#         lst = ["刘伟","david","刘能","周星驰","alex","发ge","周润发"]
#         # def func(name):
#         #     return len(name) % 3
#         a = lambda name: len(name) % 3
#         l2 = sorted(lst,key=a)  #流程:把可迭代对象的每一项传递给函数,函数返回一个数字,根据这个数字完成排序
#         print(l2)
#
#
#
#         lst = [
#             {"id":1,"name":"alex","age":18},
#             {"id":2,"name":"ben","age":16},
#             {"id":3,"name":"cecil","age":17},
#         ]
#
#         #按照年龄排序
#         # def func(dic):
#         #     return dic['age']
#
#         func = lambda sortAge : sortAge['age']   #根据字典中的年龄排序
#         l2 = sorted(lst,key=func)
#         print(l2)
#
#         func1 = lambda sortLen : len(sortLen['name'])   #根据字典中名字的长度排序
#         l3 = sorted(lst,key=func1)
#         print(l3)
#
#         func2 = lambda sortAcronym : ascii(sortAcronym['name'])  #根据ascii码排序
#         l4 = sorted(lst,key=func2)
#         print(l4)
#

# filter筛选函数
#         练习一:
#         lst = [23,28,15,27,24,22,14]
#         def func(age):
#             return age > 18
#
#         f = filter(lambda age: age > 18,lst)  #filter基本用法
#         x = sorted(f)
#         print(x)
#         for el in f:
#             print(el)
#
#         f = filter(lambda age : age % 2 == 0,filter(lambda age : age > 18, lst))  #filter嵌套
#         print(list(f))
#
#
#         print(list(filter(lambda dic: dic['age'] >=17,lst)))
#
#         练习二:
#         lst = [
#             {"id":1,"name":"alex","age":18},
#             {"id":2,"name":"ben","age":16},
#             {"id":3,"name":"cecil","age":17},
#         ]
#
#         print(list(sorted(filter(lambda dic: dic['age']>=17,lst),key=lambda dic: dic['age'])))


# map映射函数
# map(function,iterable)可以对可迭代对象中的每一个元素进行映射,分别取执行function
#
#         def func(e):
#             return e**2
#
#         mp = map(func,[1,2,3,4,5])
#         print(mp)
#         print(list(mp))
#
#         lst = [1,15,9,3,2,7,8,6,4]
#         l1 = [i**2 for i in lst]
#         m = map(lambda x: x**2,lst)
#         print(list(m))

#         计算两个列表相同位置的和
#         lst1 = [1,2,3,4,5]
#         lst2 = [2,4,5,6,7]
#
#         sum12 = map(lambda a,b : a + b,lst1,lst2)
#         print(list(sum12))


