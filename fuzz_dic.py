#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 下午 10:12
# @Site    : 
# @File    : fuzz_dic.py
# @Software: PyCharm
# @Author: Xuchao

f = open('fuzz_dic.txt','w')
for i in range(33,127):
    print(chr(i))
    f.write(str(chr(i)))
    f.write('\n')
f.close()

#先跑一下intruter，看看过滤了什么
