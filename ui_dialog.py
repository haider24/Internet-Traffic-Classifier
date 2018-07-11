# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 136)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.time = QtWidgets.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(180, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(140, 90, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color:\"red\";\n"
"color:\"white\";")
        self.stop.setObjectName("stop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Capturing Packets...."))
        self.label.setText(_translate("Dialog", "Seconds"))
        self.time.setText(_translate("Dialog", "1"))
        self.stop.setText(_translate("Dialog", "Stop Capturing"))

