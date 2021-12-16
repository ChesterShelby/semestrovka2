# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pixel_battle.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(10, 320, 166, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.game_frame = QtWidgets.QFrame(self.centralwidget)
        self.game_frame.setGeometry(QtCore.QRect(190, 10, 500, 500))
        self.game_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_frame.setObjectName("game_frame")
        self.frame_rooms = QtWidgets.QFrame(self.centralwidget)
        self.frame_rooms.setGeometry(QtCore.QRect(10, 10, 171, 211))
        self.frame_rooms.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rooms.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rooms.setObjectName("frame_rooms")
        self.result_field = QtWidgets.QTextEdit(self.centralwidget)
        self.result_field.setGeometry(QtCore.QRect(10, 360, 171, 151))
        self.result_field.setReadOnly(True)
        self.result_field.setObjectName("result_field")
        self.field_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.field_ip.setGeometry(QtCore.QRect(10, 230, 171, 25))
        self.field_ip.setObjectName("field_ip")
        self.field_port = QtWidgets.QLineEdit(self.centralwidget)
        self.field_port.setGeometry(QtCore.QRect(10, 260, 171, 25))
        self.field_port.setObjectName("field_port")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(10, 290, 171, 25))
        self.btn_connect.setObjectName("btn_connect")
        self.red = QtWidgets.QPushButton(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(10, 540, 30, 30))
        self.red.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.red.setObjectName("red")
        self.orange = QtWidgets.QPushButton(self.centralwidget)
        self.orange.setGeometry(QtCore.QRect(40, 540, 30, 30))
        self.orange.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 85, 0);")
        self.orange.setObjectName("orange")
        self.yellow = QtWidgets.QPushButton(self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(70, 540, 30, 30))
        self.yellow.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(255, 255, 0);")
        self.yellow.setObjectName("yellow")
        self.green = QtWidgets.QPushButton(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(100, 540, 30, 30))
        self.green.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);")
        self.green.setObjectName("green")
        self.blue = QtWidgets.QPushButton(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(130, 540, 30, 30))
        self.blue.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 255, 255);")
        self.blue.setObjectName("blue")
        self.dark_blue = QtWidgets.QPushButton(self.centralwidget)
        self.dark_blue.setGeometry(QtCore.QRect(160, 540, 30, 30))
        self.dark_blue.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 255);")
        self.dark_blue.setObjectName("dark_blue")
        self.purple = QtWidgets.QPushButton(self.centralwidget)
        self.purple.setGeometry(QtCore.QRect(190, 540, 30, 30))
        self.purple.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(170, 0, 255);")
        self.purple.setObjectName("purple")
        self.white = QtWidgets.QPushButton(self.centralwidget)
        self.white.setGeometry(QtCore.QRect(220, 540, 30, 30))
        self.white.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.white.setObjectName("white")
        self.black = QtWidgets.QPushButton(self.centralwidget)
        self.black.setGeometry(QtCore.QRect(250, 540, 30, 30))
        self.black.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.black.setObjectName("black")
        self.save_pic = QtWidgets.QPushButton(self.centralwidget)
        self.save_pic.setGeometry(QtCore.QRect(500, 540, 181, 31))
        self.save_pic.setObjectName("save_pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_connect.setText(_translate("MainWindow", "Connect!"))
        self.red.setText(_translate("MainWindow", "rgb(255, 0, 0)"))
        self.orange.setText(_translate("MainWindow", "rgb(255, 85, 0)"))
        self.yellow.setText(_translate("MainWindow", "rgb(255, 255, 0)"))
        self.green.setText(_translate("MainWindow", "rgb(0, 255, 0)"))
        self.blue.setText(_translate("MainWindow", "rgb(0, 255, 255)"))
        self.dark_blue.setText(_translate("MainWindow", " rgb(0, 0, 255)"))
        self.purple.setText(_translate("MainWindow", "rgb(170, 0, 255)"))
        self.white.setText(_translate("MainWindow", "rgb(255, 255, 255)"))
        self.black.setText(_translate("MainWindow", "rgb(0, 0, 0)"))
        self.save_pic.setText(_translate("MainWindow", "Save picture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())