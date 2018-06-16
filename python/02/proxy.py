#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-07 14:14:29
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib2

# authproxy_handler = urllib2.ProxyHandler({"http" : "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
authproxy_handler = urllib2.ProxyHandler({"http" : "115.239.51.147:	9000"})

# 构建一个自定义的opener
opener = urllib2.build_opener(authproxy_handler)

# 构建请求
request = urllib2.Request("http://www.baidu.com/")

# 获取响应
response = opener.open(request)

print response.read()
