import sys

from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLineEdit, QFormLayout
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5 import QtWidgets

class Textfield(QWidget):
    def __init__(self):
        super().__init__()
        Textfield1 = QLineEdit()
        Textfield1.setValidator(QIntValidator())

        Textfield2 = QLineEdit()
        Textfield2.setValidator(QIntValidator())
        credits = Textfield1.text()
        grade = Textfield2.text()
        #relation = float(grade) / float(credits)




        button = QPushButton('calculate',self)
        button.clicked.connect(self.on_click)

        flo = QFormLayout()
        flo.addRow("Credits",Textfield1)
        flo.addRow("Grade",Textfield2)
        flo.addRow(button)
        self.setLayout(flo)
    def on_click(self):

        print("这门课的学分和成绩之间的关系是 %s and %s")







if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Textfield()
    window.setWindowTitle('Start')
    window.resize(800,500)
    window.show()
    sys.exit(app.exec())