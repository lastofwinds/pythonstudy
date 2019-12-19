#!/usr/bin/env python
#-*- coding: utf-8 -*-

#函数讲解
# def appointment():
#     print("part 1")
#     print("drink 2")
#     print("dance 3")
#     return "小姐姐","小护士","大妈"
#
# appointment()   #此处执行,不接收返回值,所以在执行时,
#
# people = appointment()   #函数执行后,返回的结果
# print("after appointment get a",people)    #打印return结果

#在函数中如果不写return,表示函数没有返回值,调用方接收到的是None
# return如果放在函数步骤中间,会截断函数执行步骤,后面部分会返回None
# return如果后面跟了值，会返回这个值,同样return也会终止函数程序
# return后可以返回多个值,表示返回多个值，接收方收到的是元组


#函数练习,形参学习
# def appointment(tools,phone):   #形参tools
#     print("拿出 %s 手机" % phone)
#     print("打开 %s" % tools)
#     print("找一下心怡女生")
#     print("吃饭")
#     print("唱歌")
#
# appointment("陌陌","华为")   #实参"陌陌"
# appointment("QQ","苹果")


# def food(good_food, no_good_food, drink):
#     print("I want to eat",good_food, no_good_food, drink)
#
# food("大米饭","炸鸡","冰粉")   #形参实参默认按位赋值
# food(no_good_food="烧烤",good_food="青菜",drink="雪碧") #形参实参指定位置赋值

# def info(name,age,sex):
#     print(name,age,sex)
#
# info(name="alex",age="18",sex="man")
# info(name="ben",age="16",sex="man")

# 设置参数默认值,当给参数传递值得时候，默认值被替代
# def info(name,age,sex="man"):
#     print(name,age,sex)
#
# info("刘伟",18)
# info("张伟",20)
# info("潘晓婷",36,"woman")

#登录验证
# def login(username,password):
#     if username == 'alex' and password == '123':
#         return True
#     else:
#         return False
#
# name = input("Please Enter Your Name: ")
# psd = input("Please Enter Your Password: ")
#
# if login(name,psd):
#     print("go to home page...")
# else:
#     print("ERROR Incorrect username or password!")

#函数示例，return示例
# f(x) = x + 1
# f(3) = 3 + 1 = 4

# def f(x):
#     return x + 1
#
# ret = f(1)
# print(ret)
# print(f(2))

#获取字符串len
# s = "alexbenceildavid"
# def my_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     return count
# print(my_len(s))


#函数进阶
#1.写函数检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
#方法一
# def new_list(lst):
#     lst1 = []
#     for i in range(len(lst)):
#         if i%2 == 1:
#             lst1.append(lst[i])
#     return lst1
#
# new_list = new_list(["鬼泣5","只狼","生化危机2","LOL","王者荣耀","吃鸡","战神3"])
# print(new_list)

#方法二
# def func(lst):
#     return lst[1::2]
# print(func(["鬼泣5","只狼","生化危机2","LOL","王者荣耀","吃鸡","战神3"]))

#2.写函数，判断用户传入的对象(字符串、列表、元组)长度是否大于5
# def func(obj):
#     # if len(obj) > 5:
#     #     return True
#     # else:
#     #     return False
#     return len(obj) > 5
# print(func("linux"))
# print(func(["鬼泣5","只狼","生化危机2","LOL","王者荣耀","吃鸡","战神3"]))
# print(func((1,2,3,4,5,6,7,8)))

#3.写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者
# def func(lst):
#     if len(lst) > 2:
#         return lst[0],lst[1] # 或者return lst[:2]
# obj_opt = func(["鬼泣5","只狼","生化危机2","LOL","王者荣耀","吃鸡","战神3"])
# print(obj_opt)

#4.写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回结果
# def func(string):
#     count1,count2,count3,count4 = 0,0,0,0
#     for i in string:
#         if i == " ":
#             count1 +=1
#
#         elif i.isdigit():
#             count2 += 1
#
#         elif i.isalpha():
#             count3 += 1
#
#         else:
#             count4 += 1
#     return count1,count2,count3,count4
# str = func("__  linux?2321_ 09mkn!")
# print(str)


