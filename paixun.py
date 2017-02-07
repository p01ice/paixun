#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 20:13
# @Author  : r00t
# @Site    : 
# @File    : paixun.py
# @Software: PyCharm

li = [1,25,5,4,5,47,474,4774,58,8,4,2,41]

for j in range(1,len(li)):
    for i in range(len(li)-j):
        if li[i]>li[i+1]:
            temp = li[i]
            li[i] =li[i+1]
            li[i+1] =temp
print li
