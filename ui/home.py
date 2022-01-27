# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(777, 602)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 451, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 280, 451, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addition_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addition_button.setObjectName("addition_button")
        self.gridLayout.addWidget(self.addition_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 0, 1, 1, 1)
        self.modify_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.modify_button.setObjectName("modify_button")
        self.gridLayout.addWidget(self.modify_button, 0, 2, 1, 1)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 23))
        self.menubar.setObjectName("menubar")
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        self.addition_button.clicked.connect(HomeWindow.open_addition)
        self.delete_button.clicked.connect(HomeWindow.del_hotkey)
        self.modify_button.clicked.connect(HomeWindow.modify_hotkey)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("HomeWindow", "热键"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("HomeWindow", "文本"))
        self.addition_button.setText(_translate("HomeWindow", "添加"))
        self.delete_button.setText(_translate("HomeWindow", "删除"))
        self.modify_button.setText(_translate("HomeWindow", "修改"))

