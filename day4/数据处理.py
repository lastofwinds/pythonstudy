#!/usr/bin/env python
#-*- coding: utf-8 -*-

#join遍历列表,把列表中每一项用"_"拼接
# lst = ['汪峰','吴君如','李嘉欣','陈慧琳','关之琳']
# s = "_".join(lst)
# print(s)
#
# #split分割
# s1 = "汪峰_吴君如_李嘉欣_陈慧琳_关之琳"
# ls = s1.split("_")
# print(ls)

#remove和clear区别
# lst = ['汪峰','吴君如','李嘉欣','陈慧琳','关之琳']
# lst.clear()
# print(lst)
#结果[]，完全清除

# for el in lst:
#     lst.remove(el)   #在循环体中有迭代过程,删除列表数据时会进行标记,元素向前位移，索引标记就会不准
# print(lst)
#结果['吴君如', '陈慧琳']，未完全清除

# new_lst = []
# for el in lst:
#     new_lst.append(el)
# for el in new_lst:
#     lst.remove(el)   #根据值删除
# print(lst)

#删除以张开头的数据
# lst = ['张三丰','张无忌','林冲','李逵','张飞','鲁智深']
# lst2 = []
# for el in lst:
#     if el.startswith('张'):
#         lst2.append(el)
#
# for el in lst2:
#     lst.remove(el)
# print(lst)

#删除
# dic = {'谢逊': '金毛狮王','韦一笑': '青翼蝠王','殷天正': '白眉鹰王','金花婆婆': '紫衫龙王'}
# for k in dic:
#     dic['谢逊'] = '张无忌义父'
# print(dic)

#fromkeys方法
# d = {}
# dd = d.fromkeys('马化腾','周杰伦')  #创建新字典
# print(dd) #新的字典通过第一个参数迭代，和第二个参数组合成key:value创建新字典
# 结果{'马': '周杰伦', '化': '周杰伦', '腾': '周杰伦'}

# d = {}
# dd = d.fromkeys(['ben','aich','cecl'],18)  #value唯一,key可以多个
# print(dd)

#数据类型转换
# lst = ['张三丰','张无忌','林冲','李逵','张飞','鲁智深']
# tu1 = tuple(lst)
# print(tu1)
#
# lst1 = list(tu1)
# print(lst1)

#set集合,可以自动去重，好比只存key的字典,集合是可迭代对象
# lst = [1,2,3,4,4,4,4,55,6,7,5,7,7]
# s = set(lst)
# lst = list(s)
# print(lst)

#集合增加元素
# s = {'赵本山','范伟','小沈阳','宋小宝'}
# s.add('赵刚')
# s.add('李云龙')
# s.add('二营长')
# s.add('张大彪')
# # print(s)

#集合update
#错误添加
# s.update('钢板日穿')  #在update时，必须用元组格式的数字添加，否则update会对字符串遍历
# print(s)
#正确添加
# s.update(('钢板日穿','小泽','苍老师'))
# print(s)

# item = s.pop()  #随机删除
# print(item)

# s.remove('小泽')  #指定删除
# print(s)

#集合常用操作
#交集
# s1 = {1,2,3,4,5}
# s2 = {2,3,6,7,8}
# print(s1 & s2)  #求交集
# print(s1.intersection(s2)) #求交集

#并集
# print(s1 | s2)   #求并集
# print(s1.union(s2))  #求并集

#差集
# sx = s1 - s2
# print(s1.difference(s2))
# sy = s2 - s1
#
# for i in sy:
#     sx.add(i)
# print(sx)


#反交集
# s1 = {1,2,3,4,5,4,7}
# s2 = {2,5,8,9,1}
#
# print(s1 ^ s2)  #取出两个集合单独存在的数据
# print(s1.symmetric_difference(s2))

