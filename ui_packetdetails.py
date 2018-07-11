# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packetdetails.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 50, 921, 291))
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        self.piechart = QtWidgets.QPushButton(self.centralwidget)
        self.piechart.setGeometry(QtCore.QRect(270, 350, 171, 23))
        self.piechart.setObjectName("piechart")
        self.barchart = QtWidgets.QPushButton(self.centralwidget)
        self.barchart.setGeometry(QtCore.QRect(470, 350, 171, 23))
        self.barchart.setObjectName("barchart")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:\"blue\";")
        self.label.setObjectName("label")
        self.totalpackets = QtWidgets.QLabel(self.centralwidget)
        self.totalpackets.setGeometry(QtCore.QRect(520, 20, 59, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totalpackets.setFont(font)
        self.totalpackets.setStyleSheet("color:\"blue\";")
        self.totalpackets.setObjectName("totalpackets")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Packets Details"))
        self.piechart.setText(_translate("MainWindow", "View Stats in Pie Chart"))
        self.barchart.setText(_translate("MainWindow", "View Stats in Bar Chart"))
        self.label.setText(_translate("MainWindow", "Packets Captured: "))
        self.totalpackets.setText(_translate("MainWindow", "12"))

