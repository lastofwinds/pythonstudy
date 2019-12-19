#!/usr/bin/env python
#-*- coding: utf-8 -*-


import handle
import re
def func():
    objs = []
    name_list = dir(handle)
    new_list = []

    '''方法一'''
    # for el in name_list:
    #     if el.startswith("__") and el.endswith("__"):
    #         new_list.append(el)
    #
    # for el in new_list:
    #     name_list.remove(el)


    '''
        方法二
            下方必须使用list将对象转换成可迭代对象，否则只会返回一个对象类型    
    '''
    print(list(filter(lambda s: not s.startswith("__"),name_list)))

    '''
        getattr访问对象属性: 模块也可以成为一个对象，模块中的类也是对象，类中的函数也是对象
            getattr(class,def)
            getattr(module,class)
        hasattr判断对象的属性是否存在,如果存在返回True，如果不存在返回False，用法与getattr相同
        setattr顾名思义设置对象属性，可以给对象增加属性，一般针对构造函数的属性设置，或者字典类型数据
            setattr(对象class或者函数def...,'属性name','属性value')
    '''

    # base_sub_list = []
    # for name in name_list:
    #     cls = getattr(handle,name)
    #     if issubclass(cls,getattr(handle,"Base")) and cls != getattr(handle,"Base"):
    #         base_sub_list.append(cls())
    # print(base_sub_list)

if __name__ == '__main__':
    func()


