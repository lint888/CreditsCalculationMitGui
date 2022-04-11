from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credits Calculation")
        self.setFixedSize(QSize(500,800))
        button = QPushButton("press this button",self)
        button.setCheckable(True)
        self.label = QLabel()

        self.input = QLineEdit(self)
        self.input.setVisible(True)
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)



        button.clicked.connect(self.ButtonClicked)
        #button.clicked.connect(self.disabletheWindow) disable the whole window

    def ButtonClicked(self):
        print("clicked")
        #self.setWindowTitle("Window disabled")
    def disabletheWindow(self):
        self.setDisabled(True)









app = QApplication([])

window = MainWindow()
window.show()

app.exec()