#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-03 20:48:43
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2

url="http://www.baidu.com/s"

header={'User-Agent':"Mozilla..."}

wd=urllib.urlencode({"wd":raw_input("请输入要查询的字符串")})

fullurl=url+"?"+wd

print fullurl

request=urllib2.Request(fullurl,headers=header)

response=urllib2.urlopen(request)

# print response.read()



