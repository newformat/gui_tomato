import sys
from PyQt5 import QtWidgets, QtGui
from functools import partial
from ui.mainform import *


class MainTomato(QtWidgets.QMainWindow, Ui_MainForm):
    '''

    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self) # init GUI
        self.tt = QtGui.QStandardItemModel(self)

        self.pushButton_Reset.clicked.connect(self.itemList)


    def itemList(self):
        item =  QtGui.QStandardItem("pushButton_2")
        self.tt.appendRow(item)
        self.listView_History.setModel(self.tt)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainTomato()
    window.setFixedSize(window.width(),window.height())
    window.show()
    app.exec_()