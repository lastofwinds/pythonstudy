#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


'''打包工具struct'''

import struct

num = 156
'''将Int类型数据打包成4个字节的数据'''
num_stru = struct.pack('i',num)  #打包

print(len(num_stru))
print(num_stru)

num2 = struct.unpack('i',num_stru)  #解包
print(num2)
print(num2[0])

