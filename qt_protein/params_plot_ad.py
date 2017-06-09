import sys
from PyQt5 import QtCore, QtGui, QtPrintSupport , QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import plot.params_ad_plot as pp 

import os
qtCreatorFile = "ui/plot_params_ad.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class params_plot_window(QtWidgets.QMainWindow, Ui_MainWindow):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.open_file_button.clicked.connect(lambda:self.openFile(self.file_path.text()))
        self.data_file=''
        self.plot_btn.clicked.connect(lambda:self.select_plot())

    def select_plot(self):
        if int(self.var_cunt_combox.currentText()) == 1:
            pp.single_var(self.data_file,self.x_coordinate.text(),self.x_limit.text(),self.x_lower.text(),self.y_limit.text(),self.y_lower.text())
        else:
            pp.double_var(self.data_file,self.x_coordinate_2.text(),self.z_coordinate.text(),self.x_count.text(),self.z_count.text(),self.x_limit.text(),self.x_lower.text(),self.y_limit.text(),self.y_lower.text())
    def openFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open File Dialog",filePath,"txt files(*.txt)")
        else:
            path = QFileDialog.getOpenFileName(self,"Open File Dialog","/","txt files(*.txt)")
        self.file_path.setText(str(path[0]))
        self.data_file=str(path[0])

