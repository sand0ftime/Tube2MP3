# -*- coding: utf-8 -*-

"""

 ▗▄▄▖▗▄▄▖ ▗▄▄▄▖ ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄     ▗▄▄▖▗▖  ▗▖     ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄ ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖
▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌ █  ▐▌   ▐▌  █    ▐▌ ▐▌▝▚▞▘     ▐▌   ▐▌ ▐▌▐▛▚▖▐▌▐▌  █▐▌     █    █  ▐▛▚▞▜▌▐▌
▐▌   ▐▛▀▚▖▐▛▀▀▘▐▛▀▜▌ █  ▐▛▀▀▘▐▌  █    ▐▛▀▚▖ ▐▌       ▝▀▚▖▐▛▀▜▌▐▌ ▝▜▌▐▌  █▐▛▀▀▘  █    █  ▐▌  ▐▌▐▛▀▀▘
▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌ █  ▐▙▄▄▖▐▙▄▄▀    ▐▙▄▞▘ ▐▌      ▗▄▄▞▘▐▌ ▐▌▐▌  ▐▌▐▙▄▄▀▐▌     █  ▗▄█▄▖▐▌  ▐▌▐▙▄▄▖


 ▗▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖  ▗▄▄▖▗▄▄▄▖ ▗▄▖      ▗▖  ▗▖▗▄▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▄▄▄▄▖ ▗▄▖ ▗▖ ▗▖▗▄▄▄▖
▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌     █  ▐▌ ▐▌     ▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌  █     ▗▞▘▐▌ ▐▌▐▌▗▞▘  █
▐▌▝▜▌▐▛▀▀▘▐▌ ▐▌▐▛▀▚▖▐▌▝▜▌  █  ▐▛▀▜▌     ▐▌ ▝▜▌▐▛▀▀▘▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌  █   ▗▞▘  ▐▛▀▜▌▐▛▚▖   █
▝▚▄▞▘▐▙▄▄▖▝▚▄▞▘▐▌ ▐▌▝▚▄▞▘▗▄█▄▖▐▌ ▐▌     ▐▌  ▐▌▐▙▄▄▖▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌  █  ▐▙▄▄▄▖▐▌ ▐▌▐▌ ▐▌▗▄█▄▖

"""

import yt_dlp
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, QUrl, Qt, QTimer)
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import (QAction, QCursor, QFont, QIcon, QMovie)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QLabel, QProgressBar, QPushButton, QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
                               QTextBrowser, QTextEdit, QWidget, QFileDialog)


def __init__(self, url, browser, textBrowser, progressBar):
    super().__init__()
    self.url = url
    self.browser = browser
    self.textBrowser = textBrowser
    self.progressBar = progressBar


