#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.接口的作用
# 接口可以把不相干的系统衔接起来

# 2.抽象类和抽象方法的作用
# 抽象类和抽象方法就是用来约束代码规范的

# 3.python中应该如何约束派生类中指定的方法


# 4.如何自定义异常
# 创建异常对象，执行调用，使用raise语句抛出异常
# raise

# 5.MD5加密是否可以被反解
# 不可以反解，不可逆

# 6.为了防止撞库，md5加密时需要做什么操作并写代码实现


# 7.抽象类抽象方法和接口的区别


# 8.选课系统开发 系统登录需要有三类用户：学生、管理员、老师，针对不同用户提供不同功能：

# 学生用户：对于学生用户来说，登录之后有三个功能
# 1、查看所有课程
# 2、选择课程
# 3、删除已选课程

# 管理员用户：管理员用户除了可以做一些查看功能之外，还有很多创建工作
# 1、创建课程
# 2、创建学生账号
# 3、查看所有课程
# 4、查看所有学生
# 5、查看所有学生的选课情况

allcourse = [
    '语文',
    '数学',
    '英语',
    '历史',
    '地理',
    '生物',
    '政治',
    '物理',
    '化学',
    '计算机基础',
    'linux',
    'python',
    'go初级',
    'c语言入门与实践',
    '网络工程'
]

class Student:
    def __init__(self,id,username,address):
        self.id = id
        self.username = username
        self.address = address
        self.courselist = []

    def Addcource(self,course):
        self.courselist.append(course)

    def Seecourse(self):
        print("%s choose %s" % (self.username,self.courselist))

    def Delcourse(self,course):
        self.courselist.remove(course)

class Admin:

    def createcourse(self,course):
        allcourse.append(course)


class Teacher:
    pass

class manage:
    pass

Stu1 = Student(1,'alex','nanjing road 123')
Stu1.Addcource(allcourse[0])
Stu1.Addcource(allcourse[1])
Stu1.Addcource(allcourse[5])
Stu1.Delcourse(allcourse[1])

Stu1.Seecourse()

Adm1 = Admin()
Adm1.createcourse('docker入门与实践')
print(allcourse)

