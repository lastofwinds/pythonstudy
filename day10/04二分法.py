#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 二分法
# 练习一
#
#         lst = [1,8,16,32,55,78,89,1,5,4,7,21,123,21,23,7,12,32]
#
#         lst = sorted(lst)
#         print(lst)
#
#         n = int(input("please enter a digit: "))
#         left = 0
#         right = len(lst) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#             if n > lst[mid]:
#                 left = mid + 1
#             elif n < lst[mid]:
#                 right = mid - 1
#
#             else:
#                 print("in the list location %s" % mid)
#                 break
#         else:
#             print("the digit in the seq.")



# 练习二
#
#         lst = [1,2,3,4,5,7,10,11,13]
#
#         def func(n,lst):
#             left = 0
#             right = len(lst) -1
#             if left <= right:
#                 mid = (left + right) // 2
#                 if n > lst[mid]:
#                     new_list = lst[mid+1:]
#                     return func(n,new_list)
#                 elif n < lst[mid]:
#                     new_list = lst[:mid]
#                     return func(n,new_list)
#                 else:
#                     print("刚刚好,出现在这里")
#                     return True
#             else:
#                 return False
#
#         ret = func(13,lst)
#         print(ret)


# 练习三
# lst = [1,2,3,4,5,7,10,11,13]
# def func(n,lst,left,right):
#     if left <= right:
#         mid = (left + right) // 2
#         if n > lst[mid]:
#             left = mid + 1
#         elif n < lst[mid]:
#             right = mid - 1
#         else:
#             return True
#         return func(n,lst,left,right)
#     else:
#         return False
#
# ret = func(6,lst,0,len(lst)-1)
# print(ret)



