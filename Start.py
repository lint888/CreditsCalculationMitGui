import sys

from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets






def main():
    app=QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    #button = QtWidgets.QPushButton("hello")
    #window.setCentralWidget(button)
    window.setWindowTitle("Start")
    window.textbox = QLineEdit()
    window.textbox.resize(100,50)
    button = QtWidgets.QPushButton('calculate')
    window.resize(800,500)
    window.show()
    app.exec()

if __name__=='__main__':
    main()