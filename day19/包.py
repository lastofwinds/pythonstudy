#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


# 包就是python中的一个个项目目录

# 一般引用都是
from urllib import request

# 在python2中 __init__.py是必须的，python3中可以没有这个文件
# 自己定义一个包，一定要给出一个__init__.py


# 创建包：
#     创建文件夹
#     创建__init__.py

import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
#
# l = []
#
# l.append(open('glance/__init__.py','w'))
#
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
#
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
#
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/modules.py','w'))

# map(lambda f:f.close(),l)



'''模块引入，需要找到包路径下的对象'''
'''方式一'''
# import glance.api.policy
# glance.api.policy.get()
#
#
# '''方式二'''
# from glance.api import policy
# policy.get()


# import glance  #引入glance时调用的是glance的 __init__.py,同样可以调用__init__中的函数
# glance.func1()
# glance.func2()

