#/usr/bin/env python
# -*- coding: utf-8 -*-

#1.有如下元组，实现要求的功能
# tu = ("alex", [11,22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)},44] )

# tu = ("alex", [11,22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)},44] )
# print(tu[1][2]['k3'])
# print(tu[1][2]['k1'])
# print(tu[1][2]['k2'])
# tu[1][2]['k2'].append('seven')
# print(tu[1][2]['k2'])


#2.dic = {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}

# dic = {"k1": 'v1', "k2": ["age", "name"], "k3": [11,22,33]}
# print(dic)

# dic['k4'] = 'v4'
# print(dic)
# for i in dic:
#     print(i)

# for k,v in dic.items():
#     print(k)
#     print(v)

# for item in dic.items():
#     k,v = item
#     print(k,v)

# dic['k1'] = 'alex'
# print(dic)

# for key in dic.keys():
#     print(key)
#     print(dic[key])

# dic["k3"].append(44)
# print(dic)
#
# dic["k3"].insert(0,18)
# print(dic)


#3.有字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
#字符串和字典转换
# s = "k:1|k1:2|k2:3|k3:4"
# lst = s.split("|")
# dic = {}
#
# for el in lst:
#     a,b = el.split(":")
#     dic[a] = b
# print(dic)


#4.元素分类：有如下值li = [11,22,33,44,55,66,77,88,99,90],将所有大于66的值
#保存至字典的第一个key中，将小于66的值保存至第二个key的值中.
# dic = {'k1': [],'k2': []}
#
# li = [11,22,33,44,55,66,77,88,99,90]
# for el in li:
#     if el > 66:
#         dic['k1'].append(el)
#     if el < 66:
#         dic['k2'].append(el)
# print(dic)

#方法二
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {}
#
# for el in li:
#     if el > 66:
#         此处必须setdefault，不然在循环中值会被替换掉
#         dic.setdefault('k1', []).append(el)
#     if el < 66:
#         dic.setdefault('k2', []).append(el)
# print(dic)

#方法三
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {}
#
# for el in li:
#     if el < 66:
#         if dic.get("k1") == None:
#             dic['k1'] = [el]
#         else:
#             dic['k1'].append(el)
#     else:
#         if dic.get('k2') == None:
#             dic['k2'] =[el]
#         else:
#             dic['k2'].append(el)
# print(dic)


#5.输入商品列表
#
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
#
# for el in range(len(goods)):
#     print(el+1, goods[el]["name"], goods[el]["price"])
#
#
# #6.输入编号显示商品信息
# while True:
#     content = input("请输入你选择的编号: ")
#     if content.isdigit():
#         content = int(content) -1
#         if content <= len(goods):
#             print(goods[content]["name"], goods[content]["price"])
#         else:
#             print("超过了商品范围 ")
#     if content.upper() == 'Q':
#         print("正在退出程序...")
#         break
#     else:
#         print("输入的内容不合法")



