#!/usr/bin/env python
# -*- coding: utf-8 -*-

#内置函数

# 1.反射相关:
#
# 2.面向对象相关:
#
# 3.基础数据类型相关:
#     3.1数字相关:
#         3.1.1数据类型: bool布尔值 int整数 float浮点数 complex复数
#         3.1.2进制转换: bin() oct()八进制 hex()十六进制
#         3.1.3数学运算: abs()求绝对值 divmod()取商和余数 round()四舍五入 pow(x,y)求x的y次幂,如果有三个值，最后一个数取余 sum() min() max()
#                 print(pow(2,3)) #8
#                 print(sum([1,2,3,4]))  #10求和sum中最多只可以接两个对象,所以使用列表括起来
#                 print(max(1,2,31,1,51)) #51取最大值
#                 print(min(1,2,0.1,10,2)) #0.1取最小值
#     3.2数据结构相关:
#         3.2.1序列:
#         3.2.2列表和元组:  list tuple
#         3.2.3相关内置函数:   reversed slice
#                 lst = [1,2,3,4,5]
#                 lst1 = reversed(lst)   #反转返回一个迭代器
#                 for el in lst1:
#                     print(el)
#
#                 st = "大家好,我是麻花腾"
#                 s = slice(1,-1,2)  #切片位置指定
#                 print(st[s])
#         3.2.4数据集合: 字典dict 集合set,冻结集frozenset
#         3.2.5相关内置函数: len() sorted() zip() filter() map() enumerate枚举 all() any()
#                lst = ["钢铁侠","蜘蛛侠","蝙蝠侠"]
#                for index,el in enumerate(lst):   #枚举函数拿到索引和元素
#                    print(index,el)
#
#                print(any([False,False,"linux"]))  #any遍历对象做or或者判断符用
#                print(any([False,[],{},0]))
#
#                print(all([False,False,"linux"]))  #all遍历对象做and判断符用
#
#                lst = ["中国","美国","俄罗斯","日本"]
#                lst2 = ["北京","华盛顿","莫斯科","东京"]
#                lst3 = ["烤鸭","炸鸡","黄油+面包","寿司"]
#
#                a = zip(lst,lst2,lst3)   #zip按位合并可迭代对象,返回元组
#                print("__iter__" in dir(a))
#
#                for el in a:
#                     print(el)

#      3.3字符串: str format bytes bytearyy memoryview ord chr astii repr
#             s = format(7,"b")   #传入一个数字转换成二进制
#             print(s)
#             print(type(s))
#
#             s = format(20000,"c")  #传入一个字符串,转换成unicode编码格式
#             print(s)
#
#             s = format(31,"x")  #把十进制转成十六进制
#             print(s)
#
#             s = format(31,"X") #把十进制转成十六进制,大小写区分
#             print(s)
#
#             s = format(1234568,"e")   #科学计数法，默认保留小数点后6位
#             print(s)
#             s = format(12345675465243,".9e")  #科学计数法可以指定保留小数点后9位
#             print(s)
#
#             s = format(0.1234568,"f")   #科学计数法，浮点数默认保留小数点后6位
#             print(s)
#             s = format(0.12345675465243,".9f")  #科学计数法可以指定保留小数点后9位
#             print(s)
#
#             bytes把字符串转换成bytes类型
#             bytearray() 返回一个数组，这个数字里的元素是可变的，并且每个元素的值的范围是(0-256)
#
#             ret = bytearray('周杰伦',encoding='utf-8')
#             print(ret[0],ret[1],ret[2],ret[3])
#             print(ret)
#
#             s = memoryview("麻花腾".encode("utf-8"))  #基本不使用
#             print("__iter__" in dir(s))
#
#             print(ord("国"))   #返回ASCII数值
#             print(chr(65))    #返回的是unicode数值，输入位置数值，找出对应字符
#
#             for i in range(65535):
#                 print(chr(i),end=" ")
#
#             s = "我叫\\ haha \周杰伦"   #repr输出对象完全信息
#             print(s)
#             print(repr(s))

#
# 4.作用域相关:locals() globals()
#
# 5.迭代器相关:range next() iter()
#
# 6.其他:
#     字符串类型代码执行:eval() exec() complie
#
#             s = "1+2+3"
#             res = eval(s)   #eval会扫描字符串类型中的数据进行还原
#             print(res)
#
#             content = input("please input digit calc: ")
#             res = eval(content)
#             print(res)
#
#             exec("1+2+3")  #exec execute执行，没有返回值，如果要实现返回值，必须是整套代码
#             exec("for i in range(10):print(i)")
#
#             compile()编译代码,将字符串类型的代码编译,代码对象能够通过exec语句来执行或者eval进行求值
#             参数说明:
#                 1.resource要执行的代码,动态代码片段
#                 2.文件名,代码存放的文件名,当传入第一个参数的时候,这个参数给空就可以
#                 3.模式取值有三个:
#                     3.1.exec: 一般放一些流程语句的时候
#                     3.2.eval: resource只存放一个求值的表达式
#                     3.3.single: resource存放的代码有交互的时候,mode应为single
#
#                     code1 = "for i in range(10):print(i)"
#                     c = compile(code1,"","exec")  #compile不光可以执行字符串还可以执行强注释内容
#                     exec(c)
#
#                     code2 = "1+2+3"
#                     c = compile(code2,"","eval")
#                     res = eval(c)
#                     print(res)
#
#                     code3 = "name = input('please Entry your Name: ')"
#                     c = compile(code3,"","single")
#                     exec(c)
#                     print(name)


#     输入输出相关: input() print()

#     内存相关: hash() id()

#     文件操作相关: open()

#     模块相关: __import__() #动态引入模块

#     帮助: help()

#     调用相关: callable()  #区分函数和普通变量

#     查看内置属性: dir()
