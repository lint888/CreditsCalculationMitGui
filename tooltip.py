import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class Tooltip(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif',10))
        self.setToolTip("this is a button")
        btn = QPushButton('Button',self)
        btn.setToolTip('this is a widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltip')
        self.show()
