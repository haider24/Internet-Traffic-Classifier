from PyQt5 import QtWidgets, QtCore
from ui_mainwindow import Ui_MainWindow
from Dialog import DialogClass

class MainWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__();
        self.setupUi(self)

        self.capture.clicked.connect(self.captureButtonpressed)

        self.show()




    def captureButtonpressed(self):
        self.capture=DialogClass()

