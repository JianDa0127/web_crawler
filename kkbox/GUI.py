from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
import sys
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
import main_screen as ui
import unittest


class MainWindow(QMainWindow, ui.UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())