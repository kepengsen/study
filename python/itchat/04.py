#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11 16:27:31
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 测试图灵

import itchat
import requests

apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key'    : '8edce3ce905a4c1dbb965e6b35c3834d', # 如果这个Tuling Key不能用，那就换一个
    'info'   : 'hello', # 这是发出去的消息
    'userid' : 'wechat-robot', # 这里你想改什么都可以
}
# 通过如下命令发送一个post请求
r = requests.post(apiUrl, data=data).json()

# 打印一下返回的值，看一下拿到了什么
print(r)