#/usr/bin/env python
# -*- coding: utf-8 -*-


#内存地址查看id方法
# a = [ "groupops", "groupdev", "groupprod" ]
# b = a
# print(id(a))
# print(id(b))


#== 和 is 的区别
#== 比较的是值(内容) True
#is 比较的是内存地址(寻找一个对象) False
#如果是字符串或者同一变量时，值和对象为True
# a = [ 123, 456 ]
# b = [ 123, 456 ]
# print(a == b)
# print(a is b)


#手动指定缓存内容
# from sys import intern intern()


#字符集编码
# 1. ASCII: 8bit 1byte 英文字母 数字 特殊字符
# 2. GBK: 18bit 2byte 主要是存中文 日文 韩文 繁体字 中文特殊字符
# 3. UNICODE: 32byte 4byte
# 4. UTF-8: 可变长度的unicode
#     英文: 8bit, 1byte
#     欧洲文字: 16bit, 2byte
#     中文: 24bit, 3byte
# 5. GBK和utf-8不能直接互换,需要转码

# 1. 编码,把unicode转换成utf-8
# s = "李时珍皮"
# abc = s.encode("UTF-8")   #encode之后的结果是bytes类型, 依然是原来的字符串
# print(abc)

# 2. 解码
# abc = b'\xe6\x9d\x8e\xe6\x97\xb6\xe7\x8f\x8d\xe7\x9a\xae'
# s = abc.decode("UTF-8")
# print(s)

# 3. GBK编码解码
# abc = "陈独秀"
# print(abc.encode("GBK"))
# abc1 = b'\xb3\xc2\xb6\xc0\xd0\xe3'
# print(abc1.decode("GBK"))     #GBK编码不能使用UTF-8

# 4. GBK解码成UTF-8
# abc = b'\xb3\xc2\xb6\xc0\xd0\xe3'
# s = abc.decode("GBK")
# abc2 = s.encode("UTF-8")
# print(abc2)
# abc3 = abc2.decode("UTF-8")
# print(abc3)



