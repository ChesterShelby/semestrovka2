import sys
import numpy as np
import socket
import pickle
from time import sleep

from Player import Player


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, Qt

"""
Кароче, я удалил все лишние классы, чтобы они тебе не мешали разобраться в коде, впринципе они(эти классы)
с пояснениями есть в примере кода препода. Здесь оставил только класс, отвечающий за игру, похже добавлю возможность 
скрина, вроде это не сложно. Оставил тебе коментарии, чтобы было проще разобраться. Так же потом хотел добавить 
"стерку", но это не обязательно. Если что пиши)
"""


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
        if args == ():  # проверяет есть ли в args что-нибудь, для случаев, когда игрок начал рисовть не выбрав цвет
            self.color = 'rgb(0, 0, 0)'
        else:
            self.color = args

    def button_pushed(self, obj, x, y):
        if self.color != 'rgb(0, 0, 0)':
            clr = list(map(''.join, self.color))    # превращает tuple в массив с 1 элементом, цветом кнопки
        else:
            clr = self.color
        self.btns[x][y].setText(f'{clr}')   # изменяется текст в "пикселе"
        self.btns[x][y].setStyleSheet(f"background-color: {clr[0]}; color: {clr[0]}")   # меняется фон и цвет текста
        # print(self.btns[x][y].text())   # можешь посмотреть как выводится цвет


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PixelBattle()
    sys.exit(app.exec_())

