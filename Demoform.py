#Demoform.py
import imp
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        self.label.setText("첫번째클릭")
    def secondClick(self):
        self.label.setText("두번째클릭")
    def thirdClick(self):
        self.label.setText("세번째클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()