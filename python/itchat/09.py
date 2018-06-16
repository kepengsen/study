#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 08:30:44
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


#获取所有微信好友头像，合成一个图片 

from numpy import *
import itchat
import urllib
import requests
import os

import PIL.Image as Image
from os import listdir
import math

itchat.auto_login()
# itchat.auto_login(enableCmdQR=2)

friends = itchat.get_friends(update=True)[0:]

user = friends[0]["UserName"]
uName = friends[0]["NickName"]
print(uName+'  -------  '+user)
print '获取头像中。。。'
os.mkdir(uName)
num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(uName + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

pics = listdir(uName)

numPic = len(pics)

print('一共获取到 '+str(numPic)+' 个头像')

eachsize = int(math.sqrt(float(640 * 640) / numPic))

print(eachsize)

numline = int(640 / eachsize)

toImage = Image.new('RGB', (640, 640))


print('每行显示个数：'+str(numline))

x = 0
y = 0

for i in pics:
    try:
        #打开图片
        img = Image.open(uName + "/" + i)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        #缩小图片
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        #拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1


toImage.save(uName + "_head_img.jpg")


itchat.send_image(uName + "_head_img.jpg", 'filehelper')
