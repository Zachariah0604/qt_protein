import os
import sys
from PyQt5 import QtCore, QtGui, QtPrintSupport , QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import filters.filter_select as ffs
import filters.tri_result as tre
import filters.redundancy as fre
qtCreatorFile = "ui/filter.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class filter_window(QtWidgets.QMainWindow, Ui_MainWindow):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.input_dir_btn.clicked.connect(lambda:self.openDir(self.input_path.text(),'input_dir'))
        self.output_dir_btn.clicked.connect(lambda:self.openDir(self.output_path.text(),'output_dir'))
        self.input_dir=''
        self.output_dir=''
        self.filter_flag=0
        self.filter_btn.clicked.connect(lambda:ffs.main(self.get_checked(),self.filter_flag,self.input_dir,self.output_dir,self.fdr_lineedit.text()))

        self.input_dir_mutibtn.clicked.connect(lambda:self.openDir(self.input_path_muti.text(),'input_dir_muti'))
        self.output_dir_mutibtn.clicked.connect(lambda:self.openDir(self.output_path_muti.text(),'output_dir_muti'))
        self.input_dir_muti=''
        self.output_dir_muti=''
        self.muti_btn.clicked.connect(lambda:tre.main(self.input_dir_muti,self.output_dir_muti))

        self.input_dir_redundancybtn.clicked.connect(lambda:self.openFile(self.input_path_redundancy.text()))
        self.output_dir_redundancybtn.clicked.connect(lambda:self.openDir(self.output_path_redundancy.text(),'output_dir_redundancy'))
        self.input_redundancy_file=''
        self.output_dir_redundancy=''
        self.redundancy_btn.clicked.connect(lambda:fre.main(self.input_redundancy_file,self.output_dir_redundancy))
    def get_checked(self):
        if (self.radiopfind.isChecked()):
            self.filter_flag=1
        if (self.radiomascot.isChecked()):
            self.filter_flag=2
        if (self.radiocoment.isChecked()):
           self. filter_flag=3
    def openFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open File Dialog",filePath,"txt files(*.txt)")
        else:
            path = QFileDialog.getOpenFileName(self,"Open File Dialog","/","txt files(*.txt)")
        self.input_path_redundancy.setText(str(path[0]))
        self.input_redundancy_file=str(path[0])

    def openDir(self,filePath,file_flag):
        if os.path.exists(filePath):
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog",filePath)
        else:
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog","/")
        if file_flag == 'input_dir':
            self.input_path.setText(str(path))
            self.input_dir=str(path)
        if file_flag == 'output_dir':
            self.output_path.setText(str(path))
            self.output_dir=str(path)
        if file_flag == 'input_dir_muti':
            self.input_path_muti.setText(str(path))
            self.input_dir_muti=str(path)
        if file_flag == 'output_dir_muti':
            self.output_path_muti.setText(str(path))
            self.output_dir_muti=str(path)
        if file_flag == 'output_dir_redundancy':
            self.output_path_redundancy.setText(str(path))
            self.output_dir_redundancy=str(path)