class Ui_MainWindow(object):

    ###FUNCTION FOR BROWSE BUTTON#####
    def __init__(self):
        self.on_task_finished = None
        self.browser = None

    # DOWNLOAD FUNCTION
    def run(self):
        url = self.textEdit_2.toPlainText()  # Convert the link to plain text to use it
        self.textBrowser.setText("Downloading!!")
        try:
            ydl_opts = {
                'format': 'm4a/bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                }]
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # Use the URL

            self.textBrowser.setText("Download complete... In " + self.browser + "\n")
            self.progressBar.setProperty("value", 100)
        except Exception as e:
            self.textBrowser.setText(f"ERROR: {str(e)}")
        finally:
            self.progressBar.setProperty("value", 0)

    def browse_files(self):
        self.textBrowser.setText("Browsing!!!")
        global browser
        browser = str(QFileDialog.getExistingDirectory(self, "Select Directory 📂")) + r'/'
        self.textBrowser.setText(browser)

    ###FUNCTION FOR BITCOIN BUTTON#####
    def bitcoin(self):
        self.textBrowser.setText("Bitcoin Adress : bc1qf3u7s9ckwj8avhc6e4u7g9c5a7fzq9503jd9xj")

        ###FUNCTION FOR PAYPAL BUTTON#####

    def paypal(self):
        self.textBrowser.setText("Paypal Adress: https://paypal.me/MonsieurRobotCA?country.x=CA&locale.x=en_US")


    ###########PROGRESS BAR###########
    def update_progress(self):
        # Add 1 %
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 100
            self.timer.stop()  # Stop the timer when the progress reaches 100
            self.is_running = False  # Stop the download bar
        self.progressBar.setValue(self.progress_value)

    #############SINGLE LINK##########

    def singleToggled(self):
        ##Hide multiple links if not checked####
        if self.radioButton.isChecked():
            self.textEdit_3.hide()
            self.textEdit_4.hide()
            self.textEdit_5.hide()
            self.textEdit_6.hide()
            self.textEdit.hide()
            self.textEdit.clear()
            self.textEdit_3.clear()
            self.textEdit_4.clear()
            self.textEdit_5.clear()
            self.textEdit_6.clear()
            # Set text browser text to single link
            self.textBrowser.setText("Single link....")
            # When pushbutton is clicked it will connect to the function
            self.pushButton.clicked.connect(self.run())

    ############ON CLICK#############
    def on_button_click(self):
        if self.is_running:
            # Stop the timer if it's running
            self.timer.stop()
            self.is_running = False
        else:
            # Start the timer if it's not running
            self.timer.start(400)  # Update every 100 milliseconds
            self.is_running = True

        ###FUNCTION TO SHOW THE TEXT AREA MULTIPLE LINKS####

    def radioToggled(self):
        ##show multiple links if checked####
        if self.radioButton_2.isChecked():
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()
            self.textEdit_6.show()
            self.textEdit.show()
            self.textEdit_2.clear()
            self.textBrowser.setText("Multiple links....")

    def theme(self):
        ##show multiple links if checked####
        if self.radioButton_6.isChecked():
            print("checked! #6")
            global yellow
            yellow = True
        if self.radioButton_7.isChecked():
            print("checked! #7")
            global dark
            dark = True
        if self.radioButton_8.isChecked():
            print("checked! #8")
            global light
            light = True
        if self.radioButton_9.isChecked():
            print("checked! #9")
            purple = True
        return self

    def file_type(self):
        ##show multiple links if checked####
        if self.radioButton_4.isChecked():
            print("checked! MP4!")
            global mp4
            mp4 = True

        if self.radioButton_3.isChecked():
            print("checked! MP3!")
            global mp3
            mp4 = True

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setIconSize(QSize(70, 70))
        self.actionA = QAction(MainWindow)
        self.actionA.setObjectName(u"actionA")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(9, 266, 761, 28))
        self.textEdit_4.setMaximumSize(QSize(16777215, 28))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(12)

        self.textEdit_4.setFont(font1)
        self.textEdit_4.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(9, 198, 761, 28))
        self.textEdit_2.setMinimumSize(QSize(200, 28))
        self.textEdit_2.setMaximumSize(QSize(16777215, 28))
        self.textEdit_2.setFont(font1)
        self.textEdit_2.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(9, 402, 761, 28))
        self.progressBar.setMaximumSize(QSize(16777215, 28))
        self.progressBar.setValue(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(9, 368, 761, 28))
        self.textEdit.setMaximumSize(QSize(16777215, 28))
        self.textEdit.setFont(font1)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(9, 334, 761, 28))
        self.textEdit_6.setMaximumSize(QSize(16777215, 28))
        self.textEdit_6.setFont(font1)
        self.textEdit_6.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.movie = QMovie("tube2mp3.gif")
        self.label_2.setMovie(self.label_2.movie)
        self.label_2.movie.start()
        self.label_2.setGeometry(QRect(10, 10, 330, 111))
        self.label_2.setMinimumSize(QSize(330, 100))
        self.label_2.setMaximumSize(QSize(330, 111))
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(9, 300, 761, 28))
        self.textEdit_5.setMaximumSize(QSize(16777215, 28))
        self.textEdit_5.setFont(font1)
        self.textEdit_5.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(9, 232, 761, 28))
        self.textEdit_3.setMinimumSize(QSize(200, 28))
        self.textEdit_3.setMaximumSize(QSize(16777215, 28))
        self.textEdit_3.setFont(font1)
        self.textEdit_3.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.movie = QMovie("giphy.gif")
        self.label_3.setMovie(self.label_3.movie)
        self.label_3.movie.start()
        self.label_3.setGeometry(QRect(9, 436, 221, 191))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(350, 440, 421, 150))
        self.textBrowser.setMaximumSize(QSize(16777215, 150))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        # Enable opening external links in the default browser
        self.label.setOpenExternalLinks(True)
        # Set text interaction flags to enable link clicking
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label.setGeometry(QRect(10, 160, 210, 23))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Sans Bold"])
        font1.setBold(True)
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.browse_files)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 440, 100, 65))
        self.pushButton_2.setMinimumSize(QSize(100, 65))
        self.pushButton_2.setMaximumSize(QSize(250, 65))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.on_button_click)

        # Timer for updating the progress bar
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.is_running = False  # Flag to check if progress bar is running

        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 510, 100, 65))
        self.pushButton.setMinimumSize(QSize(100, 65))
        self.pushButton.setMaximumSize(QSize(250, 65))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(350, 0, 421, 171))
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Links = QWidget()
        self.Links.setObjectName(u"Links")
        self.radioButton_2 = QRadioButton(self.Links)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 150, 20))
        self.radioButton_2.setMinimumSize(QSize(150, 20))
        self.radioButton_2.setMaximumSize(QSize(150, 20))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(12)
        self.radioButton_2.setFont(font3)
        self.radioButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_2.clicked.connect(self.radioToggled)
        self.radioButton = QRadioButton(self.Links)
        self.radioButton.clicked.connect(self.singleToggled)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.setGeometry(QRect(10, 10, 150, 20))
        self.radioButton.setMinimumSize(QSize(150, 20))
        self.radioButton.setMaximumSize(QSize(150, 20))
        self.radioButton.setFont(font3)
        self.radioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.radioButton_4 = QRadioButton(self.tab_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 10, 146, 28))
        self.radioButton_4.setFont(font3)
        self.radioButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_4.clicked.connect(self.file_type)
        self.radioButton_3 = QRadioButton(self.tab_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setGeometry(QRect(10, 40, 146, 28))
        self.radioButton_3.setFont(font3)
        self.radioButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_3.clicked.connect(self.file_type)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font3)
        self.radioButton_6 = QRadioButton(self.tab_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 35, 181, 21))
        self.radioButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_6.clicked.connect(self.theme)
        self.radioButton_7 = QRadioButton(self.tab_3)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(10, 60, 181, 21))
        self.radioButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_7.clicked.connect(self.theme)
        self.radioButton_8 = QRadioButton(self.tab_3)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(10, 80, 171, 21))
        self.radioButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_8.clicked.connect(self.theme)
        self.radioButton_9 = QRadioButton(self.tab_3)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setChecked(True)
        self.radioButton_9.setGeometry(QRect(10, 10, 201, 21))
        self.radioButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_9.clicked.connect(self.theme)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.bitcoin_button = QPushButton(self.tab)
        self.bitcoin_button.setObjectName(u"bitcoin_button")
        self.bitcoin_button.setGeometry(QRect(0, 10, 121, 50))
        self.bitcoin_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bitcoin_button.clicked.connect(self.bitcoin)
        self.paypal_button = QPushButton(self.tab)
        self.paypal_button.setObjectName(u"paypal_button")
        self.paypal_button.setGeometry(QRect(0, 70, 121, 50))
        self.paypal_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.paypal_button.clicked.connect(self.paypal)
        self.textEdit_7 = QTextEdit(self.tab)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(130, 10, 281, 111))
        self.tabWidget.addTab(self.tab, "")
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setObjectName(u"webView")
        self.webView.setGeometry(QRect(780, 0, 591, 791))
        self.webView.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.webView.setProperty("url", QUrl(u"https://www.youtube.com"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TubetoMP3", None))
        self.actionA.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.textEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.label_2.setText("")
        self.textEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input a link here...", None))
        self.label_3.setText("")
        #if QT_CONFIG(tooltip)
        self.textBrowser.setToolTip("")
        #endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      '<a href="https://gitlab.com/sand0ftime1/tube2mp3" style="color: yellow; text-decoration: none;">Made by Sand0fTime</a>',
                                                      None))
        #if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"Where will your .mp3 end up. (Output)", None))
        #endif // QT_CONFIG(tooltip)
        #if QT_CONFIG(whatsthis)
        self.pushButton_2.setWhatsThis("")
        #endif // QT_CONFIG(whatsthis)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        #if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"Choose if you want to download from one source or more", None))
        #endif // QT_CONFIG(whatsthis)
        #if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"If you want to download multiple songs", None))
        #endif // QT_CONFIG(tooltip)
        #if QT_CONFIG(statustip)
        self.radioButton_2.setStatusTip("")
        #endif // QT_CONFIG(statustip)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Multiple links", None))
        #if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"If you want to download only one song", None))
        #endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Single link", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.Links),
                                  #QCoreApplication.translate("MainWindow", u"Links", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"File type", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Electric yellow", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Electric purple", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("MainWindow", u"Theme", None))
        self.bitcoin_button.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.paypal_button.setText(QCoreApplication.translate("MainWindow", u"PAYPAL", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow",
                                                           u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "hr { height: 1px; border-width: 0; }\n"
                                                           "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                           "li.checked::marker { content: \"\\2612\"; }\n"
                                                           "</style></head><body style=\" font-family:'Ubuntu Sans Bold'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu','Ubuntu'; vertical-align:super;\">If you really appreciate my work and want to donate click on one of the following buttons. Thank you for using my software!</span></p></body></html>",
                                                           None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"Donate", None))
    # retranslateUi
