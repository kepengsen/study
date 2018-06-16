#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11 12:24:19
# @Author  : kepengsen (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)