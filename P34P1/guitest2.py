#!/usr/bin/python
# messagebox.py 
import sys 
from PyQt4 import QtGui, QtCore

class MessageBox(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
             

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(250, 150)
        self.setWindowTitle('statusbar')
        self.statusBar().showMessage("ready")
        
app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show() 
sys.exit(app.exec_())
