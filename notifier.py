import sys
import os
import math

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt


#todo : create all widget as seperate modules which can be tweaked (size, color, shape)

class CloseCrosss(QtGui.QFrame):
    clicked = QtCore.pyqtSignal()

    def __init__(self, QWidgetparent=None):
        QtGui.QFrame.__init__(self, parent=QWidgetparent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.color = Qt.darkBlue
        self.QWidgetparent = QWidgetparent
        if QWidgetparent:
            size = self.parent().size()
            width = size.width()
            height = size.height()
            self.move(width - 30, 0)
            QWidgetparent.installEventFilter(self)
            self.setMouseTracking(True)
        self.clicked.connect(self.x_close)

    def enterEvent(self, event):
        self.changecolor(Qt.yellow)

    def leaveEvent(self, event):
        self.changecolor(Qt.darkBlue)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()
        QtGui.QFrame.mouseReleaseEvent(self, event)

    def x_close(self):
        self.close()
        self.parent().close()

    def changecolor(self, color):
        self.color = QtGui.QColor(color)
        self.update()

    def paintEvent(self, e):
        pen = QtGui.QPen(self.color, 1.5)
        qp = QtGui.QPainter(self)
        qp.setPen(pen)
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 255, 255))
        qp.setBrush(brush)
        qp.drawEllipse(5, 5, 20, 20)
        qp.drawLine(10, 10, 20, 20)
        qp.drawLine(20, 10, 10, 20)


class Notifier(QtGui.QWidget):
    def __init__(self, message=None, height=0):
        QtGui.QWidget.__init__(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        _desktop = QtGui.QApplication.desktop()
        size = _desktop.screenGeometry()
        self.resize_w = size.width() * 25 / 100
        self.resize_h = size.height() * 3 / 100

        self.move_w = size.width() - (size.width() * 25 / 100) - 1
        self.move_h = 50 + height
        self.resize(self.resize_w, self.resize_h+20)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.main_layout = QtGui.QVBoxLayout()
        self.move(self.move_w, self.move_h)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.label = QtGui.QLabel(message)
        self.label.setStyleSheet("color: lightgreen; font: 14px;")
        self.label.setIndent(20)
        self.main_layout.addWidget(self.label)
        self.setLayout(self.main_layout)

    def paintEvent(self, event):
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(QtGui.QColor(255, 255, 255, 200))
        qp.setBrush(QtGui.QColor(0, 0, 0, 200))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 5, 5)
        qp.end()


if __name__ == "__main__":
    QApp = QtGui.QApplication(sys.argv)
    # for i in range(10):
    window = Notifier("Hello times", height=100)
    cross = CloseCrosss(QWidgetparent=window)
    window.show()
    cross.show()
    QApp.exec_()
