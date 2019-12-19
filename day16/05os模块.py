#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''os模块'''
import os
import time

#创建多级目录
# os.makedirs("time/time/time/time")


#删除空目录
# os.removedirs("time/time/time/time")

# os.mkdir("os/os")
# os.rmdir("os/os")

# os.listdir("time")
# os.rename("time","timedir")

#调用系统指令
# os.system("dir")

#获取当前路径
# print(os.getcwd())

#切换目录
# os.chdir("../day15")
# print(os.listdir("./"))


'''os.path'''
# os.path.abspath("timedir")   #返回path规范化的绝对路径
# print(os.listdir("timedir"))   #列出目录中的文件和目录，返回一个列表


# print(os.path.split("Python Study/exampleOldboy/day16"))    #将全路径文件分割为全路径和文件名，返回一个元祖
# print(os.path.dirname("E:\文档 + 数据\Python Docs\Python Study"))  #从全路径中最后一个路径截断，获取前面部分

# print(os.path.basename("E:\文档 + 数据\Python Docs\Python Study"))   #从全路径中最后一个路径截断，获取后面部分


# print(os.path.exists("timedir"))   #判断目录是否存在  返回true和flase
# print(os.path.isabs("timedir"))   #判断目录是否是绝对路径 返回True和flase
# print(os.path.isfile("03time模块.py"))  #判断文件是否存在
# print(os.path.isdir("timedir"))  #判断path是否是一个目录，如果是返回true
# print(os.path.join("timedir","day16"))  #将多个路径组合返回，一般不用


# t = os.path.getatime("timedir")
# t1 = os.path.getmtime("timedir")
#
# st = time.localtime(t)  #在时间戳转换为标准时间时，需要用用localtime的这个功能
# st1 = time.localtime(t1)
#
# print(time.strftime("%Y-%m-%d %H:%M:%S",st))
# print(time.strftime("%Y-%m-%d %H:%M:%S",st1))


# print(os.path.getsize("../day16"))  #获取路径大小，不过值不准确


'''特殊属性'''
# os.sep  输出操作系统特定的分隔符，windows下为\\,linux下为/
# os.lineseo 输出当前平台使用的行终止符，windows下为\r\n，linux下为\n
# os.pathsep 输出用于分割文件路径的字符串，windows下为;,linux下为;
# os.name  输出字符串指示当前使用平台,windows->nt,linux->posix



os.stat()

st_mode: inode保护模式
st_ino: inode节点号
st_dev: inode驻留设备
st_nlink: inode的链接数
st_uid: 所有者的用户ID
st_git: 所有者的组ID
st_size: 普通文件以字节为单位的大小，包含等待特定文件的数据
st_atime: 上次访问的时间
st_mtime: 上次修改的时间
st_ctime: 由操作系统报告的ctime，在windows上是创建时间，在unix中是最新元数据修改的时间


