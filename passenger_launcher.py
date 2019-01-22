import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from winds.welcome_ui import Ui_welcome
from winds.passenger_main_ui import Ui_mainWidow
import time
import threading


class Welcome(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.ui = Ui_welcome()
        self.ui.setupUi(self)
        self.show()

    def change_ui_to_main_window(self):
        self.ui = Ui_mainWidow()
        self.ui.setupUi(self)
        self.show()


def change_scene_to_main_window():
    ex.change_ui_to_main_window()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Welcome()
    change_scene_to_main_window()
    sys.exit(app.exec_())


