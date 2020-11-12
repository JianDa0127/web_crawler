from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
import welcome as wel
import main_screen as ui

# 設定歡迎畫面
class welcome(QMainWindow, wel.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 加入buttonBox, 做動作設定
        # self.buttonBox.clicked.connect(self.redirect)
    # def redirect(self):
# 設定主畫面
# class Main(QMainWindow, ui.UI_MainWindow):
#     def __init__(self):



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = welcome()
    window.show()
    sys.exit(app.exec_())