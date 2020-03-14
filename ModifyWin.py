# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from Service import *
from PyQt5.Qt import QMessageBox

class Ui_Modifier(object):
    def __init__(self, serv, combo,label, win):
        self.serv = serv
        self.combo = combo
        self.motherlabel = label
        self.win = win
    
    def modify(self):
        try:
            self.serv.modifica(self.comboBox.currentText(), self.spinBox.value())
            self.combo.clear()
            for cat in self.serv.get_all():
                self.combo.addItem(str(cat))
            self.motherlabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Current Budget: " + "\n" + self.serv.situatie_generala()))
            self.win.close()
        except Exception as ex:
            print(ex)
            msg = PyQt5.Qt.QMessageBox()
            msg.setIcon(msg.Warning)
            msg.setText("Invalid Category")
            msg.exec()
        
    def setupUi(self, Modifier):
        Modifier.setObjectName("Modifier")
        Modifier.resize(643, 218)
        self.centralwidget = QtWidgets.QWidget(Modifier)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 10, 761, 281))
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(130, 51, 241, 31))
        self.comboBox.setObjectName("comboBox")
        
        
        for cat in self.serv.get_all():
            self.comboBox.addItem(cat.get_nume())
            
            
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(380, 50, 131, 31))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(520, 50, 121, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(270, 100, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.modify)
        Modifier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Modifier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 26))
        self.menubar.setObjectName("menubar")
        Modifier.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Modifier)
        self.statusbar.setObjectName("statusbar")
        Modifier.setStatusBar(self.statusbar)

        self.retranslateUi(Modifier)
        QtCore.QMetaObject.connectSlotsByName(Modifier)

    def retranslateUi(self, Modifier):
        _translate = QtCore.QCoreApplication.translate
        Modifier.setWindowTitle(_translate("Modifier", "Modify"))
        self.label.setText(_translate("Modifier", "Category:"))
        self.label_2.setText(_translate("Modifier", "New Budget:"))
        self.pushButton.setText(_translate("Modifier", "Modify"))

