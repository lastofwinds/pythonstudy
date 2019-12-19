# wf = {
#     "name": "汪峰",
#     "age": 18,
#     "hobby": "抢头条",
#     "wife": {
#         "name": "子怡",
#         "age": 18,
#         "hobby":["唱歌","跳舞","演戏"]
#     }
#
# }
# print(wf["wife"]["hobby"])


#
# class Person:
#     def __init__(self,name,age,hobby,wife):
#         self.name = name



'''json.dumps方法：将字典转换为字符串'''
# import json
dic = {"a":"理查德姑妈","b":"找到你","c":"看不见的客人"}
# # s = json.dumps(dic)  #如果你的key超过了ascii范围，就会显示\uxxxxx
#
# s = json.dumps(dic,ensure_ascii=False)
# print(s,type(s))
#
#
#
# '''json.loads方法: 将字符串转换为字典'''
# dic1 = json.loads(s)
# print(dic1,type(dic1))


import json
# f = open("waimai.json", mode="w", encoding="utf-8")
#
# json.dump(dic, f, ensure_ascii=False)
# f.close()
#
# f = open("waimai.json",mode="r",encoding="utf-8")
# s = json.load(f)
# print(s,type(s))



#写入多个字典时，为了让数据逐行写入 所以必须用到json.dumps且换行
# lst = [{"菜1":"回锅肉"},{"菜2":"土豆丝"},{"菜3":"干锅豆腐"}]
#
# f = open("waimai.json", mode="w", encoding="utf-8")
# for i in lst:
#     s = json.dumps(i,ensure_ascii=False) + "\n"
#     f.write(s)
#
#
# f.flush()
# f.close()


# 读取json文本字典数据
# f = open("waimai.json", mode="r", encoding="utf-8")
#
# for i in f:
#     i = i.strip()
#     dic = json.loads(i)
#     print(dic)