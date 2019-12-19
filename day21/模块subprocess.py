#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_


import subprocess
sub_obj = subprocess.Popen('dir', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

print(sub_obj.stdout.read().decode('gbk'))

# import os
# ip = os.popen("ipconfig")
# print(ip.read())


