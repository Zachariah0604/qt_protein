import sys
from PyQt5 import QtCore, QtGui, QtPrintSupport , QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import features.features_select as ffs

import os
qtCreatorFile = "ui/features.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class feature_window(QtWidgets.QMainWindow, Ui_MainWindow):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.open_file_button.clicked.connect(lambda:self.openFile(self.file_path.text()))
        self.output_dir_btn.clicked.connect(lambda:self.openDir(self.output_path.text()))
        self.data_file=''
        self.output_dir=''
        self.feature_flag=0
        self.normalize_flag=0
        self.feature_btn.clicked.connect(lambda:ffs.main(self.get_checked(),self.feature_flag,self.normalize_flag,self.data_file,self.output_dir))
        print(self.feature_flag,self.normalize_flag)
    def get_checked(self):
        if (self.radioButton35.isChecked()):
            self.feature_flag=35
        if (self.radioButton220.isChecked()):
            self.feature_flag=220
        if (self.radioButton43.isChecked()):
           self. feature_flag=43
        if (self.radioButton195.isChecked()):
           self. feature_flag=195
        if (self.radioButton255.isChecked()):
           self. feature_flag=255


        if (self.radioButtonn0.isChecked()):
           self. normalize_flag=0
        if (self.radioButtonn1.isChecked()):
           self. normalize_flag=1
        if (self.radioButtonn2.isChecked()):
           self. normalize_flag=2
        
    def openFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open File Dialog",filePath,"txt files(*.txt)")
        else:
            path = QFileDialog.getOpenFileName(self,"Open File Dialog","/","txt files(*.txt)")
        self.file_path.setText(str(path[0]))
        self.data_file=str(path[0])
    def openDir(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog",filePath)
        else:
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog","/")
        self.output_path.setText(str(path))
        self.output_dir=str(path)
