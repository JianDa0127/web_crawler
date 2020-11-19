# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/kkbox_app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 140, 541, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.release_verticalLayout = QtWidgets.QVBoxLayout()
        self.release_verticalLayout.setObjectName("release_verticalLayout")
        self.release_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.release_label.setAlignment(QtCore.Qt.AlignCenter)
        self.release_label.setObjectName("release_label")
        self.release_verticalLayout.addWidget(self.release_label)
        self.comboBox_release = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_release.setObjectName("comboBox_release")
        self.comboBox_release.addItem("")
        self.comboBox_release.addItem("")
        self.release_verticalLayout.addWidget(self.comboBox_release)
        self.gridLayout.addLayout(self.release_verticalLayout, 0, 1, 1, 1)
        self.lang_verticalLayout = QtWidgets.QVBoxLayout()
        self.lang_verticalLayout.setObjectName("lang_verticalLayout")
        self.lang_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lang_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lang_label.setObjectName("lang_label")
        self.lang_verticalLayout.addWidget(self.lang_label)
        self.comboBox_lang = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_lang.setObjectName("comboBox_lang")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.comboBox_lang.addItem("")
        self.lang_verticalLayout.addWidget(self.comboBox_lang)
        self.gridLayout.addLayout(self.lang_verticalLayout, 0, 2, 1, 1)
        self.place_verticalLayout = QtWidgets.QVBoxLayout()
        self.place_verticalLayout.setObjectName("place_verticalLayout")
        self.place_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.place_label.setAlignment(QtCore.Qt.AlignCenter)
        self.place_label.setObjectName("place_label")
        self.place_verticalLayout.addWidget(self.place_label)
        self.comboBox_place = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_place.setObjectName("comboBox_place")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.comboBox_place.addItem("")
        self.place_verticalLayout.addWidget(self.comboBox_place)
        self.gridLayout.addLayout(self.place_verticalLayout, 0, 0, 1, 1)
        self.checkbutton_verticalLayout = QtWidgets.QVBoxLayout()
        self.checkbutton_verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.checkbutton_verticalLayout.setObjectName("checkbutton_verticalLayout")
        self.pushButton_OK = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OK.sizePolicy().hasHeightForWidth())
        self.pushButton_OK.setSizePolicy(sizePolicy)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.checkbutton_verticalLayout.addWidget(self.pushButton_OK)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancel.setSizePolicy(sizePolicy)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.checkbutton_verticalLayout.addWidget(self.pushButton_Cancel)
        self.gridLayout.addLayout(self.checkbutton_verticalLayout, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.playlist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.playlist_listWidget.setEnabled(True)
        self.playlist_listWidget.setGeometry(QtCore.QRect(930, 130, 256, 511))
        self.playlist_listWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.playlist_listWidget.setProperty("showDropIndicator", True)
        self.playlist_listWidget.setSelectionRectVisible(True)
        self.playlist_listWidget.setObjectName("playlist_listWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 0, 511, 71))
        self.widget.setObjectName("widget")
        self.graphicsView_album = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_album.setGeometry(QtCore.QRect(0, 0, 91, 71))
        self.graphicsView_album.setObjectName("graphicsView_album")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(110, 0, 301, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.now_playing_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.now_playing_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.now_playing_verticalLayout.setObjectName("now_playing_verticalLayout")
        self.now_playing_song = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.now_playing_song.setAlignment(QtCore.Qt.AlignCenter)
        self.now_playing_song.setObjectName("now_playing_song")
        self.now_playing_verticalLayout.addWidget(self.now_playing_song)
        self.song_Slider = QtWidgets.QSlider(self.widget)
        self.song_Slider.setGeometry(QtCore.QRect(90, 50, 371, 22))
        self.song_Slider.setMaximum(100)
        self.song_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.song_Slider.setObjectName("song_Slider")
        self.time_label = QtWidgets.QLabel(self.widget)
        self.time_label.setGeometry(QtCore.QRect(400, 40, 60, 16))
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(80, 10, 261, 51))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_random = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_random.setGeometry(QtCore.QRect(0, 10, 61, 32))
        self.pushButton_random.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/shuffle-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_random.setIcon(icon1)
        self.pushButton_random.setObjectName("pushButton_random")
        self.pushButton_previous = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_previous.setGeometry(QtCore.QRect(50, 10, 61, 32))
        self.pushButton_previous.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_previous.setIcon(icon2)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_play = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_play.setGeometry(QtCore.QRect(100, 10, 61, 32))
        font = QtGui.QFont()
        font.setKerning(False)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setAutoFillBackground(False)
        self.pushButton_play.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_play.setIcon(icon3)
        self.pushButton_play.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_next = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_next.setGeometry(QtCore.QRect(150, 10, 61, 32))
        self.pushButton_next.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next.setIcon(icon4)
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_repeat = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_repeat.setGeometry(QtCore.QRect(200, 10, 61, 32))
        self.pushButton_repeat.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_repeat.setIcon(icon5)
        self.pushButton_repeat.setObjectName("pushButton_repeat")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(870, 0, 251, 51))
        self.widget_3.setObjectName("widget_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.widget_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 20, 91, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.volume_Slider = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.volume_Slider.setMaximum(100)
        self.volume_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_Slider.setObjectName("volume_Slider")
        self.gridLayout_3.addWidget(self.volume_Slider, 0, 0, 1, 1)
        self.pushButton_volumeUp = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_volumeUp.setGeometry(QtCore.QRect(30, 20, 51, 32))
        self.pushButton_volumeUp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/volume-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_volumeUp.setIcon(icon6)
        self.pushButton_volumeUp.setObjectName("pushButton_volumeUp")
        self.pushButton_volumeDown = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_volumeDown.setGeometry(QtCore.QRect(170, 20, 51, 32))
        self.pushButton_volumeDown.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/volume-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_volumeDown.setIcon(icon7)
        self.pushButton_volumeDown.setObjectName("pushButton_volumeDown")
        self.pushButton_lyris = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lyris.setGeometry(QtCore.QRect(1060, 90, 101, 32))
        self.pushButton_lyris.setObjectName("pushButton_lyris")
        self.pushButton_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_playlist.setGeometry(QtCore.QRect(960, 90, 101, 32))
        self.pushButton_playlist.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/playlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_playlist.setIcon(icon8)
        self.pushButton_playlist.setObjectName("pushButton_playlist")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(279, 229, 611, 401))
        self.widget_4.setObjectName("widget_4")
        self.show_result_label = QtWidgets.QLabel(self.widget_4)
        self.show_result_label.setGeometry(QtCore.QRect(90, 40, 411, 131))
        self.show_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.show_result_label.setObjectName("show_result_label")
        self.show_result_label_2 = QtWidgets.QLabel(self.widget_4)
        self.show_result_label_2.setGeometry(QtCore.QRect(90, 210, 411, 131))
        self.show_result_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.show_result_label_2.setObjectName("show_result_label_2")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(-1, 179, 251, 461))
        self.widget_5.setObjectName("widget_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_5)
        self.pushButton.setGeometry(QtCore.QRect(0, 20, 251, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 251, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 140, 251, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 200, 251, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 260, 251, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 320, 251, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lyris_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.lyris_listWidget.setEnabled(True)
        self.lyris_listWidget.setGeometry(QtCore.QRect(930, 130, 256, 511))
        self.lyris_listWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.lyris_listWidget.setProperty("showDropIndicator", True)
        self.lyris_listWidget.setSelectionRectVisible(True)
        self.lyris_listWidget.setObjectName("lyris_listWidget")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(260, 80, 631, 41))
        self.widget_6.setObjectName("widget_6")
        self.search_lineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.search_lineEdit.setGeometry(QtCore.QRect(0, 10, 511, 21))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.pushButton_search = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_search.setGeometry(QtCore.QRect(520, 0, 101, 41))
        self.pushButton_search.setObjectName("pushButton_search")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menukkbox = QtWidgets.QMenu(self.menubar)
        self.menukkbox.setObjectName("menukkbox")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.action_create_new_playlist = QtWidgets.QAction(MainWindow)
        self.action_create_new_playlist.setObjectName("action_create_new_playlist")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionVolume_Up = QtWidgets.QAction(MainWindow)
        self.actionVolume_Up.setObjectName("actionVolume_Up")
        self.actionVolume_Down = QtWidgets.QAction(MainWindow)
        self.actionVolume_Down.setObjectName("actionVolume_Down")
        self.actionSupport = QtWidgets.QAction(MainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionSuffle = QtWidgets.QAction(MainWindow)
        self.actionSuffle.setObjectName("actionSuffle")
        self.actionRepeat = QtWidgets.QAction(MainWindow)
        self.actionRepeat.setObjectName("actionRepeat")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout_kkbox = QtWidgets.QAction(MainWindow)
        self.actionAbout_kkbox.setObjectName("actionAbout_kkbox")
        self.actionOpen_Dir = QtWidgets.QAction(MainWindow)
        self.actionOpen_Dir.setObjectName("actionOpen_Dir")
        self.actionOpen_Rencent = QtWidgets.QAction(MainWindow)
        self.actionOpen_Rencent.setObjectName("actionOpen_Rencent")
        self.menukkbox.addAction(self.actionAbout_kkbox)
        self.menukkbox.addSeparator()
        self.menukkbox.addAction(self.actionSetting)
        self.menukkbox.addSeparator()
        self.menukkbox.addAction(self.actionClose)
        self.menuEdit.addAction(self.action_create_new_playlist)
        self.menuControl.addAction(self.actionPlay)
        self.menuControl.addAction(self.actionPause)
        self.menuControl.addAction(self.actionNext)
        self.menuControl.addAction(self.actionPrevious)
        self.menuControl.addSeparator()
        self.menuControl.addAction(self.actionVolume_Up)
        self.menuControl.addAction(self.actionVolume_Down)
        self.menuControl.addSeparator()
        self.menuControl.addAction(self.actionSuffle)
        self.menuControl.addAction(self.actionRepeat)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addAction(self.actionOpen_Rencent)
        self.menuHelp.addAction(self.actionSupport)
        self.menubar.addAction(self.menukkbox.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KKBOX"))
        self.release_label.setText(_translate("MainWindow", "類型"))
        self.comboBox_release.setItemText(0, _translate("MainWindow", "新歌"))
        self.comboBox_release.setItemText(1, _translate("MainWindow", "單曲"))
        self.lang_label.setText(_translate("MainWindow", "曲風"))
        self.comboBox_lang.setItemText(0, _translate("MainWindow", "本地"))
        self.comboBox_lang.setItemText(1, _translate("MainWindow", "簡中"))
        self.comboBox_lang.setItemText(2, _translate("MainWindow", "日文"))
        self.comboBox_lang.setItemText(3, _translate("MainWindow", "英文"))
        self.comboBox_lang.setItemText(4, _translate("MainWindow", "韓文"))
        self.place_label.setText(_translate("MainWindow", "地區"))
        self.comboBox_place.setItemText(0, _translate("MainWindow", "台灣"))
        self.comboBox_place.setItemText(1, _translate("MainWindow", "日本"))
        self.comboBox_place.setItemText(2, _translate("MainWindow", "全球"))
        self.comboBox_place.setItemText(3, _translate("MainWindow", "歐美"))
        self.comboBox_place.setItemText(4, _translate("MainWindow", "香港"))
        self.comboBox_place.setItemText(5, _translate("MainWindow", "新加坡"))
        self.comboBox_place.setItemText(6, _translate("MainWindow", "馬來西亞"))
        self.pushButton_OK.setText(_translate("MainWindow", "OK"))
        self.pushButton_Cancel.setText(_translate("MainWindow", "Cancel"))
        self.now_playing_song.setText(_translate("MainWindow", "Song"))
        self.time_label.setText(_translate("MainWindow", "--/--"))
        self.pushButton_lyris.setText(_translate("MainWindow", "lyris"))
        self.show_result_label.setText(_translate("MainWindow", "Search_Result"))
        self.show_result_label_2.setText(_translate("MainWindow", "Select_Result"))
        self.pushButton.setText(_translate("MainWindow", "本地音樂"))
        self.pushButton_2.setText(_translate("MainWindow", "串流音樂"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.menukkbox.setTitle(_translate("MainWindow", "kkbox"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_create_new_playlist.setText(_translate("MainWindow", "Create new playlist"))
        self.action_create_new_playlist.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Space"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setShortcut(_translate("MainWindow", "Ctrl+."))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionNext.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.actionPrevious.setText(_translate("MainWindow", "Previous"))
        self.actionPrevious.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.actionVolume_Up.setText(_translate("MainWindow", "Volume Up"))
        self.actionVolume_Up.setShortcut(_translate("MainWindow", "Ctrl+Up"))
        self.actionVolume_Down.setText(_translate("MainWindow", "Volume Down"))
        self.actionVolume_Down.setShortcut(_translate("MainWindow", "Ctrl+Down"))
        self.actionSupport.setText(_translate("MainWindow", "Support"))
        self.actionSuffle.setText(_translate("MainWindow", "Shuffle"))
        self.actionRepeat.setText(_translate("MainWindow", "Repeat"))
        self.actionOpen.setText(_translate("MainWindow", "Open File"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionAbout_kkbox.setText(_translate("MainWindow", "About"))
        self.actionOpen_Dir.setText(_translate("MainWindow", "Open Dir"))
        self.actionOpen_Rencent.setText(_translate("MainWindow", "Open Recent"))
