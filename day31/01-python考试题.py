# 1.计算示例： 1-3+5-7+9-11.....99
'''方法一'''
# fu = 1
# sum = 0
#
# for i in range(1,100,2):
#     sum += fu * i
#     fu = -fu
# print(sum)

'''方法二'''
# sum = 0
# lst = []
# for i in range(1,100,2):
#     lst.append(i)
#
# for i in range(len(lst)):
#     if i % 2 == 0:
#         sum += lst[i]
#     else:
#         sum -= lst[i]
# print(sum)


# 2. 删除字典数据，工资低于平均工资的删除

# dic = {
#     '周杰伦': 8000,
#     '林俊杰': 5000,
#     'alex': 5,
#     '太白': 5,
# }
# sum = 0
# dic_len = len(dic)
#
# for k,v in dic.items():
#     sum += v
#
# mean = sum/dic_len
# lst = []
# for k,v in dic.items():
#     if v < mean:
#         lst.append(k)
#
# for i in lst:
#     dic.pop(i)
#
# print(dic)


# 3.有文件1.txt里面的内容为：
#     id,name,age,phone,job
#     1,alex,22,13631321317,IT
#     2,wusir,23,14314134154,Tearcher
#     3,taibai,18,13454352345,IT
#
# 使用文件操作，将其构造成如下数据类型：
#   [
#     {
#         'id': '1',
#         'name': 'alex',
#         'age': '22',
#         'phone': '13631321317',
#         'job': 'IT',
#     },
#
#     {
#         'id': '2',
#         'name': 'wusir',
#         'age': '23',
#         'phone': '14314134154',
#         'job': 'Tearcher',
#     },
#
#     {
#         'id': '3',
#         'name': 'taibai',
#         'age': '18',
#         'phone': '13454352345',
#         'job': 'IT',
#     },
# ]

# 代码实现：
# result = []
# with open('1') as f:
#     title = f.readline().strip().split(',')
#     for line in f:
#         line = line.strip()
#         lst = line.split(',')
#         dic = {}
#
#         for i in range(len(title)):
#             dic[title[i]] = lst[i]
#
#         result.append(dic)
#
# with open('2',mode='a',encoding='utf-8') as f2:
#     f2.write(str(result))
#     f2.close()


# 4.网络敏感词替换成*，敏感词['苍老师','东京热','武藤兰','波多野结衣','alex']
# lst = ['苍老师','东京热','武藤兰','波多野结衣','alex']
# lst2 = []
#
# while 1:
#     content = input('请输入你评论的内容: ')
#     if content.upper() == "Q":
#         break
#
#     for el in lst:
#         if el in content:
#             content = content.replace(el,'*'*len(el))
#     lst2.append(content)
#     print(content)
#
# print(lst2)

# 5.lst = [11,8,16,8,6,5,44,7,5,3] ，计算列表中所有质数的和

# lst = [11,8,16,8,6,5,44,7,5,3]
# li = []
# sum = 0
#
# for i in range(2,10):
#     li.append(i)
#
# for i in li:
#     for n in lst:
#         if n%i != 0:
#             sum += n
#     print(sum)
#     break


# 6.车牌区域划分，给出以下车牌和地点信息对比，根据车牌信息，分析出各省车牌持有数量
# cars = ['鲁A32444','鲁B12333','京B8989M','黑C46555','沪B25041','黑C34567']
# locations = {'沪':'上海','京':'北京','黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南'}


# cars = ['鲁A32444','鲁B12333','京B8989M','黑C46555','沪B25041','黑C34567']
# locations = {'沪':'上海','京':'北京','黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南'}
#
# result = {}
# for car in cars:
#     result[locations[car[0]]] = result.get(locations[car[0]], 0) + 1
#
# print(result)


# 7.按要求完成下列转化
# list1 = [
#     {'name':'alex','hobby':'抽烟'},
#     {'name':'alex','hobby':'喝酒'},
#     {'name':'alex','hobby':'烫头'},
#     {'name':'alex','hobby':'massage'},
#     {'name':'wusir','hobby':'喊麦'},
#     {'name':'wusir','hobby':'街舞'},
# ]
# 转化为list2
#
# list2 = [
#     {'name':'alex','hobby_list':['抽烟','喝酒','烫头','massage']},
#     {'name':'wusir','hobby_list':['喊麦','街舞']},
# ]
#
# list1 = [
#     {'name':'alex','hobby':'抽烟'},
#     {'name':'alex','hobby':'喝酒'},
#     {'name':'alex','hobby':'烫头'},
#     {'name':'alex','hobby':'massage'},
#     {'name':'wusir','hobby':'喊麦'},
#     {'name':'wusir','hobby':'街舞'},
# ]
#
# result = []
# for el in list1:
#     for new_el in result:
#         if el['name'] == new_el['name']:
#             new_el['hobby_list'].append(el['hobby'])
#             break
#     else:
#         result.append({'name': el['name'],'hobby_list': [el['hobby']]})
#
# print(result)





