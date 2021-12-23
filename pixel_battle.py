import sys
import time
import numpy as np
import re
import socket
import pickle
from time import sleep
from PIL import Image

# from Player import Player

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic


class PixelBattle(QMainWindow):

    def __init__(self):
        super().__init__()
        self.game_size = (50, 50)
        self.x = 0
        self.y = 0
        self.setWindowIcon(QIcon('icon_upper_left_corner.png'))
        uic.loadUi('pixel_battle.ui', self)     # перетягивает все с шаблона, этот же шаблон,
        # но в .py есть в pixel_battle_window.py

        self.key_pressed_count = 0

        self.create_grind()
        self.set_color()

    def create_grind(self):
        self.under_the_btn = np.zeros(self.game_size, dtype=str)
        self.btns = np.zeros(self.game_size, dtype=QPushButton)
        self.open = np.zeros(self.game_size, dtype=bool)

        # создание сетки кнопок
        for i in range(self.game_size[0]):
            for j in range(self.game_size[1]):
                btn = QPushButton('white', self.game_frame)
                btn.setGeometry(i * 10, j * 10, 12, 12)
                btn.clicked.connect(lambda state, obj=btn, x=i, y=j: self.button_pushed(obj, x, y))
                btn.setStyleSheet("background-color: white; color: white;")
                self.btns[i][j] = btn
        self.show()
        self.push_color_btn()
        self.save_btn_pushed()

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
        if args == ():  # проверяет есть ли в args что-нибудь, для случаев, когда игрок начал рисовть не выбрав цвет
            self.color = ['black']
        else:
            self.color = args

    def button_pushed(self, obj, x, y):
        clr = self.color[0]
        self.btns[x][y].setText(f'{clr}')   # изменяется текст в "пикселе"
        self.btns[x][y].setStyleSheet(f"background-color: {clr}; color: {clr}")


    def save_btn_pushed(self):
        self.save_pic.clicked.connect(lambda: self.save_picture())

    def save_picture(self):
        pix_ar = np.zeros(shape=(self.game_size[0], self.game_size[1], 3), dtype=np.uint8)
        for i in range(self.game_size[0]):
            for j in range(self.game_size[1]):
                pix = self.btns[i][j].text()
                pix_ar[j][i] = self.pix_color(pix)
        image = Image.fromarray(pix_ar)
        image = image.resize((500, 500), resample=Image.NEAREST)
        tm = time.asctime()
        tm2 = tm.replace(':', '_')
        tm3 = tm2.replace(' ', '_')
        image.save(f"{tm3}.jpg")

    def pix_color(self, pix):
        colors = {
                    'black': [0, 0, 0],
                    'white': [255, 255, 255],
                    'red': [255, 0, 0],
                    'orange': [255, 165, 0],
                    'yellow': [255, 255, 0],
                    'green': [0, 255, 0],
                    'cyan': [0, 255, 255],
                    'blue': [0, 0, 255],
                    'purple': [128, 0, 128]
        }
        for color in colors.keys():
            if pix == color:
                pix_rgb = np.array(colors.get(pix), dtype=np.uint8)
                return pix_rgb


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PixelBattle()
    sys.exit(app.exec_())

