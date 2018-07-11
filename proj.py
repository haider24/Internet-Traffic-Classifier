import sys
from PyQt5.QtWidgets import QApplication

from MainWIndow import MainWindowClass


app = QApplication(sys.argv)

window = MainWindowClass()

sys.exit(app.exec_())
