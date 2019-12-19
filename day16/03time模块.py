#!/usr/bin/env python
#-*- coding: utf-8 -*-


import time

#格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))

#结构化时间
# st = time.localtime()
# print(st)
#
# #格式化结构时间
# t = time.strftime("%Y-%m-%d %H:%M:%S",st)
# print(t)


#用户输入一个时间 2018-09-08 11:22:36  -存储 时间戳
#先把格式化时间转化成结构化时间
#
# s = "2018-09-08 11:22:36"
# st = time.strptime(s,"%Y-%m-%d %H:%M:%S")
# print(st)
#
#
# #把结构化时间转换成时间戳
# t = time.mktime(st)
# print(t)

while 1:
    s = time.strftime("%Y-%m-%d %H:%M:%S")
    print(s)
    time.sleep(1)

