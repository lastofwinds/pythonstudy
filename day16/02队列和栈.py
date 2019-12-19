#!/usr/bin/env python
#-*- coding: utf-8 -*-


''''
    队列：先进先出
        在多线程中，队列顺序就不一定了
'''

import queue

# q = queue.Queue()
# q.put("刘伟")
# q.put("dayang")
# q.put("NICA")
#
# print(q.get())
# print(q.get())
# print(q.get())


'''
    栈：先进后出
'''
class StackFullError(Exception):
    pass

class StackEmptyError(Exception):
    pass

class Stack:

    def __init__(self,size):
        self.index = 0  # 栈项指针
        self.size = size
        self.lst = []  # 容器

    def push(self,el):
        if self.index < self.size:
            self.lst.insert(self.index,el)
            self.index += 1
        else:
            raise StackFullError("the stack is full.")

    def pop(self):
        if self.index > 0:
            self.index -= 1
            return self.lst[self.index]
        else:
            raise StackEmptyError("the stack is empty.")


s = Stack(5)
s.push("1")
s.push("2")
s.push("3")
s.push("4")
s.push("5")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())