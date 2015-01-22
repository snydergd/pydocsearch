#!/usr/bin/python2

import sys
from PyQt4.QtGui import QApplication, QMainWindow
from mainWindow import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
