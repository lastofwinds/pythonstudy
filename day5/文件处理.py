#!/usr/bin/env python
#-*- coding: utf-8 -*-


#文件操作
#readline逐行读取文件,readlines读取所有行
# f1 = open("c:\pythonTestFile\主播苍老师大片.txt",mode="r",encoding="UTF-8")
# line1 = f1.readline().strip()
# line2 = f1.readline().strip()

# print(line1,end="*")
# print(line2,end="*")

# content = f1.read()  #一次全部读取，一般不使用，缺点：当文件过大会导致内存溢出，卡死
# print(content)
# line3 = f1.readlines()  #一次全部读取,以列表显示出来
# print(line3)

# for line in f1:
#     print(line)
#
# f1.close()

#文件读写模式
# r读
# w尾部追加
# a换行追加

# f1 = open("c:\pythonTestFile\主播苍老师大片.txt",mode="a",encoding="UTF-8") #追加写入
#
# f1.write("周文王")
# f1.flush()
# f1.close()
#
# f1 = open("c:\pythonTestFile\主播苍老师大片.txt",mode="w",encoding="UTF-8")  #w写的时候，先清空再写入
# f1.write("周大星")
# f1.flush()
# f1.close()

#对于无法直接读取的文件，需要用到
# rb   类似二进制文件处理(指令、图片等等)
# wb
# ab
# f2 = open(r"c:\pythonTestFile\01.jpg", mode="rb")
# f3 = open(r"c:\pythonTestFile\01-1copy.jpg",mode="wb")
#
# for line in f2:
#     f3.write(line)
# f2.close()
# f3.flush()
# f2.close()

#相对路径操作图片文件
# import requests
# rs = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559732118712&di=0caded2261660296fca6e3e29908c24a&imgtype=0&src=http%3A%2F%2Fimg5q.duitang.com%2Fuploads%2Fitem%2F201410%2F20%2F20141020212040_BUGNA.thumb.700_0.jpeg")
# f = open("./photo/壁纸.jpg",mode="wb")
# f.write(rs.content)
# f.flush()
# f.close()

# 文件操作扩展模式
# r+  读写模式
# w+  写读模式
# a+  追加读模式
# r+b
# w+b
# a+b
# +    加模式会为尾部增加新写入的内容

#写读模式
# f = open("./file/菜单",mode="w+",encoding="UTF-8")
# f.write("清炒藕片")
# f.seek(0) #移动光标至开头
# content = f.read()
# print("读取的内容是",content)
# f.flush()
# f.close()

#读写模式
# f = open("./file/菜单",mode="r+",encoding="UTF-8")
# f.write("可乐鸡翅")
# f.seek(0)
# content = f.read()
# print("读取的内容是",content)
# f.flush()
# f.close()

#追加读模式
# f = open("./file/菜单",mode="a+",encoding="UTF-8")
# f.write("清炒藕片")
#
# f.seek(0)
# content = f.read()
# print(content)


#使用tell()可以知道光标在哪里
#使用seek()可以移动光标，0:表示开头,1:表示当前位置,2:表示结尾
#读写的时候，单位字符
#光标：单位时候是字节
# f = open("./file/菜单",mode="r",encoding="UTF-8")
# print(f.read(1))
#
# print(f.read(1))
# print(f.read(1))
# print(f.tell())   #告诉光标位置
#
# #从开头到结尾，一个汉字是三个字节
# #f.seek(偏移量,结尾)
# print(f.seek(0,2))

# f = open("./file/菜单",mode="w+",encoding="UTF-8")
# f.seek(0)
# print(f.read(1))
# f.seek(0,2)
#
# f.write("烤肉拌饭")
# f.flush()
# f.read()

#写一个循环为文件增加内容
# fadd = open("./file/people.txt",mode="a+",encoding="UTF-8")
# fread = open("./file/people.txt",mode="r+",encoding="UTF-8")
#
# lst = []
# while True:
#     content = input("Please input content or Enter |q or Q| quit Program: ")
#     if content.upper() == 'Q':
#         break
#     lst.append("\n"+content)
#
# print("add content for documents:",lst)
#
# for i in lst:
#     fadd.write(i)
#
# fadd.flush()
# for i in fread.readlines():
#     print(i)

#truncate截断
# f = open("./file/名字",mode="r+",encoding="UTF-8")
# f.seek(9)
#
# f.truncate(12)    #从第12位将其后面字符串截断删除,如果后面没有参数，就按照光标位置截断,如果有参数，截断到参数位置
# f.flush()

#with 语法操作文件，修改文件内容保存
# import os,time
# with open("./file/peoplelist",mode="r",encoding="utf-8") as f1 , \
#         open("./file/peoplelist_bak1",mode="w",encoding="utf-8") as f2:
#
#     for line in f1:
#         new_line = line.replace("good","sb")
#         f2.write(new_line)
#
# time.sleep(3)
# os.remove("./file/peoplelist")
# time.sleep(3)
# os.rename("./file/peoplelist_bak1","./file/peoplelist")

#日志文件处理
# result = []
# with open("./file/2019-06-06.log",mode="r+",encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         lst = line.split("|")
#         dic = {"时间": lst[0],"name":lst[1],"action":lst[2]}
#         result.append(dic)
# print(result)

# result = []
# with open("./file/yum.log",mode="r+",encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         lst = line.split(" ")
#         dic = {"time": lst[0:3],"action": lst[3].strip(":"),"object": lst[4]}
#         result.append(dic)
# print(result)

#练习一
#字符处理
# reslut = []
#
# with open("./file/fruitlist",mode="r+",encoding="utf-8") as f:
#     for line in f:
#         lst = line.split()
#         dic = {}
#         for el in lst:
#             dic[el.split(":")[0]] = el.split(":")[1]
#         reslut.append(dic)
#
# print(reslut)