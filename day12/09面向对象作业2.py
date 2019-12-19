#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.简述面向对象三大特性并用示例解释说明
# 封装
# 继承
# 多态


# 2.面向对象中的变量分为哪几种？并用示例说明区别
# 实例变量
# 类变量(静态变量)


# 3.面向对象中的方法有几种?示例说明
# 实例方法
# 类方法  @classmethod 作为方法标识
# 静态方法  @staticmethod


# 4.面向对象中属性有什么? 并用实例说明
# @property 作为方法


# 5.简述静态方法和类方法的区别
# 静态方法是必须传入对象名
# 类方法可以直接调用方法


# 6.面向对象的方法中哪个不需要传参
# 静态

# 7.面向对象中公有和私有区别
# 公有: 大家都可以调用的方法
# 私有: 只能在内部调用，或者被代理方法调用，私有的表达格式:以__开头


# 8.看代码写结果: [禁止运行]
# class Foo(object):
#     a1 = 11
#     a2 = 12
#
#     def __init__(self):
#         self.a1 = 1
#
# obj = Foo()
# print(obj.a1)  #对象内构造函数指定变量的值会重置默认变量的值
# print(obj.a2)


# 9.看代码写结果:
# class Foo(object):
#     a1 = 11
#
#     def __init__(self,num):
#         self.a2 = num
#
# obj = Foo(999)
# print(obj.a2)  #999
# print(obj.a1)  #11
#
# print(Foo.a1)  #11
# print(Foo.a2)  报错

#
# class Foo(object):
#     a1 = 1
#     __a2 = 2
#     def __init__(self,num):
#         self.num = num
#         self.__salary = 1000
#
#     def get_data(self):
#         print(self.num+self.a1)


# 10.现有50000条数据,请使用面向对象的思维来完成500w条数据的分页工作
# 分页练习
# 方法一：
# lst = ["python%s" % i for i in range(1,50000)]
#
# Pagesingle = 20
# Pagenum = int(input("请输入页面编号: "))
# total = 0
#
# Pagecontent = lst[(Pagenum-1)*Pagesingle:Pagenum*Pagesingle]
#
# if len(lst)%Pagesingle == 0:
#     total = len(lst)//Pagesingle
# else:
#     total = len(lst) // Pagesingle + 1
#
# if Pagenum > total:
#     print("no data.")
# else:
#     for i in Pagecontent:
#         print(i)

# 方法二：对象方法
# class data:
#     def __init__(self,lst,Pagesize):
#         self.lst = lst
#         self.Pagesize = Pagesize
#
#     def start(self):
#         return self.__appoint(1)
#
#     def end(self):
#         return self.__appoint(self.total)
#
#     def index(self):
#         page = int(input("请输入你要显示的页码: "))
#         return self.__appoint(page)
#
#     def __appoint(self,page):
#         return self.lst[self.Pagesize*(page - 1): self.Pagesize * page]
#
#     @property
#     def total(self):
#         total = 0
#         if len(self.lst)%self.Pagesize == 0:
#             total = len(self.lst)//self.Pagesize
#         else:
#             total = len(self.lst) // self.Pagesize + 1
#         return total
#
# lstgen = ["python%s" % i for i in range(1,20000)]
# pagesg = 20
#
# D = data(lstgen,pagesg)
#
# print(D.start())
# print(D.end())
# print(D.index())


# 11.用户注册，保存到一个文件中，并且注册的时候需要到文件中判断是否重复，如果重复，提示不能注册
# 方法一
# class Account:
#     # def __init__(self,username,password):
#     #     self.username = username
#     #     self.password = password
#     #
#
#     def register(self):
#         uname = input("Please Enter The name: ")
#         pwd = input("Please Enter The password: ")
#
#         lst = []
#         with open(r"file\user.txt", mode="r+", encoding="utf-8") as f2:
#             for i in f2:
#                 lst.append(i.split("\t")[0])
#
#         for i in lst:
#             if uname == i:
#                 print('The user is exist...')
#                 break
#         else:
#             with open(r"file\user.txt", mode="a+", encoding="utf-8") as f1:
#                 f1.write("\n" + uname + "\t" + pwd)
#
#
#     def login(self):
#         username = input("Please Enter Login user: ")
#         password = input("Please Enter Login password: ")
#
#         with open(r"file\user.txt", mode="r+", encoding="utf-8") as f3:
#             for i in f3:
#                 if  username == i.split("\t")[0] and password == i.split("\t")[1].strip():
#                     print("login success...")
#                     break
#             else:
#                 print("username or password error...")
#
#     def run(self):
#         while True:
#             print("运行账户操作...")
#             operation = input("1.register\n2.login\n3.exit\n:")
#             if operation == "1":
#                 self.register()
#             elif operation == "2":
#                 self.login()
#             elif operation == "3":
#                 break
#             else:
#                 print("Enter error...")
#
# if __name__ == "__main__":
#     a1 = Account()
#     a1.run()


# 方法二



