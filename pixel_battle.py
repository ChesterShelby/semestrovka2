import sys
import time
import numpy as np
import socket
import pickle
from time import sleep
from PIL import Image

from Player import Player

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic

SIZE_OF_PART = 1024


class ParallelConnection(QThread):

    sendPlayerObject = pyqtSignal(object)

    def __init__(self, ip, port, player: Player):
        super().__init__()

        self.sock = socket.socket()
        self.sock.connect((ip, port))
        self.player = player

    def send(self):
        bytes_array = pickle.dumps(self.player)
        print(self.player.clr, self.player.x, self.player.y, 'was send on server')
        self.sock.send(bytes_array)
        self.recieve()
        sleep(0.2)

    def recieve(self):
        while True:
            data = self.sock.recv(SIZE_OF_PART)
            another_player = pickle.loads(data)
            print(f'Получил вот это {another_player}')
            self.sendPlayerObject.emit(another_player)
            return another_player

    def run(self):
        while True:
            self.send()

    def change_player(self, x, y, clr):
        print('Пора менять знаения')
        self.player.x = x
        self.player.y = y
        self.player.clr = clr
        print('lol', self.player.x, self.player.y, self.player.clr)


class PixelBattle(QMainWindow):

    keyPressedSignal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.game_size = (50, 50)
        self.x = 0
        self.y = 0
        self.setWindowIcon(QIcon('icon_upper_left_corner.png'))
        uic.loadUi('pixel_battle.ui', self)
        self.player = Player(0, 0, 'black')

        self.init_gui()
        self.set_color()
        self.colors = {
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
        self.btn_connect.clicked.connect(lambda: self.establish_connection())
        self.push_color_btn()
        self.save_btn_pushed()
        self.show()

    def init_gui(self):

        self.btns = np.zeros(self.game_size, dtype=QPushButton)
        # создание сетки кнопок
        for i in range(self.game_size[0]):
            for j in range(self.game_size[1]):
                btn = QPushButton('white', self.game_frame)
                btn.setGeometry(i * 10, j * 10, 12, 12)
                btn.clicked.connect(lambda state, x=i, y=j: self.button_pushed(x, y))
                btn.setStyleSheet("background-color: white; color: white;")
                self.btns[i][j] = btn

        print('start')

    def establish_connection(self):
        print('try connected')
        ip = self.field_ip.text()
        port = int(self.field_port.text())

        self.player_parallel = ParallelConnection(ip, port, self.player)
        self.player_parallel.start()

        self.player_parallel.sendPlayerObject.connect(self.player_draw)
        print('ip, port =', ip, port)

    def keyPressEvent(self, event):
        self.keyPressedSignal.emit(event.key())

    @pyqtSlot(object)
    def player_draw(self, another_player):
        print('kek', type(another_player))

        x = another_player.x
        y = another_player.y
        clr = another_player.clr
        self.btns[x][y].setText(f'{clr}')  # изменяется текст в "пикселе"
        self.btns[x][y].setStyleSheet(f"background-color: {clr}; color: {clr}")
        self.player_parallel.change_player(x, y, clr)
        print('Закрасили пиксель')

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
        if args == ():
            self.color = ['black']
        else:
            self.color = args
        print(f'Выбран цвет {self.color[0]}')

    def button_pushed(self, x, y):
        self.player_parallel.change_player(x, y, self.color[0])
        print(x, y, self.color[0], 'Вот это идет в Player')
        # self.draw_in_gui(x, y)
    #
    # def draw_in_gui(self, x, y):
    #     clr = self.color[0]
    #     self.btns[x][y].setText(f'{clr}')  # изменяется текст в "пикселе"
    #     self.btns[x][y].setStyleSheet(f"background-color: {clr}; color: {clr}")

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
        for color in self.colors.keys():
            if pix == color:
                pix_rgb = np.array(self.colors.get(pix), dtype=np.uint8)
                return pix_rgb


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PixelBattle()
    sys.exit(app.exec_())

