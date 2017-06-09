import sys
from PyQt5 import QtCore, QtGui, QtPrintSupport , QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import os
from train import train_window
from get_features import feature_window
from params_plot_ad import params_plot_window
from filter import filter_window
qtCreatorFile = "ui/main.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.filter_btn.clicked.connect(self.get_filter_window)
        self.train_btn.clicked.connect(self.get_train_window)
        self.feature_btn.clicked.connect(self.get_features_window)
        self.params_plot_btn.clicked.connect(self.get_params_plot_window)
    def get_filter_window(self):
        self.get_window=filter_window()
        self.get_window.show()
    def get_train_window(self):
        self.get_window=train_window()
        self.get_window.show()
    def get_features_window(self):
        self.get_window=feature_window()
        self.get_window.show()
    def get_params_plot_window(self):
        self.get_window=params_plot_window()
        self.get_window.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())