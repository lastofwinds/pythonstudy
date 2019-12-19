#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''正则表达式'''

# 1.字符组
# [a-z][A-Z][0-9]

# 2.简单元字符

# . 匹配除换行符以外的任意字符
# \w 匹配字母或数字或下划线
# \s 匹配任意的空白字符
# \n 匹配一个换行符
# \t 匹配一个制表符
# \b 匹配一个单词的结尾
# ^ 匹配字符串的开始
# \c 匹配一个制表符
# \d 匹配数字
# $ 匹配字符串的结尾
# \W 匹配非字母数字下划线
# \D 匹配非数字
# \S 匹配非空白字符
# a|b 匹配字符a或者b
# () 匹配括号内的表达式，也表示一个组
# [...] 匹配字符组中的字符
# [^...] 匹配除了字符组中的字符以外的所有字符



# 3.量词
# * 重复零次或更多次
# + 重复一次或更多次
# ? 重复零次或一次,也就是在前面的字符出现多次的时候，只匹配一个
# {n} 重复n次
# {n,}重复n次或更多次
# {n,m} 重复n到m次



# 3.练习
# 1.findall方法：查找所有结果

import re

lst = re.findall("a","abcabcdcdsfds")
print(lst)


# 2.finditer查找到的结果返回一个迭代器

it = re.finditer(r"\d+","阮28号收入了3000块")
for el in it:
    print(el.group())

# 3.search会进行匹配，但是如果匹配到第一个结果，就会返回这个结果，如果匹配不到search返回的则是None

ret = re.search("a","abac")
print(ret.group())

# 4.match()
ret2 = re.match("a","abcda")
print(ret2.group())

# 5.split 切割按照正则切割
lst2 = re.split(r"[ab]","abcfdasfeafasdde")
print(lst2)


# 6.sub replace替换操作
result = re.sub("150","__sb__","alex150fdsaf150wusir250dasfdas150ritian")
print(result)

