import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 600, 300)
        self.setWindowTitle("Second lecture practice")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100, 50)
        btn.move(100, 100)

        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()