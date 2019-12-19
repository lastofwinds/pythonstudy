#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''supper方法'''

# class Base1:
#     def func(self):
#         super().func()  #supper在多重继承时，使同名函数都可以调用
#         print("娃哈哈")
#
# class Base2:
#     def func(self):
#         print("雪碧")
#
# class Foo(Base1,Base2):  #在多重继承时，后有MRO,C3算法，根据继承的对象，从前往后排Foo,Base1,Base2
#     pass
#
# f = Foo()
# f.func()

'''
MRO方法路径顺序:
python2
    1.使用经典类(写继承关系的时候，基类不继承object)
    2.新式类(继承关系的根，是object)
python3
    只有新式类
'''


'''
经典MRO
    使用的是深度优先遍历
'''


'''
新式类MRO，C3
新式类中如果没有菱形继承(深度优先就可以了)
如果有菱形继承：使用C3算法来计算MRO
'''






