#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 1.判断一个数是否是水仙花数,水仙花数是一个三位数，三位数的每一位的三次方的和还等于这个数
# 那这个数就是水仙花数，例如：153 = 1**3+5**3+3**3
# #
# count = 0
#
# num = input("Please The Number: ")
# if len(num) == 3:
#     if num.isdigit():
#         print(num)
# else:
#     print("<%s> Enter Format Error,Please Enter Three digit!" % num)
#     exit()
#
# for i in num:
#     sumBit = int(i)**3
#     count += sumBit
#
# if count == int(num):
#     print("%s is Narcissistic number!" % num)
# else:
#     print("%s is not Narcissistic number!" % num)


#2.彩票36选7，从36个数字中产生7个数字，最终获取到7个不重复的数字作为开奖结果
# from random import randint
# s = set()
# while len(s) < 7:
#     n = randint(1,36)
#     s.add(n)
# print(s)

#3.根据税务部门规定,
    # 1).收入在2000以下的,免征
    # 2).收入在2000-4000的，超过2000部分要征收3%的税
    # 3).收入在4000-6000的，超过4000部分要征收5%的税
    # 4).收入在6000-10000的，超过6000部分要征收8%的税
    # 5).收入在10000以上的，超过部分征收20%的税

# 注:如果一个人的收入是8000，那么他要交2000-4000的税加上4000-6000的税，
# 加上6000-10000的税
#     收入= 8000-(4000-2000)*3% -(6000-4000)*5%-(8000-6000)*8%
# 让用户输入工资计算最终到手工资

# salary = int(input("请输入你的工资: "))
#
# tax1 = (salary - 2000)*0.03
# tax2 = (salary - 4000)*0.05
# tax3 = (salary - 6000)*0.08
# tax4 = 2000*0.03 + 2000*0.05 + 4000*0.08
# tax5 = 2000*0.03 + 2000*0.05 + 4000*0.08 + (salary - 10000)*0.2
#
# if salary <= 2000:
#     print("你不用交税.你的实际收入是%s" % salary)
#
# elif salary <= 4000:
#     icsalary = salary - tax1
#     print("你要交的税是%s,你的实际收入是%s" % (tax1,icsalary))
#
# elif salary <= 6000:
#     icsalary = salary - tax2
#     print("你要交的税是%s,你的实际收入是%s" % (tax2, icsalary))
#
# elif salary <= 8000:
#     icsalary = salary - tax3
#     print("你要交的税是%s,你的实际收入是%s" % (tax3, icsalary))
#
# elif salary <= 10000:
#     icsalary = salary - tax4
#     print("你要交的税是%s,你的实际收入是%s" % (tax4, icsalary))
#
# elif salary > 10000:
#     icsalary = salary - tax5
#     print("你要交的税是%s,你的实际收入是%s" % (tax5, icsalary))


#4.给出一个纯数字列表，请对列表进行排序
# 1.完成a和b的数据交换，例如a = 10,b = 24交互之后，a = 24,b = 10
# 2.循环列表，判断a[i] 和 a[i+1]之间的大小关系,如果a[i]比a[i+1]大,则进行互换
# 循环结束的时候，当前列表中最大数据就会被移动到最右端
# 3.如如果再次执行一次上面的操作，最终第二大的数据移动到右端，以此类推
# 如果反复执行，那这个列表就变成了一个有序列表

#互换一
# a = 10
# b = 24
# c = a
# a = b
# b = c
# print(a,b)
#互换二
# a,b = b,a
# print(a,b)

#互换三
# lst = [123,124,678,670,789,368]
#
# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         lst[i],lst[i+1] = lst[i+1],lst[i]
#
# print(lst)

#冒号排序法
# lst = [123,124,678,670,789,368,6356,3123,4132,654,575]
# for n in range(len(lst)):
#     for i in range(len(lst)-1):
#         if lst[i] > lst[i+1]:
#             lst[i],lst[i+1] = lst[i+1],lst[i]
#
# print(lst)

#99乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,"\t",end="")
#     print("")