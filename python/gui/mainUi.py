#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-15 16:25:36
# @Author  : 243825348 (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
import itchat
from itchat.content import *
import datetime
import time
import os
# import top.api
import requests
import json
import re
from urllib.request import urlretrieve

current_path = os.path.dirname(os.path.abspath(__file__))

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

    '''
        程序默认UI界面信息
    '''
    def iniUI(self):
        self.setWindowTitle("州的先生淘宝客微信机器人v0.1")
        self.resize(1200, 600)

        self.vertical_box_layout()
        # 用于存放群聊列表元素
        self.chatroom_list = []
        self.current_date = datetime.datetime.strftime(datetime.datetime.today(),'%Y-%m-%d')

        # 设置程序图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
     

    # 水平垂直布局
    def vertical_box_layout(self):
        '''
            上层功能盒子
        '''
        # 创建一个用于存放登录相关按钮的窗口部件
        login_buttons = QWidget()
        login_buttons_box = QVBoxLayout()
        # 设置窗口部件的布局为垂直盒子布局
        login_buttons.setLayout(login_buttons_box)

        # 创建两个登录相关的按钮
        self.refresh_button = QPushButton("点击登录")
        self.exit_button = QPushButton("退出登陆")
        self.exit_button.setEnabled(False)
        # 将按钮添加到窗口部件中
        login_buttons_box.addWidget(self.refresh_button)
        login_buttons_box.addWidget(self.exit_button)

        # 创建一个登录按钮的组盒子
        login_box = QGroupBox()
        login_box.setTitle("登陆选项")
        # 设置登陆盒子布局为网格布局
        login_box_layout = QGridLayout()
        login_box.setLayout(login_box_layout)
        # 将按钮窗口部件添加到网格布局中
        login_box_layout.addWidget(login_buttons,0,1)

        # 创建群聊列表子盒子
        chatroom_box = QGroupBox()
        chatroom_box.setTitle("群聊列表")
        # 创建群聊列表的垂直布局层
        chatroom_box_layout = QVBoxLayout()
        # 设置群聊列表子盒子的布局层
        chatroom_box.setLayout(chatroom_box_layout)
        # 创建一个群聊部件
        scroll_widget = QWidget()
        # 创建群聊不见的布局层
        self.scroll_widget_layout = QVBoxLayout()
        # 设置群聊不见的布局层为self.scroll_widget_layout
        scroll_widget.setLayout(self.scroll_widget_layout)
        # 创建一个可滚动区域
        scroll = QScrollArea()
        # 在可滚动区域中设置窗口部件为scroll_widget
        scroll.setWidget(scroll_widget)
        scroll.setAutoFillBackground(True)
        scroll.setWidgetResizable(True)
        # 在群里盒子布局中添加可滚动区域
        chatroom_box_layout.addWidget(scroll)

        # 创建文件及Token子盒子
        settings_box = QGroupBox()
        settings_box.setTitle("配置信息")
        settings_box_layout = QGridLayout()
        settings_box.setLayout(settings_box_layout)
        # 创建输入框
        key_name = QLabel("AppKey:")
        sec_name = QLabel("Secret:")
        adzone_name = QLabel("Adzone_id:")
        self.appkey = QLineEdit()
        self.secret = QLineEdit()
        self.adzone_id = QLineEdit()
        file_name = QLabel("优惠券文件路径：")
        self.coupon_file = QLineEdit()
        choose_file = QPushButton("选择文件")
        # 添加输入框到settings_box_layout中
        settings_box_layout.addWidget(key_name,0,0)
        settings_box_layout.addWidget(self.appkey,0,1)
        settings_box_layout.addWidget(sec_name,1,0)
        settings_box_layout.addWidget(self.secret,1,1)
        settings_box_layout.addWidget(adzone_name,2,0)
        settings_box_layout.addWidget(self.adzone_id,2,1)
        settings_box_layout.addWidget(file_name,3,0)
        settings_box_layout.addWidget(self.coupon_file,3,1)
        settings_box_layout.addWidget(choose_file,4,0)

        # 创建控制按钮盒子
        control_box = QGroupBox()
        control_box.setTitle("控制开关")
        control_box_layout = QVBoxLayout()
        control_box.setLayout(control_box_layout)
        # 创建控制按钮
        self.start_run = QPushButton("开启机器人")
        self.end_run = QPushButton("停止机器人")
        self.end_run.setEnabled(False)
        self.check_info = QPushButton("检查配置信息")
        # 将控制按钮添加到控制按钮盒子中
        control_box_layout.addWidget(self.start_run,0)
        control_box_layout.addWidget(self.end_run,1)
        control_box_layout.addWidget(self.check_info,2)

        # 选项盒子
        select_box = QGroupBox()
        select_box.setTitle("功能选项")
        # 选项盒子布局
        select_box_layout = QGridLayout()
        select_box.setLayout(select_box_layout)
        # 将群聊列表盒子、配置信息盒子和控制按钮盒子添加到选项盒子中
        select_box_layout.addWidget(chatroom_box,0,0)
        select_box_layout.addWidget(settings_box,0,1)
        select_box_layout.addWidget(control_box,0,2)

        # 窗口主部件中上层功能按钮的布局
        utils_box = QGridLayout()
        # 添加登录盒子和选项盒子到上层布局中
        utils_box.addWidget(login_box,0,0)
        utils_box.addWidget(select_box,0,1)

        '''
            下层控制台盒子
        '''
        # 创建一个文本框
        self.label_1 = QTextEdit()
        self.label_1.setReadOnly(True)

        # 窗口主部件中下层控制台的布局
        console_box = QVBoxLayout()
        console_box.addWidget(self.label_1)

        '''
            主窗体的布局
        '''
        # 窗口主部件
        self.Widget = QWidget()
        # 设置窗口主部件的布局层
        widget_box = QVBoxLayout()
        self.Widget.setLayout(widget_box)
        # 在窗口主部件的布局层中添加功能按钮层和控制台层
        widget_box.addLayout(utils_box)
        widget_box.addLayout(console_box)

        '''页面初始化层'''

        # 设置UI界面的核心窗口为layout_widget
        self.setCentralWidget(self.Widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainGUI()
    gui.show()
    sys.exit(app.exec_())