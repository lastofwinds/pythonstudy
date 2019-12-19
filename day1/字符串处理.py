#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#1.取单数,双数取法类似
# x = range(1,101)
# for i in x:
#     if i%2 != 0:
#         print(i)


#2.求1..100之间所有整数相加的和
# count = 1
# sum = 0
#
# while count <= 100:
#     sum = sum + count
#     print(count)
#
#     count += 1
# print(sum)


#3.字符串切片
# s = "你今天吃啥？"
# print(s[1:5])
# print(s[0])
# print(s[-1])
# print(s[2:-1])
# print(s[1:5:2])
# print(s[-1:-6:-2])


#4.upper不区分大小写
# count = 1
# while count <= 3:
#     Enter = input("请输入Q或q退出程序: ")
#     if Enter.upper() == 'Q':
#         print("OK")
#         break
#     else:
#         print("你已经输错%s次,你还有%s次机会重试!" % (count,3-count))
# count = 1
#
# while count <=3 :
#     Enter = input("请输入Q或者q,退出程序: ")
#     if Enter == 'Q' or Enter == 'q':
#         print("输入正确,OK!")
#         break
#     else:
#         print("你已经输错%s次,你还有%s次机会重试!" % (count,3-count))
#     count += 1


#5.swapcase大小写互换
# s = "Alex isn't a good man!"
# s1 = s.swapcase()
# print(s1)


#6.casefold文字转换成小写，支持的文字比lower多(主要针对各个国家不同文字)


#7.strip去掉字符串中的空格
# s = "   linux is very good!  "
# print(s.strip())
#一般用于用户输入账号信息，自动去空格


#8.replace(old,new)字符串替换
# s = "刘伟"
# s1 = s.replace("刘伟","刘德华")
# print(s1)
#
# print(s1.isalnum())


#9.split()切片结果是list
# s = "linux is very good!"
# lst = s.split()
# print(lst[0])


#10.format人称占位符,空位字符串传递管道,格式化
# print("i am %s, i am %d years old, i like do %s" % ("alex", 18, "python"))
# print("i am {},i am {} years old, i like do {}".format("alex",18,"python") )
# print("i am {0},i am {1} years old, i like do {2}".format("alex",18,"python"))
# print("i am {name},i am {age} years old, i like do {hobby}".format(name="alex",age=18,hobby="python"))


#11.startswith 判断以什么开头
# s = " copy that, my lady"
# s1 = s.startswith(' ')
# print(s1)


#12.count方法统计次数
# s = "linux is very good! you can make linux for study!"
# s1 = s.count("linux")
# print(s1)


#13.find 方法查找，如果没有返回-1,找到返回0
# s = "linux is very good! you can make linux for study!"
# s1 = s.find("ok")
# s2 = s.find("linux")
# print(s1)
# print(s2)


#14.index方法 匹配索引位置，默认匹配第一个找到的，如果没有则报错
# s = "linux is very good! you can make linux for study!"
# s1 = s.index("i")
# print(s1)


#15.isalpha方法 判断是否由字母组成,返回结果为True或false
# s = "linux"
# s1 = s.isalpha()
# print(s1)


#16.isdigst方法 判断是否由数字组成,只认识阿拉伯数字
# s = "123"
# s1 = s.isdigit()
# print(s1)


#17.isnumeric方法 判断是否为数字阿拉伯数字和中文数字都支持
# s = "123456一二"
# s1 = s.isnumeric()
# print(s1)


#18.len字符串长度处理
# s = "just calm down"
# s1 = len(s)
# print(s1)


#19.遍历字符串
# s = "abcdefg"
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1


#20.字符串练习
#name = "aleX leNb"
# print(name[1:-1])


#21.strip方法不光可以空格 还可以去掉选中字符串,只能去除左右两边连在一起的
# print(name.strip("ab"))

# print(name.lstrip("a").rstrip("b"))

#22.判断字符串是否以al开头
# print(name.startswith("al"))

#23.判断字符串是否以Nb结尾
# print(name.endswith("Nb"))

#24.替换
# print(name.find("l"))
#只替换第一个l
# print(name.replace("l","p",1))

#25.根据分隔符分割
# print(name.split("l"))
#根据分隔符第一个l分割
# print(name.split("l",1))


#26.大小写处理
# print(name.upper())
# print(name.lower())


#27.首字母大写capitalize方法
# print(name.capitalize())


#28.count统计方法
#print(name.count("l"))

# if 'x' in name:
#     print(name.index('x'))
# else:
#     print("x isn't in name!error!")

# print(name[1])
# print(name[0:3])
# print(name[-2:])


#29.取name中字母e的索引
# count = 0
# while count < len(name):
#     if name[count] == 'e':
#         print(count)
#
#     count += 1

# s = "123a4b5c"
# s1 = s[0:3]
# print(s1)
#
# s2 = s[4:7]
# print(s2)
#
# s3 = s[0:7:2]
# print(s3)
#
# s4 = s[1:6:2]
# print(s4)
#
# s5 = s[-1]
# print(s5)
#
# s6 = s[-3:0:-2]
# print(s6)


#30.倒计时，格式化输出
# x = "321"
# for c in x:
#     print("倒计时%s秒" % (c))
# else:
#     print("出发")


#31.整数加法计算器,只可以两个数字相加

# content = input("请输入计算数字: ")
# content.replace(" ","")
# lst = content.split("+")
# print(int(lst[0]) + int(lst[1]))


#32.判断输入的字符串有几个数字
# count = 0
# x = input("请输入: ")
# for c in x:
#     if c.isdigit():
#        count += 1
# print(count)


#33.选择题
# while True:
#     print("1.你要走大路还是走小路还是绕道回家呢?")
#     print("A. 走大路回家\tB. 走小路回家\tC. 绕道回家")
#     Enter = input("你的选择是: ")
#     if Enter.upper() == 'A':
#         print("走大路回家.")
#         print("A. 坐公交\tB. 走路")
#         Enter2 = input("你的选择是: ")
#         if Enter2.upper() == 'A':
#             print("你选择了公交车，你需要10分钟可以到家.")
#             break
#         elif Enter2.upper() == 'B':
#             print("你选择了走路，你需要20分钟可以到家.")
#             break
#     elif Enter.upper() == 'B':
#         print("走小路回家")
#         break
#     elif Enter.upper() == 'C':
#         print("绕道回家")
#         print("A. 去游戏厅\tB.去网吧")
#         Enter3 = input("你的选择是: ")
#         if Enter3.upper() == 'A':
#             print("你去了游戏厅")
#             print("一个半小时到家,爸爸在家,拿棍子等着你")
#
#         elif Enter3.upper() == 'B':
#             print("你去了网吧")
#             print("两个小时到家,妈妈已经做好战斗准备")
#     else:
#         continue



#变量对比，猜大小
# from random import randint
# x = randint(1,100)
# count =1
#
# while count <= 3:
#     inputX = int(input("请输入随机数字: "))
#     if inputX < x:
#         print("猜小了!")
#     elif inputX > x:
#         print("猜大了")
#     else:
#         print("你猜对了")
#         break
#     count += 1


#34.猜大小
# from random import randint
# x = 66
# count = 1
# #确定值对比
# while count <= 3:
#     inputD = int(input("Please input digit: "))
#     if inputD < x:
#         print("guess smaller than it!")
#     elif inputD > x:
#         print("guess bigger than it!")
#     else:
#         print("guess right!")
#         break
#     count += 1

#upper方法的使用
# x = input("1: ")
# while True:
#     if x.upper() == 'Q':
#         print(x)
#         break
#     else:
#         print("Enter error!")
#         break



