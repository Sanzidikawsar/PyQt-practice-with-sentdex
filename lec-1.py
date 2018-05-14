import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.show()
window.setGeometry(50, 50, 700, 300)
window.setWindowTitle("First GUI App..")


sys.exit(app.exec_())