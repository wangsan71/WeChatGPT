# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeChat.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from wxauto import *
import os, sys
import tkinter as tk
from tkinter import *


class Ui_WeChatBotStarter(object):
    def RunG(self):
        from WeChatGPT_Groups import wx_group_chat
        self.CloseWeb()
        wx_group_chat()    

    def RunM(self):
        from WeChatGPT_YourSelf import wx_group_chat
        self.CloseWeb()
        wx_group_chat()
              
    def setupUi(self, WeChatBotStarter):
        WeChatBotStarter.setObjectName("WeChatBotStarter")
        WeChatBotStarter.resize(320, 240)
        self.pushButton_2 = QtWidgets.QPushButton(WeChatBotStarter)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 140, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.RunM)
        self.pushButton_3 = QtWidgets.QPushButton(WeChatBotStarter)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 60, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.RunG)

        self.retranslateUi(WeChatBotStarter)
        QtCore.QMetaObject.connectSlotsByName(WeChatBotStarter)

    def retranslateUi(self, WeChatBotStarter):
        _translate = QtCore.QCoreApplication.translate
        WeChatBotStarter.setWindowTitle(_translate("WeChatBotStarter", "WeChatBotStarter"))
        self.pushButton_2.setText(_translate("WeChatBotStarter", "Run for YourSelf"))
        self.pushButton_3.setText(_translate("WeChatBotStarter", "Run for Groups"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeChatBotStarter = QtWidgets.QWidget()
    ui = Ui_WeChatBotStarter()
    ui.setupUi(WeChatBotStarter)
    WeChatBotStarter.show()
    sys.exit(app.exec_())
