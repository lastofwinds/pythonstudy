#!/usr/bin/env python
#-*- coding: utf-8 -*-

import master
#
# while True:
#     print("""it write a lot of funcs...:
#           eat
#           drink
#           sleep
#           """)
#     val = input("please Enter test func: ")
#
#     '''hasattr从对象中判断是否有这个功能'''
#     if hasattr(master,val):
#         '''getattr从对象中寻找功能'''
#         attr = getattr(master,val)
#
#         if callable(attr):
#             attr()
#         else:
#             print(attr)
#     else:
#         print("no the func...")

    # if val == 'eat':
    #     master.eat()
    # elif val == 'drink':
    #     master.drink()
    # elif val == 'sleep':
    #     master.sleep()
    # else:
    #     print("not found the func...")

# func = getattr(master,'eat')
# func()

'''setattr重置对象'''
# setattr(master,'eat',lambda x: x+1)
# print(master.eat)