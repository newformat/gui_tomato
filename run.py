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
        # отключено по умолчанию
        self.label_dotsTime.setVisible(False)
        self.label_TypeInterval.setVisible(False)
        self.lcdNumber_Minute.setVisible(False)
        self.lcdNumber_Second.setVisible(False)

        # события по умолчанию
        # вкладка "Работа"
        self.horizontalSlider_workMinute.sliderMoved[int].connect(self.event_WorkMinute)
        self.checkBox_WorkOff.stateChanged.connect(self.event_checkBox_WorkOff)

        self.tt = QtGui.QStandardItemModel(self)
        self.pushButton_Reset.clicked.connect(self.itemList)


    # события - вкладка "работа"
    def event_WorkMinute(self, minute):
        self.spinBox_WorkMinute.setValue(minute)


    def event_checkBox_WorkOff(self, value):
        if value == 2:
            self.horizontalSlider_workMinute.setEnabled(False)
            self.checkBox_WorkOff.setText('off')
        else:
            self.horizontalSlider_workMinute.setEnabled(True)
            self.checkBox_WorkOff.setText('on')


# ДОПИСАТЬ БАЗОВЫЕ СОБЫТИЯ ДЛЯ ОСНОВНОГО ОФОРМЛЕНИЯ.




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