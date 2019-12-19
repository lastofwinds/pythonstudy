#1.字典中3人分别有电话和地址，利用输入的方法，如果用户存在，给出两个选项 该人的电话或者地址？
# people = {
#     'paul': {
#         'addr' : 'foo drive 23',
#         'phone': '2341'
#     },
#     'beth': {
#         'addr': 'bar street 42',
#         'phone': '9102'
#     },
#     'cecil': {
#         'addr': 'baz avenue 90',
#         'phone': '6780'
#     }
# }
#
# Labels = {
#     'addr': 'address',
#     'phone': 'phone number'
# }
#
# nameInput = input("Please the name: ")
# InfoChoice = input("Please Enter address(a) or phone(p): ")
#
# if InfoChoice.upper() == 'P':
#     key = 'phone'
# if InfoChoice.upper() == 'A':
#     key = 'addr'
#
# if nameInput in people:
#     print ("%s's %s is %s." % (nameInput, Labels[key], people[nameInput][key]))


#2.字典直接用key放入value
# dic = {}
# dic['徐峥'] = '人在囧途'
# print(dic)
#
# dic['黄渤'] = '疯狂的石头'
# print(dic)
#
# dic['王宝强'] = '天下无贼'
# print(dic)

#如果key已经存在，会替换掉原来的value
# dic['王宝强'] = '士兵突击'
# print(dic)


#3.setdefault字典中设置默认key,如果使用setdefault使key存在，下次则不会替换
# dic.setdefault("黄秋生")
# print(dic)
#
# dic.setdefault("黄秋生","头文字D")
# print(dic)


#4.字典删除
# dic = {
#     "黄日华": "天龙八部",
#     "吕颂贤": "笑傲江湖",
#     "苏有朋": "倚天屠龙记",
#     "六小龄童": "西游记"
# }
#
# dic.pop("吕颂贤")  #指定索引删除
# print(dic)
#
# dic.popitem()   #随机删除
# print(dic)
#
# del dic["苏有朋"]   #del方法删除
# print(dic)
#
# dic.clear()   #clear清空
# print(dic)


#5.字典修改
# dic = {
#     "刘能": "王小利",
#     "赵四": "刘晓光",
#     "王木生": "范伟",
#     "谢大脚": "于月仙",
#     "李大国": "小鬼"
# }
#
# dic["王木生"] = "刘伟"  #根据key = value修改
# print(dic)
#
# dic2 = {
#     "刘能": "大阳哥",
#     "赵四": "github",
#     "王木生": "汪峰",
#     "谢大脚": "冯提莫",
#     "王大拿": "金老板"
# }
#
# dic.update(dic2)     #根据集合方法更新到dic1中，如果有相同的则替换
# print(dic)


#6.字典查询
# dic = {'刘能': '大阳哥', '赵四': 'github', '王木生': '汪峰', '谢大脚': '冯提莫', '李大国': '小鬼', '王大拿': '金老板'}
# print(dic['刘能'])    #调key取value
# print(dic['周杰伦'])     #当key不存在时,报key错
#
# print(dic.get('赵四'))   #get方法获取key取value
# print(dic.get('周杰伦'))   #当key不存在时，报None空


#字典本身是一个可迭代对象
#字典查询
# dic = {}
# dic["盖伦"] = "德玛西亚之力"
# value = dic.setdefault("菲奥娜","无双剑姬")     #在没有key value的情况下，新增行为
# value2 = dic.setdefault("盖伦","德玛西亚之力")   #在已有key value的情况下，新增不执行，直接执行查询
#
# print(value)
# print(value2)
# print(dic)


#按位赋值，变量必须与后面值的数量一致
# a,b = 10,20
# print(a,b)
# a,b = (10,20)    #解构，解包等同于上面做法
# print(a,b)


#字典处理
# dic = {
#     "汪峰": "1",
#     "周杰伦": "2",
#     "罗志祥": "3"
# }

# print(dic.keys())       #拿到key
# for key in dic.keys():
#     print(key)          #拿到key
#     print(dic[key])     #拿到value

# print(dic.values())     #拿到value
# for value in dic.values():
#     print(value)        #只能拿到value，无法获取key

#写法一
# print(dic.items())      #拿到的是key+value
# for item in dic.items():
#     print(item)         #拿到key+value的元组
#     print(item[0],item[1])   #拿到key+value的字符串

#写法二
# for item in dic.items():
#     k,v = item
#     print(k,v)     #拿到key+value的字符串

#写法三
# for k,v in dic.items():
#     print(k,v)       #拿到key+value的字符串

#可迭代的字典，取数据注意事项
# for item in dic:
#     print(item)        #循环遍历默认拿到的是字典中的key
#     print(dic[item])   #获取value


#嵌套示例二
# wf = {
#     "name": "汪峰",
#     "age": 48,
#     "成名曲": "春天里",
#     "wife": {
#         "name": "章子怡",
#         "age": 39,
#         "工作": "演员"
#     },
#     "children": [
#         {"num": "001", "name": "汪一", "hobby": "唱歌"},
#         {"num": "002", "name": "汪二", "hobby": "演戏"}
#     ]
# }
#
# print(wf['children'][1]["hobby"])
# print(wf["wife"]["工作"])
#
# wf["wife"]["age"] = wf["wife"]["age"] + 10
# print(wf["wife"]["age"])
#
# print(wf.keys())
# print(wf.values())

