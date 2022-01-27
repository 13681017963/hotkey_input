# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdditionWindow(object):
    def setupUi(self, AdditionWindow):
        AdditionWindow.setObjectName("AdditionWindow")
        AdditionWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AdditionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 451, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cancel_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout_2.addWidget(self.cancel_button, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.confirm_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout_2.addWidget(self.confirm_button, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)
        self.hotkey = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.hotkey.setObjectName("hotkey")
        self.gridLayout.addWidget(self.hotkey, 0, 2, 1, 1)
        AdditionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdditionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        AdditionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdditionWindow)
        self.statusbar.setObjectName("statusbar")
        AdditionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdditionWindow)
        self.cancel_button.clicked.connect(AdditionWindow.cancel_addition)
        self.confirm_button.clicked.connect(AdditionWindow.confirm_addition)
        QtCore.QMetaObject.connectSlotsByName(AdditionWindow)

    def retranslateUi(self, AdditionWindow):
        _translate = QtCore.QCoreApplication.translate
        AdditionWindow.setWindowTitle(_translate("AdditionWindow", "MainWindow"))
        self.label.setText(_translate("AdditionWindow", "热键："))
        self.label_2.setText(_translate("AdditionWindow", "文本："))
        self.cancel_button.setText(_translate("AdditionWindow", "取消"))
        self.confirm_button.setText(_translate("AdditionWindow", "确定"))
        self.hotkey.setText(_translate("AdditionWindow", "无"))

