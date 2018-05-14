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
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)

        self.show()

    def close_application(self):
        print("Hello World!")
        self.setWindowTitle("Seriously!")

        # sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()