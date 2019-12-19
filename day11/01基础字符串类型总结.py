#!/usr/bin/env python
#-*- coding: utf-8 -*-

# 字符串格式化第一种方法
# name = 'alex'
# xingge = 'sb'
# age = 18
#
# info = "姓名: %s 性格: %s 年龄: %s" % (name,xingge,age)
# print(info)


#字符串格式化第二种方法
# name = 'alex'
# xingge = 'sb'
# age = 18
#
# info = f"姓名: {name} 性格: {xingge} 年龄: {age}"  #format方法,python3.6以上版本支持
# print(info)


#索引和切片
# 索引
# [0]
# [1]
# [-1]


# 切片
# [start,end,step]
# s = "linux is good and be friendly to programmers."
# print(s[1:10:2])
# print(s[-1::-2])


# 方法
# upper() 转换成大写
# strip() 去掉左右两端的空白
# replace(old,new) 把old换成new
# split() 切割，默认按照空白切割，切完后结果是列表
# join() 把元素拼接
# startswith() 以***开头
# find()/count()/index() 查找
# isdigit() 判断数字
# len() 长度
# encode(编码集)编码
#     1.ASCII. 8bit  1byte
#     2.GBK. 16bit 2byte 国标码. GB2312
#     3.unicode.万国码. 23bit 4byte
#     4.utf-8. 可变长度的unicode.
#             英文: 1byte
#             欧洲: 2byte
#             中文: 3byte
#     编码之后的数据bytes
#         bytes.decode()解码
# ...


# 列表方法
# 1.增
#     append() 追加
#     insert(index,data) 插入数据
#     extend(Iterable) 迭代添加
#
# 2.删除
#     pop()
#     remove(元素)
#     del 切片删
#     clear() 清空
#
# 3.修改
#     index切片修改
#     lst[i] = "新元素"
#
# 4.查询
#     一般根据index查询
#     for循环
#
# 5.操作
#     count() 计数
#     index() 查找元素
#     sort() 排序
#     reverse() 翻转

# 列表不能直接在循环中删除，因为涉及到元素移动，
# 需要把要删除的内容添加到新列表中，循环新列表，删除老列表


# 拷贝：
#     1.= 赋值操作，没有创建对象，两个变量使用同一个对象
#     2. 浅拷贝，只拷贝一层
#     3. 深拷贝，和这个对象相关的内部信息全部拷贝一份，deepcopy()原型模式


# 推导式：[结果 for循环 if判断]


# 字典：
    # 由{}表示，内部存储key:value,key是可hash对象（不可变数据），value没有限制
    # 字典没有索引和切片
    #
    # 1.增
    #     dic[新key] = value
    #     dic.setdefault(key,value)
    #
    # 2.删除
    #     pop(key)
    #     popitems() 随机删除一个
    #     del
    #     clear() 清空
    #
    # 3.修改
    #     dic[老key] = 新value
    #     dic.update({}) 把***字典跟新到字典中
    #
    # 4.查询：
    #     通过key来查询
    #     get(key,default)
    #     setdefault(key,value)
    #
    # 5.常用操作
    #     keys() 获取所有的key
    #     values() 获取所有的value
    #     item() 获取所有的k,v
    #     fromkeys() 多个key公用一个value


# 元组：
#     不可变
#     不可变指的是第一层
#     方法：
#         count
#         index
#         __iter__
#         len
#         __init__


# 集合
#     无序，不重复，可哈希(元素)
#     去重
#     fronzenset()


# print语句
#     sep=分隔符

# print("刘德华","高明宏","梁朝伟",sep="|")


