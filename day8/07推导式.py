#推导式
# 列表：装python1期，python2期...
#列表推导式
# lst = ["python%s" % i for i in range(1,10)]
# print(lst)


#获取100以内的能被3整除的数
# lst = [i for i in range(1,101) if i%3 == 0]
# print(lst)
# #获取100以内3整除数的平方
# lst1 = [i*i for i in range(1,101) if i%3 == 0]
# print(lst1)
#
# #寻找名字中带有两个e的人的名字
# names = [['tom','billy','jefferson','andrew','wesley','steven','joe'],['alice','jill','ana']]
# lst2 = [ name for first in names for name in first if name.count("e") >= 2 ]
# print(lst2)


#字典推导式,{key:value for 循环 if 赛选}
# dic = {"a": "123","b": "456","c": "789"}  #基本不使用
# d = { dic[k]: k for k in dic }
# print(d)

# 实例一：
# lst1 = ["东北","陕西","山西"]
# lst2 = ["大拉皮","油泼面","老陈醋"]
#
# dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
# print(dic)

#集合推导式{"1","2","3"}
# lst = ["周杰伦","周润发","周伯通"]
# s = {el for el in lst}
# print(s)

# 列表推导式与生成器表达式的优缺点

# 生成器表达式:记录一下代码，然后每次需要的时候去生成器中执行一次这个代码
#     1.节省内存
#     2.惰性机制
#     3.只能向前

# 列表推导式：一次性把所有数据创建出来，容易产生内存溢出

#生成器调用方式
# def func():
#     print(111)
#     yield 222
#
# g = func()
#
# g1 = (i for i in g)   #生成器执行完后，会释放内存
# g2 = (i for i in g1)
#
# print(list(g))
# print(list(g1))
# print(list(g2))
