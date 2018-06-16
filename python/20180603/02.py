#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-03 18:51:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib2
# 设置请求头
ua_headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

# 通过urllib2.Request() 方法构造一个请求对象
request=urllib2.Request("http://www.baidu.com/",headers=ua_headers)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response=urllib2.urlopen(request)

# 服务器返回的类文件对对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html=response.read()

# 返回HTTP的响应码
print response.getcode()

# 返回 返回实际数据的页面url，防止重定向问题
print response.geturl()

# 返回 服务器响应的HTTp报头
print response.info()

# 打印响应的html
# print html


