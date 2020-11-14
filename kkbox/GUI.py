from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
# sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
# sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer/icon')
from main_screen import Ui_MainWindow
import unittest


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # 主界面初始化
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 播放器設置
        self.playlist = QMediaPlaylist(self)
        self.player = QMediaPlayer(self)
        self.media_content = QMediaContent(QUrl.fromLocalFile('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/text.mp3'))
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        self.player.setMedia(self.media_content)
        ## 音量設置
        self.volume_Slider.valueChanged.connect(self.volume_slider_func)
        self.player.setVolume(50)
        self.player.play()
        self.duration = self.player.duration() #取得歌曲長度(macOS無法設定...)

        # 狀態列功能設置
        self.retranslateUi(self)
        self.actionClose.triggered.connect(app.exit)
        # self.actionsOpen.triggered.connect(self.file_open)
        self.actionPlay.triggered.connect(self.playMusic)
        self.actionNext.triggered.connect(self.nextMusic)
        self.actionPrevious.triggered.connect(self.previousMusic)
        self.actionSuffle.triggered.connect(self.Music_mode)
        self.actionRepeat.triggered.connect(self.Music_mode)
        # self.actionVolume_Up.triggered.connect(self)
        # self.actionVolume_Down.triggered.connect(self)

        # 播放器按鈕設置
        # Icons made by <ahref="https://www.flaticon.com/authors/bqlqn"title = "bqlqn">bqlqn</a>from<ahref = "https://www.flaticon.com/"title = "Flaticon">www.flaticon.com</a>

        self.pushButton_play.clicked.connect(self.playMusic)
        self.pushButton_previous.clicked.connect(self.previousMusic)
        self.pushButton_next.clicked.connect(self.nextMusic)
        self.pushButton_random.clicked.connect(self.Music_mode)
        self.pushButton_repeat.clicked.connect(self.Music_mode)

        # 取得comboBox_place, comboBox_release, comboBox_lang選取的值
        self.pushButton_OK.clicked.connect(self.get_comboBoxValue)

    # def file_open(self):
    #     # 開啟檔案
    def playMusic(self):
        # 播放音樂
        if self.player.state() == 1:
            self.player.pause()
        else:
            self.player.play()
    def nextMusic(self):
        # 下一首歌
        if self.playlist.currentIndex() == self.playlist.mediaCount() - 1:
            self.playlist.setCurrentIndex(0)
        else:
            self.playlist.next()
    def previousMusic(self):
        # 上一首歌
            if self.playlist.currentIndex() == 0:
                self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)
            else:
                self.playlist.previous()
    def Music_mode(self):
        # 音樂模式
        if self.playlist.playbackMode() == 2:
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        elif self.playlist.playbackMode() == 3:
            self.playlist.setPlaybackMode(QMediaPlaylist.Random)

        elif self.playlist.playbackMode() == 4:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
    def volume_slider_func(self, value):
        # 音量條
        self.player.setVolume(value)

    def get_comboBoxValue(self):
        # 取得地區,歌曲類型,歌曲語言
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