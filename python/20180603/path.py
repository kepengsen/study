#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-03 23:33:50
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
path=os.getcwd()+'/test2'
print ("\033[7;30;40m\t"+path+"\033[0m")
print ("\033[27;31;40m\t"+path+"\033[0m")
print ("\033[0;32;40m\t"+path+"\033[0m")
print ("\033[1;32;40m\t"+path+"\033[0m")
print ("\033[22;33;40m\t"+path+"\033[0m")
print ("\033[4;34;40m\t"+path+"\033[0m")
print ("\033[24;35;40m\t"+path+"\033[0m")
print ("\033[5;36;40m\t"+path+"\033[0m")
print ("\033[25;37;40m\t"+path+"\033[0m")

print os.path.exists(path)

if not os.path.exists(path):
    # os.makedirs(path) 
    print '创建新目录成功'
else:
    print '目录已存在'


