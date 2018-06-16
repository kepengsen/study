#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 10:30:49
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

#获取好友签名
#用jieba分词，然后制作成词云，首先要安装jieba和wordcloud库
#pip install jieba
#pip install wordcloud

import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image

# 先登录
itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
uName = friends[0]["NickName"]
tList = []
for i in friends:
	# 获取个性签名
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    print signature
    tList.append(signature)

# 拼接字符串
text = "".join(tList)
# jieba分词
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)
# wordcloud词云
mypath = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(mypath, "wechat.jpg")))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf')\
    .generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片 并发送到文件助手
my_wordcloud.to_file(os.path.join(mypath, uName+"_Signature.png"))
itchat.send_image(uName+"_Signature.png", 'filehelper')
print 'over'
