#!/usr/bin/env python
#-*- coding: utf-8 -*-

#1.输出评委名单列表
# lst = []
# count = 1
# sum = 1
# while True:
#     content = input("Please input judges: ")
#     if content.upper() == 'Q':
#         break
#     lst.append(content)
#     for i in range(len(lst)):
#         print(i + 1,lst[i])
#     count += sum
#
# print(lst)

#2.输出电影评分
# lst2 = ["头号玩家","爱情公寓","一出好戏","西红柿首富"]
#
# dic = {}
# for el in lst2:
#     mark = input("输入电影<%s>的分数: " % el)
#     dic[el] = int(mark)
#
# print(dic)

#3.如有以下5个评委,让5个评委进行输入打分,要求分数必须大于5分,小于10分

# lst = ['赵四','刘能','王二麻','张三','小沈阳']
#
# for el in lst:
#     mark = int(input("Please Enter Grade: "))
#     if mark > 5 and mark < 10:
#         print(el,mark)
#     else:
#         print("Please Enter grade(5 - 10)!")

#4.念数字给出一个字典,在字典中标识出每个数字的发音,包括相关符号,然后由用户输入一个数字,让程序读出相对应的发音
#不需要语音print即可

# dic = {
#     "_": "fu",
#     "0": "ling",
#     "1": "yi",
#     "2": "er",
#     "3": "san",
#     "4": "si",
#     "5": "wu",
#     "6": "liu",
#     "7": "qi",
#     "8": "ba",
#     "9": "jiu",
#     ".": "dian"
# }
#
# num = input("请输入你要读的数字: ")
# s = ""
# for c in num:
#     s = s + dic[c] + " "
# print(s)


#5.车牌区划分,现给出以下车牌，根据牌的信息，分析出各省的车牌持有量
# dic = {}
# cars = ['鲁A32444','鲁B12333','湘B8989M','黑C46555','沪B25041','克A5678S']
# local = {
#     '沪': '上海',
#     '黑': '黑龙江',
#     '鲁': '山东',
#     '鄂': '湖北',
#     '湘': '湖南'
# }
#方法一
# for car in cars:
#     paitou = car[0]
#     if paitou not in local.keys():
#         continue
#     if dic.get(local[paitou]) == None:
#         dic[local[paitou]] = 1
#     else:
#         dic[local[paitou]] = dic[local[paitou]] + 1
# print(dic)

#方法二
# for car in cars:
#     paitou = car[0]
#     if paitou not in local.keys():
#         continue
#     num = dic.get(local[paitou], 0)
#     num += 1
#     dic[local[paitou]] = num
#
# print(dic)

#6.有如下主播信息,1计算主播，2删除收益小于平均值的主播
# zhubo = {'卢本伟': 122000,'冯提莫': 189999,'金老板': 99999,'吴老板': 25000000,'alex': 126}
# sumZ = len(zhubo)
# s = 0
#
# for value in zhubo.values():
#     s += value
# avg = s/sumZ
#
# print("以上主播收入平均值: %s" % avg)
#
# lst = []
# for k,v in zhubo.items():
#     if v < avg:
#         lst.append(k)
#
# for el in lst:
#     zhubo.pop(el)
#
# print(zhubo)