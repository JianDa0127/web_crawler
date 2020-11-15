import time
import os
import sys
# sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')
import unittest

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.Qt import QUrl
from main_screen import Ui_MainWindow

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # 主界面初始化
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 路徑設定
        media_root = QFileInfo(__file__).absolutePath()
        image_root = QFileInfo(__file__).absolutePath()
        print(media_root)
        print(image_root)

        # icon設定
        # Icons made by <ahref="https://www.flaticon.com/authors/bqlqn"title = "bqlqn">bqlqn</a>
        # from<ahref = "https://www.flaticon.com/"title = "Flaticon">www.flaticon.com</a>
        # self.setWindowIcon(QIcon(image_root + '/icon/kkbox_app_icon.png'))

        # 播放器
        # self.fileName = ""
        # self.now_playing_song = ''
        self.playlist = QMediaPlaylist(self)
        self.player = QMediaPlayer(self)
        ## 顯示歌名和專輯
        self.now_playing_song.setText('Hello, World!')
        self.now_playing_album.setText('Unknown')

        ## 進度條設置(macOS bug)
        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.get_position_func)
        ## 音量設置
        self.volume_Slider.valueChanged.connect(self.volume_slider_func)
        self.player.setVolume(50)

        ## 播放列表設置
            # 取得音樂檔案位置
            # self.media_content = QMediaContent(QUrl.fromLocalFile('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/text.mp3'))
            # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
            # self.player.setMedia(self.media_content)
        self.playlist_listWidget.hide()
        self.player.setPlaylist(self.playlist)
        self.media_list = ['{}/01. Wake Up, Get Up, Get Out There.mp3'.format(media_root),
                           '{}/04. Life Will Change.mp3'.format(media_root),
                           '{}/17. Last Surprise.mp3'.format(media_root),
                           ]
        for m in self.media_list:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(m)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
        self.playlist_listWidget.addItems([m.split('/')[-1] for m in self.media_list])
        self.playlist.setCurrentIndex(self.playlist_listWidget.currentRow())
        self.player.play()

        print(self.playlist.playbackMode)

        # 狀態列功能設置
        self.retranslateUi(self)
        self.actionClose.triggered.connect(app.exit)
        # self.actionsOpen.triggered.connect(self.file_open)
        self.actionPlay.triggered.connect(self.playMusic)
        self.actionNext.triggered.connect(self.nextMusic)
        self.actionPrevious.triggered.connect(self.previousMusic)
        self.actionSuffle.triggered.connect(self.Music_mode_random)
        self.actionRepeat.triggered.connect(self.Music_mode_repeat)
        # self.actionVolume_Up.triggered.connect(self)
        # self.actionVolume_Down.triggered.connect(self)

        # 播放器按鈕設置
        self.pushButton_play.clicked.connect(self.playMusic)
        self.pushButton_previous.clicked.connect(self.previousMusic)
        self.pushButton_next.clicked.connect(self.nextMusic)
        self.pushButton_random.clicked.connect(self.Music_mode_random)
        self.pushButton_repeat.clicked.connect(self.Music_mode_repeat)
        # self.pushButton_lyris.clicked.connect(self.lyris)
        self.pushButton_playlist.clicked.connect(self.playlist_setting)

        # 取得comboBox_place, comboBox_release, comboBox_lang選取的值
        self.pushButton_OK.clicked.connect(self.get_comboBoxValue)

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

    def Music_mode_random(self):
        # 音樂模式:隨機
        self.playlist.setPlaybackMode(QMediaPlaylist.Random)
        print(self.playlist.playbackMode)
        
    def Music_mode_repeat(self):
        # 音樂模式:單曲循環
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        print(self.playlist.playbackMode)

    def playlist_setting(self):
        # 播放列表
        if self.playlist_listWidget.isHidden():
            self.playlist_listWidget.show()
        else:
            self.playlist_listWidget.hide()

    def get_duration_func(self, d_time):
        # 取得進度條位址
        self.song_Slider.setRange(0, d_time)
        self.song_Slider.setEnabled(True)
        self.get_time_func(d_time)

    def get_time_func(self, d_time):
        # 播放時間
        seconds = int(d_time / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        # if minutes == 0 and seconds == 0:
        #     self.time_label.setText('--/--')
        # else:
        #     self.time_label.setText('{}:{}'.format(minutes, seconds))

    def get_position_func(self, song_position):
        # 音樂進度條
        self.song_Slider.setValue(song_position)

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