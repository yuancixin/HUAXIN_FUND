# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WorkSpace\Git\python_test\src\interface\matplotlib.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from interface import MatplotlibWidget
from PyQt5.QtWidgets import QApplication,QWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1056, 591)
        self.widget = MatplotlibWidget(QWidget)
        self.widget.setGeometry(QtCore.QRect(0, 40, 1041, 541))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        
class MainWindow(QWidget,Ui_Form):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())


