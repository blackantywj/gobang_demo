# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_game_begin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartGame(object):
    def setupUi(self, StartGame):
        StartGame.setObjectName("StartGame")
        StartGame.resize(630, 470)
        StartGame.setMinimumSize(QtCore.QSize(630, 470))
        StartGame.setMaximumSize(QtCore.QSize(630, 470))
        StartGame.setStyleSheet("background-image:url(../source/1.png)")
        self.AI = QtWidgets.QPushButton(StartGame)
        self.AI.setGeometry(QtCore.QRect(59, 316, 120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.AI.setFont(font)
        self.AI.setStyleSheet("background: transparent")
        self.AI.setText("")
        self.AI.setObjectName("AI")
        self.Human = QtWidgets.QPushButton(StartGame)
        self.Human.setGeometry(QtCore.QRect(50, 361, 146, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Human.setFont(font)
        self.Human.setStyleSheet("background: transparent")
        self.Human.setText("")
        self.Human.setObjectName("Human")
        self.develop = QtWidgets.QPushButton(StartGame)
        self.develop.setGeometry(QtCore.QRect(59, 407, 120, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.develop.setFont(font)
        self.develop.setStyleSheet("background: transparent")
        self.develop.setText("")
        self.develop.setObjectName("develop")

        self.retranslateUi(StartGame)
        QtCore.QMetaObject.connectSlotsByName(StartGame)

    def retranslateUi(self, StartGame):
        _translate = QtCore.QCoreApplication.translate
        StartGame.setWindowTitle(_translate("StartGame", "五子棋"))

