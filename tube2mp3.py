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
import PySide6.QtGui
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

    # FUNCTION FOR BROWSE BUTTON
    def __init__(self):
        self.on_task_finished = None
        self.browser = None

    # DOWNLOAD FUNCTION
    def run(self):
        url = self.link_InputBox.toPlainText()  # Convert the link to plain text to use it
        self.notification_Box.setText("Downloading!!")  # Set the text in the notification box to "Downloading!!"
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

            self.notification_Box.setText("Download complete... In " + self.browser + "\n")
            self.progressBar.setProperty("value", 100)
        except Exception as e:
            self.notification_Box.setText(f"ERROR: {str(e)}")
        finally:
            self.progressBar.setProperty("value", 0)

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

        ###FUNCTION TO SHOW THE TEXT AREA MULTIPLE LINKS####

    def theme(self):
        ##show multiple links if checked####
        if self.buttonElectric_Theme.isChecked():
            print("checked! Yellow Electric")
            global yellow
            yellow = True
        if self.buttonDark_Theme.isChecked():
            print("checked! Dark theme")
            global dark
            dark = True
        if self.buttonLight_Theme.isChecked():
            print("checked! Light theme")
            global light
            light = True
        if self.buttonPurpleElectric_Theme.isChecked():
            print("checked! Purple Electric")
            purple = True
        return self

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

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.movie = PySide6.QtGui.QMovie("tube2mp3.gif")
        self.label_2.setMovie(self.label_2.movie)
        self.label_2.movie.start()
        self.label_2.setGeometry(QRect(10, 10, 330, 111))
        self.label_2.setMinimumSize(QSize(330, 100))
        self.label_2.setMaximumSize(QSize(330, 111))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.movie = PySide6.QtGui.QMovie("giphy.gif")
        self.label_3.setMovie(self.label_3.movie)
        self.label_3.movie.start()
        self.label_3.setGeometry(QRect(9, 436, 221, 191))
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
        self.label.setGeometry(QRect(10, 160, 210, 23))
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
        self.pushButton.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.mp4_Button = QRadioButton(self.tab_2)
        self.mp4_Button.setObjectName(u"buttonSingle_Link_4")
        self.mp4_Button.setGeometry(QRect(10, 10, 146, 28))
        self.mp4_Button.setFont(font3)
        self.mp4_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.mp4_Button.clicked.connect(self.file_type)
        self.mp3_Button = QRadioButton(self.tab_2)
        self.mp3_Button.setObjectName(u"buttonSingle_Link_3")
        self.mp3_Button.setChecked(True)
        self.mp3_Button.setGeometry(QRect(10, 40, 146, 28))
        self.mp3_Button.setFont(font3)
        self.mp3_Button.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.mp3_Button.clicked.connect(self.file_type)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font3)
        self.buttonElectric_Theme = QRadioButton(self.tab_3)
        self.buttonElectric_Theme.setObjectName(u"buttonElectric_Theme")
        self.buttonElectric_Theme.setGeometry(QRect(10, 35, 181, 21))
        self.buttonElectric_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonElectric_Theme.clicked.connect(self.theme)
        self.buttonDark_Theme = QRadioButton(self.tab_3)
        self.buttonDark_Theme.setObjectName(u"buttonDark_Theme")
        self.buttonDark_Theme.setGeometry(QRect(10, 60, 181, 21))
        self.buttonDark_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonDark_Theme.clicked.connect(self.theme)
        self.buttonLight_Theme = QRadioButton(self.tab_3)
        self.buttonLight_Theme.setObjectName(u"buttonLight_Theme")
        self.buttonLight_Theme.setGeometry(QRect(10, 80, 171, 21))
        self.buttonLight_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonLight_Theme.clicked.connect(self.theme)
        self.buttonPurpleElectric_Theme = QRadioButton(self.tab_3)
        self.buttonPurpleElectric_Theme.setObjectName(u"buttonPurpleElectric_Theme")
        self.buttonPurpleElectric_Theme.setChecked(True)
        self.buttonPurpleElectric_Theme.setGeometry(QRect(10, 10, 201, 21))
        self.buttonPurpleElectric_Theme.setCursor(PySide6.QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonPurpleElectric_Theme.clicked.connect(self.theme)
        self.tabWidget.addTab(self.tab_3, "")
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
                                                                         u"Input a YouTube link here press enter after each link for multiple download.",
                                                                         None))

        self.label_2.setText("")

        self.label_3.setText("")
        #if QT_CONFIG(tooltip)
        self.notification_Box.setToolTip("")
        #endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      '<a href="https://github.com/sand0ftime/Tube2MP3.git" style="color: yellow; text-decoration: none;">Made by Sand0fTime</a>',
                                                      None))
        #if QT_CONFIG(tooltip)
        self.browse_Button.setToolTip(
            QCoreApplication.translate("MainWindow", u"Where will your .mp3 end up. (Output)", None))
        #endif // QT_CONFIG(tooltip)
        #if QT_CONFIG(whatsthis)
        self.browse_Button.setWhatsThis("")
        #endif // QT_CONFIG(whatsthis)
        self.browse_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        #if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"Choose if you want to download from one source or more", None))
        self.mp4_Button.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.mp3_Button.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"File type", None))
        self.buttonElectric_Theme.setText(QCoreApplication.translate("MainWindow", u"Electric yellow", None))
        self.buttonDark_Theme.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.buttonLight_Theme.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.buttonPurpleElectric_Theme.setText(QCoreApplication.translate("MainWindow", u"Electric purple", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
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