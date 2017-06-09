#coding:utf-8
import sys
from PyQt5 import QtCore, QtGui, QtPrintSupport , QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import PyQt5.uic
import os
import train_model.lightg_bm as tl
import params
qtCreatorFile = "ui/model_select.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class get_params(QDialog):
    def __init__(self, parent=None):
        super(get_params, self).__init__(parent)
        self.setMinimumSize(100, 100)
        #self.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowCloseButtonHint)
        self.params=params.dict_lightgbm
        self.headDict = {}
        self.headPostArrayKey = 0
        self.HeadGroupBox = QGroupBox('add params')
        self.HeadGroupBox.setMinimumHeight(200)  
        self.HeadGroupBox.scroll(100,2)
        self.HeadAddParam = QPushButton(u'+')
        self.headDict[str(self.headPostArrayKey)+'_param'] = QComboBox()
        self.headDict[str(self.headPostArrayKey)+'_value'] = QLineEdit()
        self.HeadGroupBoxLayout = QGridLayout()
        self.HeadGroupBoxLayout.addWidget(self.HeadAddParam, 0, 0)
        self.HeadGroupBoxLayout.addWidget(QLabel('paramName:'), 1, 0)
        for k,v in self.params.items():
            self.headDict[str(self.headPostArrayKey)+'_param'].addItem(v,k)
        self.HeadGroupBoxLayout.addWidget(self.headDict[str(self.headPostArrayKey)+'_param'], 1, 1)
        #self.HeadGroupBoxLayout.addWidget(self.headDict[str(self.headPostArrayKey)+'_param'], 1, 1)
        self.HeadGroupBoxLayout.addWidget(QLabel('Value:'), 1, 2)
        self.HeadGroupBoxLayout.addWidget(self.headDict[str(self.headPostArrayKey)+'_value'], 1, 3)
        self.HeadGroupBox.setLayout(self.HeadGroupBoxLayout)
        self.HeadAddParam.clicked.connect(self.addHeadParam)

       
        self.btnPost = QPushButton('Ok')
        self.postbtnLoayout = QHBoxLayout()
        self.postbtnLoayout.addStretch()
        self.postbtnLoayout.addWidget(self.btnPost)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.HeadGroupBox)
        main_layout.addLayout(self.postbtnLoayout)  
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        #return self.btnPost.clicked.connect(self.postData)
        


    
    def addHeadParam(self):
        sts=str(self.headPostArrayKey+1)
        self.headDict[sts+'_param'] = QComboBox()
        #self.headDict[sts+'_param'].clear()
        for k,v in self.params.items():
            self.headDict[sts+'_param'].addItem(v,k)
        self.headDict[sts+'_value'] = QLineEdit()

        self.HeadGroupBoxLayout.addWidget(QLabel('paramName'))
        self.HeadGroupBoxLayout.addWidget(self.headDict[sts+'_param'])
        self.HeadGroupBoxLayout.addWidget(QLabel(u'Value'))
        self.HeadGroupBoxLayout.addWidget(self.headDict[sts+'_value'])
        self.headPostArrayKey+=1
    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()
class train_window(QtWidgets.QMainWindow, Ui_MainWindow):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
       
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        get_params_window=get_params()
       
        self.open_file_button.clicked.connect(lambda:self.openFile(self.file_path.text()))
        self.output_dir_btn.clicked.connect(lambda:self.openDir(self.output_path.text()))
        self.add_params_button.clicked.connect(self.param_window)
        self.finally_params={}
        self.data_file=''
        self.output_dir=''
        self.model_name=self.model_box.currentText()
        if  self.tarin_btn.clicked: 
            self.tarin_btn.clicked.connect(lambda:tl.lightGbm(self.data_file,dict(self.finally_params),int(self.n_flods.value()),True,int(self.random_seed.text()),int(self.num_round.text()),self.output_dir))

    def param_window(self):
        self.get_params_window=get_params()
        self.get_params_window.show()
        self.get_params_window.btnPost.clicked.connect(self.postData)
        self.get_params_window.exec_()
   
    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()
    def postData(self):
        self.params_dict_data={}
        self.params_dict=self.get_params_window.headDict
        for k, v in self.params_dict.items():
            temp=k.split('_')
            if temp[1]=='param':
                if temp[0] in self.params_dict_data:
                    self.params_dict_data[temp[0]]['param'] =str(v.currentText())
                else:
                    self.params_dict_data[temp[0]] = {'param':str(v.currentText())}

            elif temp[1]=='value':
                if temp[0] in self.params_dict_data:
                    self.params_dict_data[temp[0]]['value'] =str(v.text())
                else:
                    self.params_dict_data[temp[0]] = {'value':str(v.text())}
        print(self.params_dict_data)
        
        for i in self.params_dict_data.keys():
            param_data = self.params_dict_data[str(i)]
            if '.' in param_data['value']:
                self.finally_params[str(param_data['param'])]=float(param_data['value'])
            else:
                self.finally_params[str(param_data['param'])]=int(param_data['value'])
        self.params_dict_text.clear()
        self.params_dict_text.insertPlainText(str(self.finally_params))
   
    def openFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open File Dialog",filePath,"csv files(*.csv)")
        else:
            path = QFileDialog.getOpenFileName(self,"Open File Dialog","/","csv files(*.csv)")
        self.file_path.setText(str(path[0]))
        self.data_file=str(path[0])
    def openDir(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog",filePath)
        else:
            path = QFileDialog.getExistingDirectory(self,"Open File Dialog","/")
        self.output_path.setText(str(path))
        self.output_dir=str(path)
