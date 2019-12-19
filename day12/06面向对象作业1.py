#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.简述编写类和执行类中方法的流程
# 定义一个类：
#   1.定义一个函数 2.调用类里的函数

# 2.面向对象的三大特征
# 封装、继承、多态

# 3.将一下函数改成类方法使用
# def func(a1):
#     print(a1)
#
# class Output:
#     def output(self,a1):
#         print(a1)
#
# o = Output()
# o.output('拉钩..')

# 4.方法和函数的区别?
# 方法:写在类中，需要传递self
# 函数:孤立，不需要传递self

# 5.什么是构造方法?
# def __init__(self):

# 6.面向对象中的self指的是什么?当前类的对象
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# obj = Person('alex',18,'man')

# 7.以下代码体现面向对象的什么特点?封装
# class Message:
#     def email(self):pass
#     def msg(self):pass
#     def wechat(self):pass

# 8.定义一个类，其中有计算周长和面积的方法(圆的半径通过参数传递到构造方法)

# class Circular:
#     def __init__(self,r):
#         self.r = r
#
#     def perimeter(self):
#         print(2 * 3.14 * self.r)
#
#     def area(self):
#         print(3.14 * self.r ** 2)
#
# round = Circular(10)
# round.perimeter()
# round.area()


# 9.面向对象中为什么要有继承?扩展性

# 10.python多继承时，查找成员的顺序遵循什么规则?从左到右,MRO C3算法
# class Base1:
#     def f1(self):
#         print('base1.1')
#
#     def f2(self):
#         print('base1.f2')
#
#     def f3(self):
#         print('base2.f3')
#         self.f1()
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
#
# class Foo(Base1,Base2):
#     def f0(self):
#         print('foo.f0')
#         self.f3()
#
# c1 = Foo()
# c1.f1()
# c1.f0()


# 11.用对象实现:
# 1.while循环提示用户输入用户名、密码、邮箱
# 2.为每个用户创建一个对象,并添加到列表中
# 3.当列表中添加了3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
#
# class User:
#     def __init__(self, username, password, email):
#         self.username = username
#         self.password = password
#         self.email = email
#
# user_list = []
# # for i in range(3):
# #     user = input("请输入用户名:")
# #     pwd = input("请输入密码:")
# #     email = input("请输入邮箱:")
# #     u = User(user, pwd, email)
# #     user_list.append(u)
# # else:
# #     for u in user_list:
# #         print("我叫: %s ,我的邮箱是: %s" % (u.username, u.email))
# sum = 0
# count = 1
# while True:
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     email = input("请输入邮箱:")
#     u = User(user, pwd, email)
#     user_list.append(u)
#     sum += count
#     if sum == 3:
#         break
#
# for u in user_list:
#     print("我叫: %s ,我的邮箱是: %s" % (u.username, u.email))


# 12.用对象实现用户完整注册和登录
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#
# class Account:
#     def __init__(self):
#         self.userinfo = []
#
#     def register(self):
#         print("注册账户...")
#         id = input("注册ID:")
#         pwd = input("ID密码:")
#
#         u = User(id,pwd)
#         for i in self.userinfo:
#             if id == i.username:
#                 print("账户已存在...")
#         self.userinfo.append(u)
#
#     def login(self):
#         print("账户登录...")
#         username = input("请输入ID: ")
#         password = input("请输入密码: ")
#
#         for u in self.userinfo:
#             if u.username == username and u.password == password:
#                 print("login success! welcome to login xxx...")
#
#     def run(self):
#         while True:
#             print("1.注册\t2.登录\t3.退出")
#             choice = input("账户操作: ")
#             if choice == "1":
#                 self.register()
#             elif choice == "2":
#                 self.login()
#             elif choice == "3":
#                 break
#             else:
#                 print("Enter error,Please Enter 1|2|3...")
#
# if __name__ == "__main__":
#     obj = Account()
#     obj.run()





