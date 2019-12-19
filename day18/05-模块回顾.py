#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


# 1.模块
#     import 模块
#     from 模块 import xxx
#
#     加载模块过程：
#         1.先去查看是否加载过该模块 顺序：内存-> 内置 ->sys.path
#         2.如果没有加载过，开辟一个名称空间
#         3.执行该模块中的代码，所有产生的变量/类/函数都放在名称空间中
#         4.给名称空间命名，使用as语法，可以给模块一个精简的别名
#
#     为一个自建模块导入多个模块：
#         import a,b,c 一次导入多个模块
#         from 模块  import a,b,c as xxx
#         from xxx import *

import re
import ssl
import json
from urllib.request import urlopen
import scrapy

headers = {'User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
content = urlopen("http://www.baidu.com").read().decode("utf-8")
obj = re.compile(r"<a href=(.*?)</a>", re.S)


print(obj.findall(content))

#
# obj = re.compile(r"\[<a .*?>日韩剧集专区</a>\]<a href='(?P<second_url>.*?)'>.*?</a>",re.S)
# obj.findall(content)

#
# second_content = urlopen('https://www.dytt8.net/html/gndy/dyzz/20191201/59435.html').read().decode("gbk")
#

