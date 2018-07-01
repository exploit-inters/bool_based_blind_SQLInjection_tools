#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 下午 08:42
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Author: Xuchao
import sys
import time

for i in range(32,127):
    time.sleep(1)
    sys.stdout.write(chr(i))
    sys.stdout.flush()