#5.写函数，接收两个数字，返回大的数字
# def func(digit1,digit2):
#     # if digit1 > digit2:
#     #     return digit1
#     # else:
#     #     return digit2
#     return digit1 if digit1 > digit2 else digit2
# print(func(11,12))

#三目运算
# a = 100
# b = 20
# c = a if a > b else b
# print(c)

#6.写函数，检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容，并将新内容返回给调用者
# def func(dic):
#     for k,v in dic.items():
#         if len(v) > 2:
#             v = v[:2]
#             dic[k] = v
#     return dic
#
# print(func({"k1": "v1v1","k2": [11,22,33,44]}))

#7.写函数，此函数只接收一个参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典
# 的键值对为此列表的索引及对应的元素，例如传入的列表为:[11,22,33]返回的字典为{0:11,1:22,2:33}
# def func(lst):
#     dic = {}
#     if type(lst) == list:
#         for i in range(len(lst)):
#             dic[i] = lst[i]
#         return dic
#     else:
#         print("input error! Please Enter a list.")
#
# print(func([11,22,33]))

#8.写函数，函数接收四个参数分别是：姓名，年龄，性别，学历，用户通过输入这四个内容，然后将这
# 四个字内容传到函数中，此函数接收到这四个内容，将内容追加到一个student_mes文件中
# def func(name,age,sex,edu):
#     with open("./file/student_mes",mode="a",encoding="utf-8") as f:
#         f.write(name + "\t" + age + "\t" + sex + "\t" + edu + "\n")
#         f.flush()
#         f.close()
#
# func("alex","18","man","undergraduate_course")
# func("ben","20","man","undergraduate_course")

#9.对第8题升级，支持用户输入，Q或者q退出，性别默认为男
#写一个函数，要求输入姓名，年龄，学历，性别到一个文件student_mes,性别默认为男，
#如果遇到女学生，则把性别改为女
# def info(name,age,edu,sex="man"):    #默认值必须在末尾
#     with open("./file/student_mes", mode="a+", encoding="utf-8") as f:
#         f.write(name + "\t" + age + "\t" + sex + "\t" + edu + "\n")
#         f.flush()
#     # return name,age,sex,edu
#
# while True:
#     content = input("Do you enter student information? yes(Y) or no(N): ")
#
#     if content.upper() == "Q" or content.upper() == "NO" or content.upper() == "N":
#         print("Exit Program...")
#         break
#     if content.upper() == "Y" or content.upper() == "YES":
#         print("Enter Correct! Next Step...")
#         name = input("Please Enter The Name of The Student: ")
#         age = input("Please Enter The Age of The Student: ")
#         edu = input("Please Enter The Education of The Student: ")
#         sex = input("Please Enter The Gender of The Student: ")
#
#         sex = "man" if sex == "" else "woman"
#         # if sex == "":
#         #     info(name,age,edu)
#         # else:
#         #     info(name,age,edu,sex)


#10.升级题
#写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的
#批量修改操作
# import os
# def filehand(filename,old,new):
#     with open(filename,mode="r",encoding="utf-8") as f1, \
#         open(filename+"_new",mode="w",encoding="utf-8") as f2:
#         for line in f1:
#             line = line.replace(old,new)
#             f2.write(line)
#             f2.flush()
#     os.remove(filename)
#     os.rename(filename+"_new",filename)
#
# filehand("./file/peoplelist","good","sb")


#11.写一个函数完成三次登录功能，再写一个函数完成注册功能

# '''
#     注册
# '''
# def regist(username,password):
#     '''检查是否重复'''
#     f = open("./file/user_info",mode="r+",encoding="utf-8")
#     for line in f:
#         if line != "":
#             continue
#         user_info_username = line.split()[0]
#         if username == user_info_username:
#             return False
#     else:
#         '''写入到文件中'''
#         f.write(username+"\t"+password+"\n")
#
#     f.flush()
#     f.close()
#     return True
#
# name = input("Please enter your username: ")
# psw = input("Please enter your passwor: ")
# print(regist(name,psw))

