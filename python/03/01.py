#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 14:46:15
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib2
import urllib
import json

# 爬去双色球历史开奖

url='http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice'

# 完整的headers
headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "Sites=_21; UniqueID=elqKe1qjTlDTUMUJ1528786915747; _ga=GA1.3.1401112782.1528786915; _gid=GA1.3.605956444.1528786915; _gat_gtag_UA_113065506_1=1; 21_vq=18",
        "Host": "www.cwl.gov.cn",
        "Referer": "http://www.cwl.gov.cn/kjxx/ssq/kjgg/"
    }

formdata={
	'name':'ssq',
	'issueCount':100
}
data = urllib.urlencode(formdata)

req=urllib2.Request(url,data=data,headers=headers)

res=urllib2.urlopen(req)

html=res.read()

# print html

with open("./双色球100期.json", "a") as f:
      f.write(html)

data=json.loads(html)

for item in data['result']:
	print u'第'+item['code']+u'期---红球: '+item['red']+u' 篮球: '+item['blue']+u'__________开奖日期: '+ item['date']




