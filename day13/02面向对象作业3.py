#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# class F3(object):
#     def f1(self):
#         ret = super().f1()
#         print(ret)
#
# class F2(object):
#     def f1(self):
#         print('123')
#
# class F1(F3,F2):
#     pass
#
# obj = F1()
# obj.f1()


# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#
#     def changelist(self,request):
#         print(self.num,request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#         def changelist(self,request):
#             print(666,self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self,k,v):
#         self._registry[k] = v(k)
#         self._registry[Department] = RoleConfig(Department)
#
# site = AdminSite()


# 1.完成网上商城订单功能，写出基本结构和基本操作即可，把结构一定列出来
# 每个用户都有一堆订单，每个订单有一堆订单明细，每个明细对应一个商品
# 用户
# 信息：订单编号、昵称、用户名、密码、电话、email、家庭住址、身份证号

# 订单
# 信息：订单编号、流水号、所属用户编号、收货编号、邮费、订单状态（0:是否发货，1:是否收货，2：是否退货）
# 评价编号

# 评价
# 信息：评价编号，评价分数，评价内容，评价显示（0：显示，1：不显示），评价类型（1：物流评价，2：服务评价，3：商品评价）

# 订单明细
# 信息：明细编号，小流水号，商品购买时价格，购买数量，商品编号

#
# class User:
#     def __init__(self,id,nick_name,login_name,login_psw,real_name,card,phone,address,email):
#         self.id = id
#         self.nick_name = nick_name
#         self.login_name = login_name
#         self.login_psw = login_psw
#         self.real_name = real_name
#         self.card = card
#         self.phone = phone
#         self.address = address
#         self.email = email
#         self.order_list = []
#
# class Order:
#     def __init__(self,id,liushui,user,address,pingjia,youfei,order_status=0):
#         self.order_detail_list = []
#
# class Pingjia:
#     def __init__(self,id,score,content,pingjia_status,isShow=0):
#         pass
#
# class OrderDetail:
#     def __init__(self,id,xiaoliushui,price,num,product,order):
#         pass
#
# class Product:
#     def __init__(self,id,name,desc,price,store):


# 2.完成学生选课系统

# 学生
# 信息：学号、姓名、住址、选的课程列表
# 功能：
#     查看：查看学生所有课程信息
#     添加：添加课程：把选好的课程添加到课程列表

# 课程
# 信息：课程编号、课程名称、老师
# 功能：
#     查看：查看该课程的全部信息
#     设置老师：给当前课程设置一个老师

# 老师
# 信息：老师编号、老师名称、老师电话
# 功能：无

from random import randint
class Student:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address
        self.class_list = []

    def AddCourse(self,course):
        self.class_list.append(course)

    def __str__(self):
        print("姓名:%s" % self.name)
        for c in self.class_list:
            print("所选课程: %s" % c.name)
            if c.teacher:
                print("授课老师是:%s" % (c.teacher.phone))
            else:
                print("该课程还没有老师...")
        return "___________"


class Course:
    def __init__(self,id,name,teacher=None):
        self.id = id
        self.name = name
        self.teacher = teacher


    def set_teacher(self,teacher):
        self.teacher = teacher

    def show(self):
        if self.teacher:
            print("课程:%s,授课老师是:%s" % (self.name,self.teacher.name))
        else:
            print("课程:%s,授课老师是:%s" % self.name,"无")

class Teacher:
    def __init__(self,id,name,phone):
        self.id = id
        self.name = name
        self.phone = phone


c1 = Course(1,"语文")
c2 = Course(2,"数学")
c3 = Course(3,"英语")

t1 = Teacher(1,"彭大",123456)
t2 = Teacher(2,"王二",234561)
t3 = Teacher(3,"张三",345612)

c1.set_teacher(t1)
c2.set_teacher(t2)
c3.set_teacher(t3)

c_lst = [c1,c2,c3]
stu_lst = []
for i in range(30):
    stu = Student(i,"Stu%s" % i,"Sh")

    s = set()
    while len(s) < 3:
        s.add(randint(0,2))

    for index in s:
        stu.AddCourse(c_lst[index])

    stu_lst.append(stu)


for stu in stu_lst:
    print(stu)


