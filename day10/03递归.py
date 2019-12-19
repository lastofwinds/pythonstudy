#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归
#     自己调用自己

#         def func():
#             print("我叫李嘉城")
#             func()
#
#         func()
#
#         import sys
#         sys.setrecursionlimit(3000)   #设置递归深度,一般使用默认
#
#         def func(index):
#             print(index)
#             func(index + 1)
#         func(1)

# 二叉递归(此处为伪代码)
#         def func(root):
#             left = root.left
#             right = root.right
#
#             func(left)
#             func(right)

# 递归练习
# 遍历文件夹
#         import os
#         def func(file_path,ceng):
#             #listdir获取路径下的所有文件
#             lst = os.listdir(file_path)
#             for file in lst:
#                 fullpath = os.path.join(file_path,file)
#                 if os.path.isdir(fullpath):
#                     print("\t"*ceng,file)
#                     func(fullpath,ceng +1)
#                 else:
#                     print("\t"*ceng,file)
#         func(r"E:\360驱动大师目录",0)
