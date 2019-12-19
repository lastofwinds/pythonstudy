#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 1.依赖关系  在方法中引入另一个类的对象
# 2.关联关系
# 3.组合关系
# 4.聚合关系
# 5.继承关系
# 6.实现关系
# 7.特殊成员

'''1.依赖关系演示: 在方法中引入另一个类的对象'''
# class Elephant:
#     def __init__(self,name):
#         self.name = name
#
#     def open(self,ref):
#         print("open the door.")
#         ref.open_door()   #依赖关系
#
#     def close(self,ref):  #依赖关系，涉及到解耦
#         print("I'm in.close the door.")
#         ref.close_door()
#
#     def getinto(self):
#         print("get into...")
#
# class Refrigerator:
#     def open_door(self):
#         print("refrigerator opened it's door.")
#
#     def close_door(self):
#         print("refrigerator closed it's door.")
#
# alex = Elephant("liuwei")
# bx1 = Refrigerator()
# alex.open(bx1)
# alex.close(bx1)


'''2.关联关系演示: '''
# class Boy:
#     def __init__(self,name,xingge,girlFriend=None):
#         self.name = name
#         self.xingge = xingge
#         self.girlFriend = girlFriend
#
#     def yujian(self,girl):
#         self.girlFriend = girl    #关联至Girl对象
#
#     def eat(self):
#         if self.girlFriend:
#             print("%s 和 %s 一起吃" % (self.name,self.girlFriend.name))
#         else:
#             print("单身狗...")
#
# class Girl:     #关联至Boy类中yujian方法
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print("%s 在吃..." % self.name)
#
# alex = Boy("alex","娘炮")
# alex.eat()
# girl = Girl("tingting")
# alex.yujian(girl)
# alex.eat()
# alex.girlFriend.eat()   #关联中可以调出被关联对象的功能


'''关联关系设计组合聚合: 一对多练习'''
# class School:
#     def __init__(self,name,address,phone,teach_list = []):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.__teach_list = []
#
#     def zhaopin(self,t):
#         self.__teach_list.append(t)
#
#     def display(self):
#         for el in self.__teach_list:
#             print(el.name,el.hobby)
#
# class Teacher:
#     def __init__(self,name,gender,salary,hobby,school):
#         self.name = name
#         self.gender = gender
#         self.salary = salary
#         self.hobby = hobby
#         self.school = school
#
# tuling_bj = School("图灵","朝阳国贸","10000")
# tuling_sh = School("图灵","上海浦东","10001")
# tuling_sz = School("图灵","深圳南山","10001")
#
# t1 = Teacher("Taibai","man",150000,"开车",tuling_bj)
# t2 = Teacher("Eggon","man",100000,"钻研技术",tuling_sh)
# t3 = Teacher("gaoxin","woman",50000,"带娃",tuling_sz)
#
# tuling_bj.zhaopin(t1)
# tuling_sh.zhaopin(t2)
# tuling_sz.zhaopin(t3)
#
# tuling_bj.display()
# tuling_sh.display()


'''类名和对象是可以作为key使用'''
# class Base:
#     def __init__(self,num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#         self.func2()
#
#     def func2(self):
#         print(111,self.num)
#
# class Foo(Base):
#     def func2(self):
#         print(222,self.num)
#
# lst = [Base(1),Base(2),Foo(3)]
# for obj in lst:
#     obj.func2()