#
# '''登录,似乎只支持大小写字母和数字'''
# def login(username,password):
#     f = open("./file/user_info",mode="r",encoding="utf-8")
#     for line in f:
#         line = line.split("_")
#         if line[0] == username and line[1] == password:
#             f.close()
#             return True
#     else:
#         f.close()
#         return False
#
# for i in range(2,-1,-1):
#     inusername = input("Please Enter Your Username: ")
#     inpassword = input("Please Enter Your Password: ")
#     ret = login(inusername,inpassword)
#     if ret:
#         print("login success.")
#         break
#     else:
#         print("username or password error,you have %s more chances" % i)



#动态传参
# def eat(*args):
#     for i in args:
#         print("I want to eat", i)
#
# eat("肯德基","鸭脖","啤酒")


#表接收位置传参
#*args位置传参
# def func(a,b,*args):   #作为一个元祖传参，不可以放在前面，不然会报错，因为所有参数都被*args吸收
#     print(a,b,args)
#
# func(1,2,3,4,5)
#
#声明参数
# def func2(*args,a,b):
#     print(args,a,b)
#
# func2(1,2,3,a=4,b=5)  #这里可以参数值声明，以免冲突

#**kwargs关键字传参
# def func(**kwargs):    #关键字传参会得到一个字典，对应键值
#     print(kwargs)
#
# func(a=10,b=20,jay="周杰伦",jj="林俊杰")

#*args+**kwargs基本支持所有传参
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# func(1,2,3,5,jj="林俊杰",jay="周杰伦",soup="鸡汤")

#练习1
# def func(*args):   #聚合参数，成为一个元组
#     print(args)
#
# lst = ["大白菜","小白菜","娃娃菜","大头菜"]
# func(lst)
# func(*lst)    #将列表中实参聚合到元组

#练习2
# def func(**kwargs):
#     print(kwargs)
#
# dic = {"张无忌": "明教教主","谢逊": "金毛狮王","范遥": "光明右使"}
# # func(张无忌=dic["张无忌"],谢逊=dic["谢逊"],范遥=dic["范遥"])
#
# func(**dic)   #这里**是把字典打散，字典的key作为参数的名字，字典的值作为参数的值传递给形参


#命名空间
# 1.全局命名空间
# 2.局部命名空间
# 3.内置命名空间

# #全局命名空间示例
# a = 10
# print(a)
#
# #在函数内部属于局部命名空间
#
# def func():
#         num = 10
#
# func()

#取值顺序，先找局部，再找全局
# a = 10   #全局
# def func():
#     a = 20  #局部
#     print(a)
# func()

#作用域：变量或者函数的声明周期

#globals()查看全局作用域中的所有内容
# qiao = "乔峰"
# print(globals())
#
# def liftAstore():
#     print("Alex lift the store.")
#
# liftAstore()
# print(globals())




#逻辑顺序调用
# def func1():
#     print("我是func1")
#
# def func2():
#     print("我是func2")
#     func1()
#
# def func3():
#     func2()
#     print("我是func3")
#
# func3()

#函数嵌套
# def outer():
#     def inner():
#         print("我是内部")
#     print("我是外部")   #优先调用外部函数
#     inner()    #再调用内部函数
#
# outer()

#函数嵌套练习
# def outer():
#     print("我是外面的.")
#     def inner_1():
#         print("我是inner1.")
#         def inner_2():
#             print("我是inner2.")
#         inner_2()
#     def inner_3():
#         inner_1()
#         print("我是inner3")
#     inner_3()
# outer()


#global全局环境变量设置
# a = 10
# def func():
#     global a   #设置全局环境变量，将函数内部变量设置为全局
#     a = 20   #所有的a都是外面的了
#     print(a)  #现在只有看的权利
#
# print(a)
# func()
# print(a)


#nolocal找局部变量，离他最近的上层变量
# def func():
#     def func0():
#         a = 50
#         def func1():
#             nonlocal a
#             a = 60
#             print("我是func1:",a)
#             def func2():
#                 a = 70
#                 print("我是func2:",a)
#             func2()
#         print("我是func0:",a)
#         func1()
#         print("我是func0:", a)
#     func0()
# func()


