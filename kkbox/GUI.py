from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer/icon')
from main_screen import Ui_MainWindow
import KKboxCrawler
import datetime
import unittest


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # 主界面初始化
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 播放器設置

        # 播放器按鈕設置
        # Icons made by <ahref="https://www.flaticon.com/authors/bqlqn"title = "bqlqn">bqlqn</a>from<ahref = "https://www.flaticon.com/"title = "Flaticon">www.flaticon.com</a>

        # self.pushButton_play.clicked.connect(self.playMusic)
        # self.pushButton_previous.clicked.connect(self.previousMusic)
        # self.pushButton_next.clicked.connect(self.nextMusic)
        # self.pushButton_random.clicked.connect(self.randomMusic)
        # self.pushButton_repeat.clicked.connect(self.repeatMusic)

        # 狀態列功能設置
        self.retranslateUi(self)
        self.actionClose.triggered.connect(app.exit)

        # 取得comboBox_place, comboBox_release, comboBox_lang選取的值
        self.pushButton_OK.clicked.connect(self.get_comboBoxValue)

    # 地區設置
    def get_comboBoxValue(self):
        place_select_value = self.comboBox_place.currentText()
        release_select_value = self.comboBox_release.currentText()
        lang_select_value = self.comboBox_lang.currentText()

        print(place_select_value)
        print(release_select_value)
        print(lang_select_value)
    # 播放器按鈕功能設置
    # def playMusic(self):


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())