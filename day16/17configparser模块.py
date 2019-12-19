import configparser

conf = configparser.ConfigParser()
# conf["DEFAULT"] = {
#     "session-time-out":30,
#     "user-alive":60,
#     "connect-alive":10
# }
#
# conf["189-DB"] = {
#     "ip":"192.168.1.189",
#     "port":3306,
#     "user": "root",
#     "password": "123456"
# }
#
#
# conf["163-DB"] = {
#     "ip":"192.168.1.163",
#     "port":3306,
#     "user": "root",
#     "password": "123456"
# }
#
#
# f = open("db.ini",mode="w")
# conf.write(f)

# conf.sections() #获取到章节
# conf.read("db.ini")
# # print(conf.sections())
# print(conf['163-DB']['ip'])
#
#
# for k,v in conf['163-DB'].items():
#     print(k,v)


#改删操作
# conf.read("db.ini")
# conf['163-DB']['user'] = "admin"
# conf.write(open("db.ini",mode="w"))

# del conf['163-DB']['password']
# conf.write(open("db.ini",mode="w"))


#设置操作

# conf.read("db.ini")
# conf.set("163-DB","wangermazi","163")
# conf.write(open("db.ini",mode="w"))


#增加章节
# conf.read("db.ini")
# conf.add_section('175-REDIS')
# conf.write(open("db.ini",mode="w"))

