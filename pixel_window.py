import sys
import random
import numpy as np
import socket
import pickle
from time import sleep

from Player import Player

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, Qt


class PixelBattle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game_size = (50, 50)
        self.x = 0
        self.y = 0
        self.create_grind()

    def create_grind(self):

        self.setWindowIcon(QIcon('icon.png'))
        uic.loadUi('pixel_battle.ui', self)

        self.under_the_btn = np.zeros(self.game_size, dtype=str)
        self.btns = np.zeros(self.game_size, dtype=QPushButton)
        self.open = np.zeros(self.game_size, dtype=bool)

        for i in range(self.game_size[0]):
            for j in range(self.game_size[1]):
                btn = QPushButton(None, self.game_frame)
                btn.setGeometry(i * 10, j * 10, 12, 12)
                btn.clicked.connect(lambda state, obj=btn, x=i, y=j: self.button_pushed(obj, x, y))
                self.btns[i][j] = btn
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PixelBattle()
    sys.exit(app.exec_())