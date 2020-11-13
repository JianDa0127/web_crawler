from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
import welcome as wel
import main_screen as ui
import unittest

# 設定歡迎畫面(account, password)
# class welcome(QMainWindow, wel.Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#

# 設定主畫面
class Main(QMainWindow, ui.UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 加入place_comboBox, 做動作設定
        self.place_comboBox.clicked.connect(self.place)
        # 加入song_comboBox, 做動作設定
        self.song_comboBox.clicked.connect(self.songstyle)
    # def place(self):

    # def songstyle(self):

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())