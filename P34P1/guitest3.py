import sys
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import SIGNAL, QMainWindow, QObject
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from _ctypes import alignment


class com(QObject):
    close_app = pyqtSignal()
    
    
class qw(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(qw, self).__init__(parent)
        self.statusBar().showMessage("OK")
        self.setWindowTitle(u"车牌")
        
        qb1 = QtGui.QPushButton(u"添加")
        qb2 = QtGui.QPushButton("b2")
        qb3 = QtGui.QPushButton("b3")
        qb1.clicked.connect(self.react)
        qb2.clicked.connect(self.react)
        qb3.clicked.connect(self.closedownd)
        
        btlayout = QHBoxLayout()
        btlayout.addStretch()
        btlayout.addWidget(qb1)
        btlayout.addWidget(qb2)
        
        ledt1 = QLineEdit()
        ledt2 = QLineEdit()
        qlb1 = QLabel(u"姓名")
        qlb2 = QLabel(u"车牌")
        
        glayout = QGridLayout()
        glayout.addWidget(qlb1, 0, 0)
        glayout.addWidget(ledt1, 0, 1)
        glayout.addWidget(qlb2, 1, 0)
        glayout.addWidget(ledt2, 1, 1)
        glayout.addLayout(btlayout, 2, 0, 1, 3)
        
        cwgt = QWidget()
        cwgt.setLayout(glayout)
        
        self.setCentralWidget(cwgt)
         
        
        self.c = com()
        self.c.close_app.connect(self.close)
        
    def keyPressEvent(self, event):
        print(event)
        if event.key() == Qt.Key_Escape:
            self.c.close_app.emit()
    
        
    def react(self):
        self.statusBar().showMessage(self.sender().text()+"was pressed")
    
    def closedownd(self):
        self.close()            

        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    q1 = qw()
    q1.show()
    app.exec_()  