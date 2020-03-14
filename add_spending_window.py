# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_spending_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from click._compat import WIN
from PyQt5.Qt import QMessageBox

from PyQt5.QtWidgets import QTableWidgetItem

class Ui_AddSpending(object):
    def __init__(self, serv_cat, serv_chel,combo, label,table, win):
        self.serv_cat = serv_cat
        self.serv_chel = serv_chel
        self.combo = combo
        self.budget = label
        self.table = table
        self.win = win
        
    
    def add(self):
        try:
            self.serv_chel.adauga(self.doubleSpinBox.value(), self.comboBox.currentText(),self.textEdit.toPlainText())
            self.combo.clear()
            for cat in self.serv_cat.get_all():
                self.combo.addItem(str(cat))
            self.table.clear()
            self.table.setRowCount(0)
            for chel in self.serv_chel.get_all_chel():
                self.table.setRowCount( self.table.rowCount() + 1)
                self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
                self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
                self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
                self.budget.setText(QtCore.QCoreApplication.translate("MainWindow", "Current Budget: " + "\n" + self.serv_cat.situatie_generala()))

            self.win.close()
        except Exception as ex:
            win = QMessageBox()
            win.setIcon(win.Warning)
            win.setText(str(ex))
            win.exec()
            
    def setupUi(self, AddSpending):
        AddSpending.setObjectName("AddSpending")
        AddSpending.resize(911, 379)
        self.centralwidget = QtWidgets.QWidget(AddSpending)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 881, 401))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
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
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(90, 40, 131, 31))
        self.doubleSpinBox.setMaximum(1001.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 111, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(340, 41, 221, 41))
        self.comboBox.setObjectName("comboBox")
        for cat in self.serv_cat.get_all():
            self.comboBox.addItem(cat.get_nume())
            
            
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 861, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(670, 37, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)
        AddSpending.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddSpending)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 26))
        self.menubar.setObjectName("menubar")
        AddSpending.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddSpending)
        self.statusbar.setObjectName("statusbar")
        AddSpending.setStatusBar(self.statusbar)

        self.retranslateUi(AddSpending)
        QtCore.QMetaObject.connectSlotsByName(AddSpending)

    def retranslateUi(self, AddSpending):
        _translate = QtCore.QCoreApplication.translate
        AddSpending.setWindowTitle(_translate("AddSpending", "Add spending"))
        self.label.setText(_translate("AddSpending", "Budget:"))
        self.label_2.setText(_translate("AddSpending", "Category:"))
        self.label_3.setText(_translate("AddSpending", "Description:"))
        self.pushButton.setText(_translate("AddSpending", "Add"))

