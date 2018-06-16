#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-12 09:43:00
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 给某个好友快速发消息

import itchat
itchat.auto_login(hotReload=True)

name=itchat.search_friends(name=u'路江彪')[0]['UserName']

print name

num=1

while num <= 100:
	
    itchat.send(u'你在干嘛？怎么不说话'+'_'*10+str(num), toUserName=name)
    num += 1


