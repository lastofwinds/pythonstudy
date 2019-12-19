#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# class Earth:
#     '''构造方法'''
#     def __init__(self):
#         print("init...")
#
#     ''''''
#     def __call__(self, *args, **kwargs):
#         pass
#
#     '''从对象中获取数据'''
#     def __getitem__(self, item):
#         print("I'm getitem: ",item)
#
#     '''在对象中设置数据'''
#     def __setitem__(self, key, value):
#         print(key,value)
#
#     '''在对象中删除key'''
#     def __delitem__(self, key):
#         print(key)
#
#     '''enter exit上下文标签管理: 为with服务的'''
#     def __enter__(self):
#         print("我是进入...")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("我是出来")
#
#
# if __name__ == '__main__':
#     obj = Earth()
#     # obj()       # 会默认执行__call__()
#     print(obj['mahuateng'])    # 从对象中获取数据 默认执行__getitem__()
#     obj.__setitem__('alex',18)
#     del obj['mahuateng']
#
# # dic = {'name':'汪峰','age':18}
# # print(dic['name'])
#
#     with obj:
#         print("你好,我是周润发")

# class Boy:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     '''返回这个对象的字符串表达形式'''
#     def __str__(self):
#         return "name: %s\tage: %s" % (self.name,self.age)
#
#     '''__new__创建对象'''
#     def __new__(cls, *args, **kwargs):
#         print("新概念")
#         return object.__new__(cls)   #创建对象
#
# b1 = Boy('alex',18)
# print(b1)  #默认打出对象类型


# 创建对象步骤：
# 1.加载类
# 2.开辟内存(__new__)
# 3.初始化(__init__)
# 4.使用对象


