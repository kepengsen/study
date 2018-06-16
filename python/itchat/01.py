#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 15:54:47
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)

itchat.auto_login(True)
itchat.run()

