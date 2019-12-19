#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
    shelve提供python的持久化操作，就是将数据写入磁盘，小数据库，字典格式数据，写入数据时会生成几个文件
'''


# import shelve
#
# f = shelve.open("大阳哥",writeback=True)
#
# f['jj'] = "林俊杰"
# f['dyg'] = "大阳哥"
# f['xsy'] = "小沈阳"


# f["jay"] = "周杰伦"
# f.close()
# print(f["jay"])


# f['jay'] = {'name':"周杰伦",'age':38,"hobby":"song"}
# print(f['jay']['name'],f['jay']['age'])


# 注意：shelve中字典格式数据修改
# f['jay']['name'] = "周润发"   #修改字典数据，需要把内存数据回写到磁盘，然后磁盘更改数据才会生效，也就是上面writeback参数功能
# print(f['jay']['name'])

# f = shelve.open("大阳哥")
# print(f.keys())
# for key in f.keys():
#     print(key)
#
# for key in f:
#     print(key)
#
# for k,v in f.items():
#     print(k,v)




# shelve练习:
import sys
import shelve

def store_person(db):
    '''query user for  data and store it in the shelf object'''

    pid = input("Enter unique ID number: ")
    person = {}
    person['name'] = input("Enter name: ")
    person['age'] = input("Enter age: ")
    person['phone'] = input("Enter phone number: ")
    db[pid] = person


def lookup_person(db):
    '''query user '''
    pid = input("Enter ID number: ")
    field = input("what would you like to know? (name, age, phone) ")
    field = field.strip().lower()
    print(field.capitalize() + ":", db[pid][field])

def print_help():
    print("The available commands are:")
    print("store: Stores information about a person")
    print("lookup: Looks up a person from ID number")
    print("quit: save changes and exit")
    print("?: Print this message")

def enter_command():
    cmd = input("Enter command (? for help) ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open("./database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__': main()

