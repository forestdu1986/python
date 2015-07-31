#!/usr/bin/env python
#coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import SIGNAL, QMainWindow, QObject
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from _ctypes import alignment
import shelve


class com(QObject):
    #new class com which contains a new signal close_app
    close_app = pyqtSignal()
    
    
class qw(QtGui.QDialog):
    def __init__(self, parent = None):
        super(qw, self).__init__(parent)
        self.setWindowTitle(u"车牌输入")
        #two buttons one to trigger add event, one to clear the two line editors
        qb1 = QtGui.QPushButton(u"添加")
        qb2 = QtGui.QPushButton(u"清空")
        qb1.clicked.connect(self.addtext)
        qb2.clicked.connect(self.cleartext)
        #button layout contains two buttons which will be added to a grid layout with label and line editor
        btlayout = QHBoxLayout()
        btlayout.addStretch()
        btlayout.addWidget(qb1)
        btlayout.addWidget(qb2)
        
        self.ledt1 = QLineEdit()
        self.ledt2 = QLineEdit()
        qlb1 = QLabel(u"姓名")
        qlb2 = QLabel(u"车牌")
        

        glayout = QGridLayout()
        glayout.addWidget(qlb1, 0, 0)
        glayout.addWidget(self.ledt1, 0, 1)
        glayout.addWidget(qlb2, 1, 0)
        glayout.addWidget(self.ledt2, 1, 1)
        glayout.addLayout(btlayout, 2, 0, 1, 3)
        

        self.setLayout(glayout)
        
         
        
        self.c = com()
        #relate new signal to main window close
        self.c.close_app.connect(self.close)
        
    def keyPressEvent(self, event):
        #rewrite key press event to emit new signal
        if event.key() == Qt.Key_Escape:
            self.c.close_app.emit()
    
        
    def addtext(self):
        s = shelve.open("test.dat")
        s[self.ledt1.text().strip()] = self.ledt2.text().strip()
        self.statusBar().showMessage(self.ledt1.text()+"was pressed")
        s.close()
    
    def closedownd(self):
        self.close()            

    def cleartext(self):
        self.ledt1.clear()
        self.ledt2.clear()    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    q1 = qw()
    q1.show()
    app.exec_()  