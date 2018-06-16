#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11 17:03:10
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import itchat

itchat.auto_login(hotReload=True)

#获取微信好友列表，如果设置update=True将从服务器刷新列表
# friends = itchat.get_friends(update=True) 
# for i in friends:
#     print(i)


# 获取特定UserName的用户信息
# itchat.search_friends(userName='@abcdefg1234567')


# 获取备注、微信号、昵称中的任何一项等于name键值的用户 并打印第一个的UserName
# print itchat.search_friends(name=u'张亚坤')[0]['UserName']

# 获取名字中含有特定字符的公众号，返回值为一个字典的列表
print itchat.search_mps(name=u'小冰')[0]
itchat.send(u'你在干嘛？怎么不说话', toUserName=itchat.search_mps(name=u'小冰')[0]['UserName'])