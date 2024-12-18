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
import time

import yt_dlp
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, QUrl, Qt, QTimer)
import PySide6.QtGui
from PySide6.QtCore import Signal
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QLabel, QProgressBar, QPushButton, QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
                               QTextBrowser, QTextEdit, QWidget, QFileDialog)


def __init__(self, url, browser, textBrowser, progressBar):
    super().__init__()
    self.url = url
    self.browser = browser
    self.notification_Box = textBrowser
    self.progressBar = progressBar



class Ui_MainWindow(object):
    themeChanged = Signal(str)  # Signal now passes a theme identifier (theme filename)
    global gif_logo
    # FUNCTION FOR BROWSE BUTTON
    def __init__(self):
        self.on_task_finished = None
        self.browser = None

    # DOWNLOAD FUNCTION
    def download_song(self):
        #parse the links from the textbrowser
        input_text=self.link_InputBox.toPlainText()
        #split multiple links in commas
        urls = [url.strip() for url in input_text.split(',') if url.strip()]
        self.notification_Box.setText("Downloading..")
        try:
            ydl_opts = {
                'format': 'm4a/bestaudio/best',
                'outtmpl': browser + '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for index,url in enumerate(urls):
                 ydl.download([url])  # Use the URL

            #this text will show when the download is complete
            self.progressBar.setProperty("value", 0)
            time.sleep(1)
            self.progressBar.setProperty("value", 100)
            self.notification_Box.append("Download complete...")


        except Exception as e:
            self.notification_Box.setText(f"ERROR: {str(e)}")
        finally:
            self.progressBar.setProperty("value", 0)

    # BROWSE BUTTON FUNCTION
    def browse_files(self):
        self.notification_Box.setText("Browsing!!!")
        global browser
        browser = str(QFileDialog.getExistingDirectory(self, "Select Directory 📂")) + r'/'
        self.notification_Box.setText(browser)

    ###FUNCTION FOR BITCOIN BUTTON#####
    def bitcoin(self):
        self.notification_Box.setText("Bitcoin Adress : bc1qf3u7s9ckwj8avhc6e4u7g9c5a7fzq9503jd9xj")

        ###FUNCTION FOR PAYPAL BUTTON#####

    def paypal(self):
        self.notification_Box.setText("Paypal Adress: https://paypal.me/MonsieurRobotCA?country.x=CA&locale.x=en_US")

    ###########PROGRESS BAR###########
    def update_progress(self):
        # Add 1 %
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 100
            self.timer.stop()  # Stop the timer when the progress reaches 100
            self.is_running = False  # Stop the download bar
        self.progressBar.setValue(self.progress_value)

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

    def on_change_theme(self, theme_file):
        """Emit signal with the selected theme's filename when the radio button is toggled."""

        # Check if the Purple Electric theme is selected
        if self.buttonPurpleElectric_Theme.isChecked():
            print('Purple Electric theme selected!')
            self.logo_Gif.movie = PySide6.QtGui.QMovie("purple_logo.gif")  # Set purple GIF
            self.themeChanged.emit(theme_file)  # Emit the selected theme filename

        # Check if the Dark theme is selected
        elif self.buttonDark_Theme.isChecked():
            print('Dark theme selected!')
            self.logo_Gif.movie = PySide6.QtGui.QMovie("dark_logo.gif")  # Set dark GIF
            self.themeChanged.emit(theme_file)  # Emit the selected theme filename

        # Check if the Light theme is selected
        elif self.buttonLight_Theme.isChecked():
            print('Light theme selected!')
            self.logo_Gif.movie = PySide6.QtGui.QMovie("light_logo.gif")  # Set light GIF
            self.themeChanged.emit(theme_file)  # Emit the selected theme filename

        # Check if the Yellow Electric theme is selected
        elif self.buttonElectric_Theme.isChecked():
            print('Yellow Electric theme selected!')
            self.logo_Gif.movie = PySide6.QtGui.QMovie("yellow_logo.gif")  # Set yellow GIF
            self.themeChanged.emit(theme_file)  # Emit the selected theme filename

        # Start the GIF animation
        if self.logo_Gif.movie:
            self.logo_Gif.movie.start()  # Ensure the GIF animation starts

    def file_type(self):
        ##show multiple links if checked####
        if self.mp4_Button.isChecked():
            print("checked! MP4!")
            global mp4
            mp4 = True

        if self.mp3_Button.isChecked():
            print("checked! MP3!")
            global mp3
            mp4 = True

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = PySide6.QtGui.QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = PySide6.QtGui.QIcon()
        icon.addFile(u"icon.png", QSize(), PySide6.QtGui.QIcon.Mode.Normal, PySide6.QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setIconSize(QSize(70, 70))
        self.actionA = PySide6.QtGui.QAction(MainWindow)
        self.actionA.setObjectName(u"actionA")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        font1 = PySide6.QtGui.QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(12)

        self.link_InputBox = QTextEdit(self.centralwidget)
        self.link_InputBox.setObjectName(u"link_InputBox")
        self.link_InputBox.setGeometry(QRect(9, 198, 761, 200))
        self.link_InputBox.setMinimumSize(QSize(200, 28))
        self.link_InputBox.setMaximumSize(QSize(16777215, 200))
        self.link_InputBox.setFont(font1)
        self.link_InputBox.viewport().setProperty("cursor", PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(9, 402, 761, 28))
        self.progressBar.setMaximumSize(QSize(16777215, 28))
        self.progressBar.setValue(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.logo_Gif = QLabel(self.centralwidget)
        self.logo_Gif.setObjectName(u"label_2")
        self.logo_Gif.setGeometry(QRect(10, 10, 330, 111))
        self.logo_Gif.setMinimumSize(QSize(330, 100))
        self.logo_Gif.setMaximumSize(QSize(330, 111))
        self.sand0ftime_Gif = QLabel(self.centralwidget)
        self.sand0ftime_Gif.setObjectName(u"label_3")
        self.sand0ftime_Gif.movie = PySide6.QtGui.QMovie("giphy.gif")
        self.sand0ftime_Gif.setMovie(self.sand0ftime_Gif.movie)
        self.sand0ftime_Gif.movie.start()
        self.sand0ftime_Gif.setGeometry(QRect(9, 436, 221, 191))
        self.notification_Box = QTextBrowser(self.centralwidget)
        self.notification_Box.setObjectName(u"textBrowser")
        self.notification_Box.setGeometry(QRect(350, 440, 421, 150))
        self.notification_Box.setMaximumSize(QSize(16777215, 150))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        # Enable opening external links in the default browser
        self.label.setOpenExternalLinks(True)
        # Set text interaction flags to enable link clicking
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label.setGeometry(QRect(575, 600, 210, 23))
        font2 = PySide6.QtGui.QFont()
        font2.setFamilies([u"Ubuntu Sans Bold"])
        font1.setBold(True)
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.browse_Button = QPushButton(self.centralwidget)
        self.browse_Button.clicked.connect(self.browse_files)
        self.browse_Button.setObjectName(u"pushButton_2")
        self.browse_Button.setGeometry(QRect(240, 440, 100, 65))
        self.browse_Button.setMinimumSize(QSize(100, 65))
        self.browse_Button.setMaximumSize(QSize(250, 65))
        self.browse_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.download_Button = QPushButton(self.centralwidget)
        self.download_Button.clicked.connect(self.download_song)

        # Timer for updating the progress bar
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.is_running = False  # Flag to check if progress bar is running

        self.download_Button.setObjectName(u"pushButton")
        self.download_Button.setGeometry(QRect(240, 510, 100, 65))
        self.download_Button.setMinimumSize(QSize(100, 65))
        self.download_Button.setMaximumSize(QSize(250, 65))
        self.download_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(350, 0, 421, 171))
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.Links = QWidget()
        self.Links.setObjectName(u"Links")
        font3 = PySide6.QtGui.QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(12)
        self.tab_FileType = QWidget()
        self.tab_FileType.setObjectName(u"tab_2")
        self.mp4_Button = QRadioButton(self.tab_FileType)
        self.mp4_Button.setObjectName(u"buttonSingle_Link_4")
        self.mp4_Button.setGeometry(QRect(10, 10, 146, 28))
        self.mp4_Button.setFont(font3)
        self.mp4_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.mp4_Button.clicked.connect(self.file_type)
        self.mp3_Button = QRadioButton(self.tab_FileType)
        self.mp3_Button.setObjectName(u"buttonSingle_Link_3")
        self.mp3_Button.setChecked(True)
        self.mp3_Button.setGeometry(QRect(10, 40, 146, 28))
        self.mp3_Button.setFont(font3)
        self.mp3_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.mp3_Button.clicked.connect(self.file_type)
        self.tabWidget.addTab(self.tab_FileType, "")
        self.theme_Tab = QWidget()
        self.theme_Tab.setObjectName(u"tab_3")
        self.theme_Tab.setFont(font3)
        self.buttonElectric_Theme = QRadioButton(self.theme_Tab)
        self.buttonElectric_Theme.setObjectName(u"buttonElectric_Theme")
        self.buttonElectric_Theme.setGeometry(QRect(10, 35, 181, 21))
        self.buttonElectric_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonElectric_Theme.toggled.connect(lambda: self.on_change_theme('yellow_theme.qss'))
        self.buttonDark_Theme = QRadioButton(self.theme_Tab)
        self.buttonDark_Theme.setObjectName(u"buttonDark_Theme")
        self.buttonDark_Theme.setGeometry(QRect(10, 60, 181, 21))
        self.buttonDark_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonDark_Theme.toggled.connect(lambda: self.on_change_theme('dark_theme.qss'))
        self.buttonLight_Theme = QRadioButton(self.theme_Tab)
        self.buttonLight_Theme.setObjectName(u"buttonLight_Theme")
        self.buttonLight_Theme.setGeometry(QRect(10, 80, 171, 21))
        self.buttonLight_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonLight_Theme.toggled.connect(lambda: self.on_change_theme('light_theme.qss'))
        self.buttonPurpleElectric_Theme = QRadioButton(self.theme_Tab)
        self.buttonPurpleElectric_Theme.setObjectName(u"buttonPurpleElectric_Theme")
        self.buttonPurpleElectric_Theme.setChecked(True)
        self.buttonPurpleElectric_Theme.setGeometry(QRect(10, 10, 201, 21))
        self.buttonPurpleElectric_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonPurpleElectric_Theme.toggled.connect(lambda: self.on_change_theme('purple_theme.qss'))
        self.tabWidget.addTab(self.theme_Tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.bitcoin_button = QPushButton(self.tab)
        self.bitcoin_button.setObjectName(u"bitcoin_button")
        self.bitcoin_button.setGeometry(QRect(0, 10, 121, 50))
        self.bitcoin_button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.bitcoin_button.clicked.connect(self.bitcoin)
        self.paypal_button = QPushButton(self.tab)
        self.paypal_button.setObjectName(u"paypal_button")
        self.paypal_button.setGeometry(QRect(0, 70, 121, 50))
        self.paypal_button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.paypal_button.clicked.connect(self.paypal)
        self.donateBox_Text = QTextEdit(self.tab)
        self.donateBox_Text.setObjectName(u"donateBox_Text")
        self.donateBox_Text.setGeometry(QRect(130, 10, 281, 111))
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

        self.link_InputBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                         u"Input a YouTube link here, add a comma after each link for multiple downloads.",
                                                                         None))

        self.logo_Gif.setText("")

        self.sand0ftime_Gif.setText("")
        #if QT_CONFIG(tooltip)
        self.notification_Box.setToolTip("")
        #endif // QT_CONFIG(tooltip)
        self.label.setText(
            QCoreApplication.translate("MainWindow",
                                       '<a href="https://github.com/sand0ftime/Tube2MP3.git">Made by Sand0fTime</a>',
                                       None
                                       )
        )
        #if QT_CONFIG(tooltip)
        self.browse_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Where will your .mp3 end up. (Output)", None))
        #endif // QT_CONFIG(tooltip)
        #if QT_CONFIG(whatsthis)
        self.browse_Button.setWhatsThis("")
        #endif // QT_CONFIG(whatsthis)
        self.browse_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.download_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        #if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"Choose if you want to download from one source or more", None))
        self.mp4_Button.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.mp3_Button.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FileType),
                                  QCoreApplication.translate("MainWindow", u"File type", None))
        self.buttonElectric_Theme.setText(QCoreApplication.translate("MainWindow", u"Electric Yellow", None))
        self.buttonDark_Theme.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.buttonLight_Theme.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.buttonPurpleElectric_Theme.setText(QCoreApplication.translate("MainWindow", u"Electric Purple", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.theme_Tab),
                                  QCoreApplication.translate("MainWindow", u"Theme", None))
        self.bitcoin_button.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.paypal_button.setText(QCoreApplication.translate("MainWindow", u"PAYPAL", None))
        self.donateBox_Text.setHtml(QCoreApplication.translate("MainWindow",
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
