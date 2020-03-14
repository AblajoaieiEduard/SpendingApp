# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_AddWindow(object):
    def __init__(self, serv, serv_chel, combo, label, table, win):
        self.serv = serv
        self.serv_chel = serv_chel
        self.combo = combo
        self.motherlabel = label
        self.table = table
        self.win = win
        
    def add(self):
        try:
            self.serv.adauga(self.lineEdit.text(), int(self.spinBox.value()))
            
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
        
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(800, 130)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 821, 221))
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
        self.label.setGeometry(QtCore.QRect(10, 25, 161, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(170, 30, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(500, 31, 121, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 81, 31))
        self.label_2.setObjectName("label_2")
        self.AddButton = QtWidgets.QPushButton(self.frame)
        self.AddButton.setGeometry(QtCore.QRect(630, 27, 93, 41))
        self.AddButton.setObjectName("AddButton")
        self.AddButton.clicked.connect(self.add)
        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AddWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "AddWindow"))
        self.label.setText(_translate("AddWindow", "Category name: "))
        self.label_2.setText(_translate("AddWindow", "Budget:"))
        self.AddButton.setText(_translate("AddWindow", "Add"))

