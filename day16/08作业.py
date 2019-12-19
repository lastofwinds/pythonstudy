#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 1.回顾文件递归遍历



# 2.写一个copy函数,接受两个参数,第一个参数是源文件的位置,第二个参数是目标位置,将源文件copy到目标位置

def copy(source,dest):
    path = os.path.join(path,os.path.basename(source))
    with open(source,mode="rb") as f1, open(dest,mode="wb") as f2:
        for line in f1:
            f2.write(line)
