from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
import sys
import tube2mp3  # Import the tube2mp3 module
from tube2mp3 import Ui_MainWindow  # Import Ui_MainWindow from tube2mp3


class Tube2MP3(QtWidgets.QMainWindow, Ui_MainWindow):  # Changed to Tube2MP3 class name
    def __init__(self, parent=None):
        super(Tube2MP3, self).__init__(parent)  # Updated constructor to use Tube2MP3
        self.setupUi(self)


        # Connect the themeChanged signal to the method that changes the theme
        self.themeChanged.connect(self.change_theme)

    def change_theme(self, theme_file):
        """Change the theme when the signal is emitted."""
        try:
            # Attempt to load the selected theme file
            with open(theme_file, "r") as f:
                _style = f.read()
                self.setStyleSheet(_style)  # Apply the stylesheet to the app
            print(f"Theme '{theme_file}' applied successfully!")
        except FileNotFoundError:
            print(f"Theme file '{theme_file}' not found. Using default theme.")


def load_theme(app: QApplication):
    """Load the default theme if available."""
    try:
        with open("purple_theme.qss", "r") as f:  # You can change this to any default theme
            _style = f.read()
            app.setStyleSheet(_style)
    except FileNotFoundError:
        print("Default theme file not found. Proceeding with default theme.")


def main():
    """Main function to initialize and run the app."""
    app = QApplication(sys.argv)

    # Load the default theme at the start
    load_theme(app)

    # Create and show the main window with the new class name (Tube2MP3)
    form = Tube2MP3()  # Change this line to instantiate Tube2MP3 instead of ExampleApp
    form.show()

    # Start the application's event loop
    app.exec()


if __name__ == "__main__":
    main()
