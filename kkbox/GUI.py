from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
import sys
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
from main_screen import Ui_MainWindow
import KKboxCrawler
import datetime
import unittest


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # 主界面初始化
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 狀態列功能設置
        self.retranslateUi(self)
        self.actionClose.triggered.connect(app.exit)
        # 取得comboBox_place, comboBox_release, comboBox_lang的值
        self.pushButton01.clicked.connect(self.get_comboBoxValue)
    # 地區設置
    def get_comboBoxValue(self):
        place_select_value = self.comboBox_place.currentText()
        release_select_value = self.comboBox_release.currentText()
        lang_select_value = self.comboBox_lang.currentText()
        print(place_select_value)
        print(release_select_value)
        print(lang_select_value)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())