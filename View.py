from Controller import *
from calendar import week
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class View(QMainWindow):
    def __init__(self,) -> None:
        QMainWindow.__init__(self)
        self.initMenu()
        self.set_week()
    def set_week(self):
        self.table = QTableWidget(5,3)
        self.setCentralWidget(self.table)
        self.setGeometry(50,50,700,400)
        self.show()

    def initMenu(self):
        actions = self.menuBar()
        fileMenu = actions.addMenu("Settings")
        fileMenu = actions.addMenu("Settings")

app = QApplication()
mygui = View()
app.exec_()

    

