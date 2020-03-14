# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoveWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Service import *
from PyQt5.Qt import QMessageBox

class Ui_Remove(object):
    def __init__(self, serv, serv_chel, combo, label, table, win):
        self.serv = serv
        self.serv_chel = serv_chel
        self.combo = combo
        self.motherlabel = label
        self.table = table
        self.win = win
        
    def remove(self):
        try:
            self.serv.sterge(self.comboBox.currentText())
            self.combo.clear()
            for cat in self.serv.get_all():
                self.combo.addItem(str(cat))
            self.motherlabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Current Budget: " + "\n" + self.serv.situatie_generala()))
            self.table.clear()
            self.table.setRowCount(0)
            for chel in self.serv_chel.get_all_chel():
                self.table.setRowCount( self.table.rowCount() + 1)
                self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
                self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
                self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
            self.win.close()
        except Exception as ex:
            print(ex)
            win = QMessageBox()
            win.setIcon(win.Warning)
            win.setText("Invalid Category.")
            win.exec()
            
    def setupUi(self, Remove):
        Remove.setObjectName("Remove")
        Remove.resize(800, 133)
        self.centralwidget = QtWidgets.QWidget(Remove)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 751, 221))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 291, 41))
        self.comboBox.setObjectName("comboBox")
        
        
        for cat in self.serv.get_all():
            self.comboBox.addItem(cat.get_nume())
            
            
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(522, 20, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.remove)
        Remove.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Remove)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Remove.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Remove)
        self.statusbar.setObjectName("statusbar")
        Remove.setStatusBar(self.statusbar)

        self.retranslateUi(Remove)
        QtCore.QMetaObject.connectSlotsByName(Remove)

    def retranslateUi(self, Remove):
        _translate = QtCore.QCoreApplication.translate
        Remove.setWindowTitle(_translate("Remove", "Remove"))
        self.label.setText(_translate("Remove", "Category to remove:"))
        self.pushButton.setText(_translate("Remove", "Remove"))


