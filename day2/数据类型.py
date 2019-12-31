#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# name = "alex"
# age = "18"
# hobby = "看书"
# #格式化输出
# print('我叫%s,我喜欢%s,我今年%s' %(name,hobby,age))

# count = 1
#
# while count <= 3:
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#     if username == 'alex' and password == '123456':
#         print("输入正确!")
#         break
#     else:
#         print("用户名或密码错误!")
#
#     print("您已经输错%s次,您还剩%s次输入机会!" % (count,3-count))
#     count += 1

#算法1-2+3-4....+99除了88以外的总和?

# count = 1
# sum = 0
#
# while count < 100:
#     if count == 88:
#         count += 1
#         continue
#     if count % 2 == 1:
#         sum += count
#     else:
#         sum -= count
#     count += 1
# print(sum)

#判断一句话是否是回文
#字符串翻转用法
# tmp = ''
# count = 1
# while count <= 3:
#     content = input("Please Enter Your Article: ")
#     for i in reversed(content):
#         tmp += i
#
#     if content == tmp:
#         print("Right! %s is Palindrome!" % (content))
#         break
#     else:
#         print("Error! %s is not Palindrome!" % (content))
#         print("You typed %s times,You have %s chance." % (count,3-count))
#
#     count += 1

#

# content = input("请输入你的字符串: ")

# upper_case = ''
# lower_case = ''
# digit = ''
#
# for i in content:
#     if i.isupper():
#         upper_case += i
#     if i.islower():
#         lower_case += i
#     if i.isdigit():
#         digit += i
#     # else:
#     #     print("Enter Your upperCase | lowerCase | digit!")
# print("All Upper is %s." % (upper_case))
# print("All Lower is %s." % (lower_case))
# print("All Digit is %s." % (digit))
#
# print(len(upper_case))
# print(len(lower_case))
# print(len(digit))

# AlexInfo = {
#     'name': 'alex',
#     'age': '18',
#     'hobby': 'read a book'
# }
# print(AlexInfo.get('name'))

# name = 'alex'
# age = '18'
# hobby = 'read a book'
# print("My name is %s, I like %s,I am %s years old." % (name,hobby,age))


#列表插入的三种方法
#按照顺序插入
# list = []
# list.append("阮宏宇")
# list.append("钢铁侠")
# list.append("徐峥")
# print(list)
#
# #按位置插入
# list.insert(2,"刘能")
# list.insert(1,"赵四")
# print(list)
#
# #批量插入
# list.extend(["刘德华","张学友","郭富城"])
# print(list)
#
# list2 = ["alex","sherry","dio"]
# list.extend(list2)
# print(list)

#列表删除的方法
#pop默认弹出最后一个,还可以指定索引删除
# lst = ["刘德华","张学友","郭富城"]
# lst.pop()
# print(lst)

# lst.pop(1)
# print(lst)

#remove制定删除
# lst.remove("刘德华")
# print(lst)

#clear清除,清空列表
# lst = ["语文","数学","英语","物理","化学"]
# lst.clear()
# print(lst)

#del,删除列表，切片删除
# del lst[0]
# print(lst)
#
# del lst[::2]
# print(lst)

#修改列表数据
#元素重定义
# lst = ["语文","数学","英语","物理","化学"]
# lst[0] = "垃圾"
# print(lst)
#
# lst[-3] = "人渣"
# print(lst)

#切片修改
# lst[1:4:2] = ["太污","哇靠"]
# print(lst)

# lst = ["马化腾","马云","周鸿祎","李彦宏","雷军"]
# print(lst.count("马云"))
#
# lst.sort()
# print(lst)

# lst = [1,546,342212,965,2,0,3]
# lst.sort()
# print(lst)

#翻转排序
# a = [1,4,2,5]
# a.sort(reverse=True)
# print(a)

#列表嵌套
# lst = [
#     "周润发",
#     "周星驰",
#     "周笔畅",
#     ["九品",["吴孟达","alex","林雪"]],
#     "算死草",
#     "赌侠"
# ]
# lst[3][1][1] = lst[3][1][1].capitalize()
# print(lst[3][1][1])
#
# lst[3][0] = lst[3][0].replace(lst[3][0],"一品")
# print(lst[3][0])

#元组
# tu = (1,2)
# tu1 = (1,)
# print(tu)
# print(tu1)

#空元组定义
# tu2 = tuple()

# #常规输出列表元素
# lst = ["张无忌","张三丰","张翠山","张伟","张磊","张继"]
# for i in lst:
#     print(i)
#
# #获取索引输出列表元素，但是多得到了一个索引
# for el in range(5):
#     print(lst[el])

# for el in range(len(lst)):
#     print(lst[el])

# li = ["alex","WuSir","ritian","barry","wenzhou"]
# li.append("seven")
# print(li)
#
# print(len(li))
# li.insert(0,"Tony")
# print(li)
#
# li.insert(1,"Kelly")
# print(li)

# l2 = [1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)

# s = "qwert"
# li.extend(s)
# print(li)

# li = [1,3,2,"a",4,"b",5,"c"]
# l1 = li[0:3]
# print(l1)
#
# l2 = li[3:6]
# print(l2)
#
# l3 = li[0:7:2]
# print(l3)

# l4 = li[1:6:2]
# print(l4)
#
# l5 = li[-1:]
# print(l5)

# l6 = li[-3:-8:-2]
# print(l6)

# lis = [
#     2,3,"k",
#     ["qwe",20,["tt",3,1],89],
#     "cb","adv"
# ]

# lis[3][2][0] = lis[3][2][0].upper()
# print(lis[3][2][0])

# lis[3][2][0] = lis[3][2][0].swapcase()
# print(lis[3][2][0])

# li = ["alex","eric","rain"]
# sum = ''
# for i in li:
#     sum += i + "_"
#
# print(sum[:-1])
# li = ["alex","eric","rain"]
#
# for i in range(len(li)):
#     print(i)
# li = []
# for i in range(1,100):
#     if i%2 == 0:
#         li.append(i)
#
# print(li)
#
# lis = []
# for i in range(1,50):
#     if i%3 == 0:
#         lis.append(i)
#
# print(lis)
# lis = []
# for i in range(1,100):
#     lis.append(i)
#
# print(lis)

