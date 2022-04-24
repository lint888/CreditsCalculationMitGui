from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Credits Calculation")
        self.resize(500,600)
        self.createMenu()

        #create the label for credits input and the input area
        self.Creditslabel = QLabel(self)
        self.Creditslabel.setText("Credits")
        self.Creditslabel.move(100,50)
        self.inputCredits = QLineEdit(self)

        self.inputCredits.move(200,50)
        #create the label for grade input
        self.gradelabel = QLabel(self)
        self.gradelabel.setText("Grade")
        self.gradelabel.move(100,100)
        self.inputgrade = QLineEdit(self)
        self.inputgrade.move(200,100)

        self.equationLabel = QLabel(self)
        self.equationLabel.setText("equation")
        self.equationLabel.move(200,200)




        self.Resultlabel = QLabel(self)
        self.Resultlabel.setText("Result")
        self.Resultlabel.move(200,400)
        #self.Resultlabel.setText(self.input.text())


        button = QPushButton("calculate", self)

        button.clicked.connect(self.ButtonCalculateClicked)



    def createMenu(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        # File menu
        fileMenu = QMenu(" &File", self)
        menuBar.addMenu(fileMenu)
        # Open Recent submenu
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        self.readFiles = fileMenu.addMenu("read files")
        self.readImages = fileMenu.addMenu("Read Images")
        # Separator
        fileMenu.addSeparator()

        editMenu = menuBar.addMenu(" &Edit")
        menuBar.addMenu(editMenu)


    def ButtonCalculateClicked(self):
        self.equationLabel.setText(self.inputgrade.text() + "/" + self.inputCredits.text())
        ans = eval(self.equationLabel.text())

        self.Resultlabel.setText(str(ans))











if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())