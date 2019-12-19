#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
    引入模块hashlib
        md5特性：
            md5加密不可逆，需要解密
'''


import hashlib
#
# # 1.创建一个MD5对象
# obj = hashlib.md5(b"fdasfeajiofjdasoif")   #加盐
#
# # 2.把要加密的内容给md5
# obj.update("alex".encode("utf-8"))   #必须是字节
#
# # 3.获取密文
# val = obj.hexdigest()
# print(val)

def my_md5(val):
    obj = hashlib.md5(b"fdasfeajiofjdasoif")
    obj.update(val.encode("utf-8"))
    val = obj.hexdigest()
    return val

# 注册时，用md5进行加密，存储的是加密后的密文
username = input("请输入用户名: ")
password = input("请输入密码: ")

cun = my_md5(password)
print(cun)

if username == 'alex' and my_md5(password) == 'ab4eb1ecd8e1e60cf5ac6eb6145c2709':
    print("登录成功")
else:
    print("登录失败")

