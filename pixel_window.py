import sys
import numpy as np
import socket
import pickle
from time import sleep

from Player import Player
from pixel_battle_window import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic   # ?
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, Qt


SIZE_OF_PART = 1024


class ParallelConnection(QThread, Ui_MainWindow):
    sendPlayerObject = pyqtSignal(object)

    def __init__(self, ip, port, player):
        super().__init__()

        self.sock = socket.socket()
        self.sock.connect((ip, port))
        self.player = player

    def send(self):
        bytes_array = pickle.dumps(self.player)
        self.sock.send(bytes_array)
        bytes_array = self.recieve()
        sleep(0.2)

    def recieve(self):
        data = self.sock.recv(SIZE_OF_PART)
        another_player: Player = pickle.loads(data)

        self.sendPlayerObject.emit(another_player)

    def run(self):
        while True:
            self.send()

    def change_player_state(self, x, y):
        self.player.x = x
        self.player.y = y
        self.player.c = None


class ParallelCounter(QThread):
    sendTextSignal = pyqtSignal(str)

    def __init__(self, function):
        super().__init__()
        self.sendTextSignal.connect(function)
        self.key_pressed_count = 0

    def run(self):
        i = 0
        while i < 10e6:
            self.sendTextSignal.emit(f"Сейчас я {i}\nНажали {self.key_pressed_count} раз!")
            QThread.msleep(200)
            i += 1

    def set_pressed_count(self, count):
        self.key_pressed_count = count


class PixelBattle(QMainWindow):

    keyPressedSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.game_size = (50, 50)
        self.x = 0
        self.y = 0
        self.setWindowIcon(QIcon('icon_upper_left_corner.png'))
        uic.loadUi('pixel_battle.ui', self)

        self.key_pressed_count = 0
        # self.keyPressedSignal.connect(self.moving_by_key)

        self.create_grind()
        self.set_color()

    def create_grind(self):
        self.under_the_btn = np.zeros(self.game_size, dtype=str)
        self.btns = np.zeros(self.game_size, dtype=QPushButton)
        self.open = np.zeros(self.game_size, dtype=bool)

        # создание сетки кнопок
        for i in range(self.game_size[0]):
            for j in range(self.game_size[1]):
                btn = QPushButton(None, self.game_frame)
                btn.setGeometry(i * 10, j * 10, 12, 12)
                btn.clicked.connect(lambda state, obj=btn, x=i, y=j: self.button_pushed(obj, x, y))
                self.btns[i][j] = btn
        self.show()
        self.push_color_btn()

    def push_color_btn(self):

        self.red.clicked.connect(lambda : self.set_color(self.red.text()))
        self.orange.clicked.connect(lambda: self.set_color(self.orange.text()))
        self.yellow.clicked.connect(lambda: self.set_color(self.yellow.text()))
        self.green.clicked.connect(lambda: self.set_color(self.green.text()))
        self.blue.clicked.connect(lambda: self.set_color(self.blue.text()))
        self.dark_blue.clicked.connect(lambda: self.set_color(self.dark_blue.text()))
        self.purple.clicked.connect(lambda: self.set_color(self.purple.text()))
        self.white.clicked.connect(lambda: self.set_color(self.white.text()))
        self.black.clicked.connect(lambda: self.set_color(self.black.text()))

    def set_color(self, *args):
        if args == (): # проверяет есть ли в args что-нибудь, для случаев, когда игрок начал рисовть не выбрав цвет
            self.color = 'rgb(0, 0, 0)'
        else:
            self.color = args

    def button_pushed(self, obj, x, y):
        if self.color != 'rgb(0, 0, 0)':
            clr = list(map(''.join, self.color)) # превращает tuple в list
        else:
            clr = self.color
        self.btns[x][y].setStyleSheet(f"background-color: {clr[0]};")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PixelBattle()
    sys.exit(app.exec_())