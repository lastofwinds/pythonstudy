#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_

import re
# 1.eval exec compile

# 1.1exec识别出字符串中的变量
# exec("for i in range(10):print(i)")


# 1.2compile
# obj = re.compile(r"\d+")
# lst = obj.findall("大秧歌昨天赚了5000")
# lst2 = obj.findall("银行流水5000,花了6000")
# print(lst)
# print(lst2)


#findall匹配取出匹配对象
# lst3 = re.findall(r"\d+","大秧歌昨天赚了5000")
# lst4 = re.findall(r"\d+","银行流水5000,花了6000")
# print(lst3)
# print(lst4)

# ret = re.findall("www.(baidu|oldboy).com","www.oldboy.com")
# print(ret)


#?:不分组，直接对对象进行匹配
# ret1 = re.findall("www.(?:baidu|oldboy).com","www.oldboy.com")
# print(ret1)


# split
# 匹配时以匹配对象为分隔符
ret = re.split("\d+","eva3feafr4yuan")
print(ret)

# 匹配时保留分隔符
ret1 = re.split("(\d+)","eva3feafr4yuan")
print(ret1)



