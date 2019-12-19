#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''日志处理：引入logging模块'''

import logging

# basicConfig只能用于单一日志输出配置
# 日志基础配置
# logging.basicConfig(filename='app.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=0   #level设置级别，当你的信息的级别>=level的时候，才会写入日志
# )
#
# logging.critical("我是critical，级别高的错误输出")
# logging.error("刘伟，你在干什么？住手")
# logging.warning("我是警告.")
# logging.info("我叫信息")
# logging.debug("我是调试")
# logging.log(2,"自定义")


'''logging测试一'''
# import traceback  #引入获取堆栈模块
#   #引入日志处理模块
# for i in range(100):
#     try:
#         if i % 3 == 0:
#             raise FileNotFoundError("我是FileNoteFoundException...")
#         elif i % 3 == 1:
#             raise StopIteration()
#         elif i % 3 == 2:
#             raise KeyError()
#
#     except FileNotFoundError as e:
#         val = traceback.format_exc()
#         logging.error(val)
#
#     except StopIteration as e:
#         val = traceback.format_exc()
#         logging.error(val)
#
#     except KeyError as e:
#         val = traceback.format_exc()
#         logging.error(val)
#
#     except Exception as e:
#         val = traceback.format_exc()
#         logging.error(val)



# 多文件日志处理

'''FileHandler多日志处理'''

# 创建一个操作日志的对象logger(依赖FileHandler)
# file_handler = logging.FileHandler('l1.log','a',encoding='utf-8')
# file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))
# logger1 = logging.Logger('A',level=40)
# logger1.addHandler(file_handler)
# logger1.error("我是A系统")
#
#
# # 再创建一个操作日志的对象logger(依赖FileHandler)
# file_handler = logging.FileHandler('l2.log','a',encoding='utf-8')
# file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))
# logger2 = logging.Logger('B',level=40)
# logger2.addHandler(file_handler)
# logger2.error("我是A系统")








