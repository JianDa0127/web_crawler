import time
import unittest
import os
import sys
import json
import requests
import datetime
import KKboxCrawler

# 測試介面檔位址
sys.path.append('/Users/glow/Desktop/IECS/Data_Science_and_GUI/group_demo/web_crawler/kkbox/UI_Designer')

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.Qt import QUrl
from main_screen import Ui_MainWindow

# 設定路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
# music_dir = current_dir + r'/music_data'
music_dir = current_dir + r'/Ui_Designer/music_data'
music_files = os.listdir(music_dir)
# image_dir = current_dir + r'/icon'
image_dir = current_dir + r'/Ui_Designer/icon'

print(current_dir)
print(music_dir)
print(music_files)
print(image_dir)

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # 主界面初始化
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.init_action()
        self.init_player_botton()
        # 日期初始化
        self.dateEdit.setDate(QDate.currentDate())
        # self.init_web_crawler_botton()

        # icon來源
        # Icons made by <ahref="https://www.flaticon.com/authors/bqlqn"title = "bqlqn">bqlqn</a>
        # from<ahref = "https://www.flaticon.com/"title = "Flaticon">www.flaticon.com</a>

        # 播放器
        # self.fileName = ""
        # self.now_playing_song = ''
        self.playlist = QMediaPlaylist(self)
        self.player = QMediaPlayer(self)
        ## 初始化歌名與顯示區塊
        self.now_playing_song.setText('Unknown')
        self.show_result_label.setText('This place will show the search result')
        test_pic = QtGui.QPixmap('IMG_1065.JPG')
        self.picture_label.setPixmap(test_pic)

        ## 歌詞列表設置
        self.lyris_listWidget.hide()

        ## 進度條設置(macOS bug)
        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.get_time_func)
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

        self.media_list = []
        for i in music_files:
            self.media_list.append('{}/{}'.format(music_dir, i))

        for m in self.media_list:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(m)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist_listWidget.addItems([m.split('/')[-1] for m in self.media_list])
        self.playlist.setCurrentIndex(self.playlist_listWidget.currentRow())

        self.playlist_listWidget.itemDoubleClicked.connect(self.Music_Player)
        # 取得搜尋欄的輸入
        self.pushButton_search.clicked.connect(self.search_result)

        # 取得爬蟲參數
        self.pushButton_OK.clicked.connect(self.get_comboBoxValue)

    def init_action(self):
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
    def init_player_botton(self):
        # 播放器按鈕設置
        self.pushButton_play.clicked.connect(self.playMusic)
        self.pushButton_previous.clicked.connect(self.previousMusic)
        self.pushButton_next.clicked.connect(self.nextMusic)
        self.pushButton_random.clicked.connect(self.Music_mode_random)
        self.pushButton_repeat.clicked.connect(self.Music_mode_repeat)
        self.pushButton_lyris.clicked.connect(self.lyris_setting)
        self.pushButton_playlist.clicked.connect(self.playlist_setting)
        self.song_Slider.sliderMoved.connect(self.update_position_func)

    def init_web_crawler_botton(self):
        self.pushBotton_local.clicked.connnct()
        self.pushButton_online.clicked.connect()

    def Music_Player(self, song_name):
        self.now_playing_song.setText(song_name.text())
        self.player.play()

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

    def lyris_setting(self):
        # 歌詞
        if self.lyris_listWidget.isHidden():
            self.lyris_listWidget.show()
        else:
            self.lyris_listWidget.hide()
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
        if minutes == 0 and seconds == 0:
            self.time_label.setText('--/--')
        elif seconds < 10:
            self.time_label.setText('{:2d}:0{}'.format(minutes, seconds))
        else:
            self.time_label.setText('{:2d}:{:2d}'.format(minutes, seconds))

    def get_position_func(self, song_position):
        # 音樂進度條
        self.song_Slider.setValue(song_position)

    def update_position_func(self, song_progress):
        self.player.setPosition(song_progress)
        d_time = self.song_Slider.maximum() - song_progress
        self.get_time_func(d_time)

    def volume_slider_func(self, value):
        # 音量條
        self.player.setVolume(value)

    def search_result(self):
        search_result_text = self.search_lineEdit.text()
        self.show_result_label.setText(search_result_text)
        self.search_lineEdit.clear()

    def get_comboBoxValue(self):
        # 預設字典
        songtype = {'單曲': 'song', '新歌': 'newrelease'}
        area = {'台灣': 'tw', '香港': 'hk', '日本': 'jp', '新加坡': 'sg', '馬來西亞': 'my'}
        lang = {'本地': 'tc', '簡中': 'sc', '日文': 'ja', '英文': 'en', '馬來西亞': 'ms'}
        cate = {'華語': '297', '西洋': '390', '日語': '308', '韓語': '314', '台語': '304', '粵語': '320',
                '綜合': '104', '馬來西亞': '917', '西方': '771', '亞洲': '861'}
        # 取得選取參數
        songtype_select_value = self.comboBox_songtype.currentText()
        area_select_value = self.comboBox_area.currentText()
        lang_select_value = self.comboBox_lang.currentText()
        cate_select_value = self.comboBox_cate.currentText()
        rank_select_value = self.comboBox_rank.currentText()
        date = self.dateEdit.date()
        # print(songtype[songtype_select_value])
        # print(area[area_select_value])
        # print(lang[lang_select_value])
        # print(cate[cate_select_value])
        # print(rank_select_value)
        # print(date.toString(Qt.ISODate))

        # 抓取爬蟲資料
        Crawler_data = KKboxCrawler.KKboxCrawler(songtype[songtype_select_value], area[area_select_value],
                                                 lang[lang_select_value], rank_select_value, cate[cate_select_value],
                                                 date.toString(Qt.ISODate))
        print(Crawler_data)

        # 將爬蟲資料丟進主畫面
        self.tableWidget.setRowCount(int(rank_select_value, base=10))
        for i in range(0, int(rank_select_value, base=10)): #row
            for j in range(0, 5): #col
                self.tableWidget.setItem(i, j, QTableWidgetItem("i+j")) #將資料加入指定的表格位置

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
