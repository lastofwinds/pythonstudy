#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#1.将10-100倒序插入列表，并且输出能被4整除的元素
# lst = []
#
# for el in range(100,9,-1):
#     if el%2 == 0 and el%4 == 0:
#         lst.append(el)
#
# print(lst)


#2.输出1-30添加进入一个列表，并且能被3整除的元素替换成*
# lst = []
# for el in range(1,31):
#     lst.append(el)
#
# for i in range(len(lst)):
#     if lst[i]%3 == 0:
#         lst[i] = '*'
# print(lst)


#3.找出列表中所有带空格的元素去除空格，并且找出以A或a开头且以c结尾的元素添加到一个列表中
# li = ["TaiBai","ale xC","AbC","reen"," ri TiAn","WuSir","aqc"]
#
# lst = []
# for i in li:
#     li = i.replace(" ","")
#     if (i.startswith("A") or i.startswith("a")) and i.endswith("c"):
#         lst.append(i)
# print(lst)


#5.敏感词列表 li = ["苍老师","东京热","武藤兰","波多野结衣"] \
#如果用户输入了敏感词,则将敏感词替换为等长度的*(苍老师=***)添加到新列表中 \
#如果用户没有输入敏感词,则添加到上面列表中


# li = ["苍老师","东京热","武藤兰","波多野结衣"]
#
# lst = []
#
# content = input("Please input your content: ")
#
# for i in li:
#     if i == content:
#         content = content.replace(i,"*"*len(i))
# print(content)


#6.一个列表[1,3,4,"alex",[3,7,8,"TaiBai"],5,"RiTiAn"],循环打出里面的每个元素，遇到列表，再循环里面的元素，以此类推
# lst = [1,3,4,"alex",[3,7,8,"TaiBai"],5,"RiTiAn"]

# for i in lst:
#     if type(i) == list:
#         for n in i:
#             print(n)
#     else:
#         print(i)
#对上面的的大写全部转换成小写
# for i in lst:
#     if type(i) == list:
#         for n in i:
#             if type(n) == str:
#                 print(n.lower())
#             else:
#                 print(n)
#     else:
#         if type(i) == str:
#             print(i.lower())
#         else:
#             print(i)


#7.输入班级成绩，格式为:张三_55,添加到一个列表，并且求平均分?
# lst = []
# while True:
#     grade = input("请输入学生及分数或Q/q推出程序: ")
#     if grade.upper() == 'Q':
#         break
#     lst.append(grade)
#
# print(lst)
# sum = 0
# for i in lst:
#     sum += int(i.split("_")[1])
#
# print(sum/len(lst))


#8.敲7游戏，从0开始数，遇到数字含有7或7的倍数则给列表添加一个“咣”，所有数都添加到一个列表中?
# lst = []
# n = int(input("请输入列表要添加的数字个数: "))
#
# for i in range(1,n+1):
#     if i%7 == 0 or "7" in str(i):
#         lst.append("咣")
#     else:
#         lst.append(i)
#
# print(lst)


#9.心动女生选择，先输入10个心动女生,而后再选择3个心动女生，最后选出一个，每次选择之前都会出现选项供选?



