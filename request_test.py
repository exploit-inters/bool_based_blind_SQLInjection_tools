#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Xuchao

import requests

url = 'https://www.baidu.com'
r = requests.get(url)
# print(r.text)
# print(r.headers)
# print(r.cookies)
# print(r.status_code)
dic = {
    'data':'1'
}
r = requests.post(url,data=dic)
print(r.text)