from PySide6 import QtWidgets
import tube2mp3
from tube2mp3 import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication


class ExampleApp(QtWidgets.QMainWindow, tube2mp3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


def main():
    form = ExampleApp()
    form.show()
    app.exec()


app = QApplication(sys.argv)
# Select the theme by opening theme.qss
if __name__ == '__main__':
    if Ui_MainWindow.theme:
        with open("theme.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
    # Call the main function
    main()
