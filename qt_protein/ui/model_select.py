# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_select.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_model_select(object):
    def setupUi(self, model_select):
        model_select.setObjectName("model_select")
        model_select.resize(356, 600)
        self.centralwidget = QtWidgets.QWidget(model_select)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 54, 12))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 50, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        self.open_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_button.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.open_file_button.setObjectName("open_file_button")
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.file_path.setObjectName("file_path")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 54, 12))
        self.label_3.setObjectName("label_3")
        self.add_params_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_params_button.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.add_params_button.setObjectName("add_params_button")
        self.params_view = QtWidgets.QLineEdit(self.centralwidget)
        self.params_view.setGeometry(QtCore.QRect(80, 110, 211, 131))
        self.params_view.setObjectName("params_view")
        model_select.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(model_select)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 23))
        self.menubar.setObjectName("menubar")
        model_select.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(model_select)
        self.statusbar.setObjectName("statusbar")
        model_select.setStatusBar(self.statusbar)

        self.retranslateUi(model_select)
        QtCore.QMetaObject.connectSlotsByName(model_select)

    def retranslateUi(self, model_select):
        _translate = QtCore.QCoreApplication.translate
        model_select.setWindowTitle(_translate("model_select", "MainWindow"))
        self.label.setText(_translate("model_select", "模型选择"))
        self.comboBox.setItemText(0, _translate("model_select", "LightGBM"))
        self.comboBox.setItemText(1, _translate("model_select", "XGBoost"))
        self.label_2.setText(_translate("model_select", "训练数据"))
        self.open_file_button.setText(_translate("model_select", "浏览"))
        self.label_3.setText(_translate("model_select", "参数设置"))
        self.add_params_button.setText(_translate("model_select", "添加参数"))

