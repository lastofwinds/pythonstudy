#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys

# sys.argv  #命令行参数List，第一个元素是程序本身路径
# sys.exit()  #退出程序，正常退出状态0，错误退出状态1
# print(sys.version)  #获取python解释程序的版本
# sys.path  返回模块的搜索路径,初始化时使用python的PATH环境变量
# sys.platform 返回操作系统的平台名称

#在运行时，给python传递的信息，调出执行程序的名称
print(sys.argv)


ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]


print(ip)
print(username)
print(password)