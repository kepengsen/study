#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 15:09:36
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING],isGroupChat=True)
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    print msg.user
    print '___________user________________-'

    print msg.type
    print '___________type________________-'

    print msg['ToUserName']
    print '___________ToUserName________________-'
    
    
    print msg['Text']
    print '_____________Text______________-'
    
    print msg['User']['NickName']
    print '_____________NickName______________-'


def lc():
    print('finish login')
def ec():
    print('exit')

itchat.auto_login(loginCallback=lc, exitCallback=ec,hotReload=True)
time.sleep(3)
itchat.run()