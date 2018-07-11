from PyQt5 import QtWidgets, QtCore
import subprocess
from ui_dialog import Ui_Dialog
from PacketDetailsWindow import PacketDetailsWindowClass

class DialogClass(QtWidgets.QMainWindow, Ui_Dialog):

    pro=None
    time=None

    def __init__(self):
        super().__init__();
        self.setupUi(self)

        self.stop.clicked.connect(self.stopButtonpressed)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setStyleSheet("background:white")
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_event)
        self.setFixedSize(self.size())
        self.timer.start(1000)

        global time_elapsed
        time_elapsed = 0

        global pro
        pro = subprocess.Popen(['tcpdump', '-i', 'any', '-w', 'test.pcap'], shell=False)

        self.show()

    def update_event(self):

        global time_elapsed

        time_elapsed += 1

        if time_elapsed is 1:
            self.time.setText("%d" % time_elapsed)
        else:
            self.time.setText("%d" % time_elapsed)




    def stopButtonpressed(self):

        global pro
        pro.terminate()
        self.stop = PacketDetailsWindowClass()
        self.close()




