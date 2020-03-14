# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from Service import *
from AddWindow import *
from RemoveWindow import Ui_Remove
from ModifyWin import Ui_Modifier
from add_spending_window import *
from ModifySpendingWin import Ui_ModifySpending


class Ui_MainWindow(object):
    def __init__(self, serv_cat, serv_chel):
        self.__serv_cat = serv_cat
        self.__serv_chel = serv_chel
        self.addwin = QtWidgets.QMainWindow()
        self.removewin = QtWidgets.QMainWindow()
        self.modifywin = QtWidgets.QMainWindow()
        self._translate = QtCore.QCoreApplication.translate
        self.add_spending_win = QtWidgets.QMainWindow()
        """
        Fac butonul de add spending sa ruleze cu restul aplicatiei. Eroare daca treci peste buget maxim. Afisaj instant in label budget
       """
    def add(self):
        self.adder = Ui_AddWindow(self.__serv_cat,self.__serv_chel, self.CategoryBox, self.LabelBudget, self.SpendingsTable, self.addwin)
        self.adder.setupUi(self.addwin)
        self.addwin.show()
    
    def remove(self):
        self.remover = Ui_Remove(self.__serv_cat,self.__serv_chel, self.CategoryBox, self.LabelBudget, self.SpendingsTable, self.removewin)
        self.remover.setupUi(self.removewin)
        self.removewin.show()
    
    def modify(self):
        self.modifier = Ui_Modifier(self.__serv_cat, self.CategoryBox,self.LabelBudget, self.modifywin)
        self.modifier.setupUi(self.modifywin)
        self.modifywin.show()
        self.LabelBudget.setText(self._translate("MainWindow", "Current Budget: " + "\n" + self.__serv_cat.situatie_generala()))
    
    def add_chel(self):
        self.adder = Ui_AddSpending(self.__serv_cat, self.__serv_chel,self.CategoryBox,self.LabelBudget, self.SpendingsTable, self.add_spending_win)
        self.adder.setupUi(self.add_spending_win)
        self.add_spending_win.show()
    
    def remove_chel(self):
        try:
            self.__serv_chel.sterge(int(self.SpendingsTable.currentRow())+1)
            self.SpendingsTable.clear()
            self.SpendingsTable.setRowCount(0)
            for chel in self.__serv_chel.get_all_chel():
                self.SpendingsTable.setRowCount( self.SpendingsTable.rowCount() + 1)
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
            self.LabelBudget.setText(QtCore.QCoreApplication.translate("MainWindow", "Current Budget: " + "\n" + self.__serv_cat.situatie_generala()))
            self.CategoryBox.clear()
            for cat in self.__serv_cat.get_all():
                self.CategoryBox.addItem(str(cat))
        except Exception as ex:
            win = QMessageBox()
            win.setWindowTitle("Error")
            win.setIcon(win.Warning)
            if self.SpendingsTable.currentRow() == -1:
                win.setText("Select a spending first by clicking on a row in the table.")
            else:
                win.setText("Invalid Category.")
            win.exec()
    
    def modify_chel(self):
        self.modifier = Ui_ModifySpending(self.__serv_cat, self.__serv_chel,self.CategoryBox,self.LabelBudget, self.SpendingsTable, self.add_spending_win)
        self.modifier.setupUi(self.add_spending_win)
        self.add_spending_win.show()
    
    
    def search_chel(self):
        self.SpendingsTable.clear()
        self.SpendingsTable.setRowCount(0)
        for chel in self.__serv_chel.get_all_chel():
            if self.SearchLine.text().lower() in chel.get_descriere().lower() or self.SearchLine.text().lower() in chel.get_categorie().lower():
                self.SpendingsTable.setRowCount( self.SpendingsTable.rowCount() + 1)
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
                self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
                
    def back_chel(self):
        self.SpendingsTable.clear()
        self.SpendingsTable.setRowCount(0)
        for chel in self.__serv_chel.get_all_chel():
            self.SpendingsTable.setRowCount( self.SpendingsTable.rowCount() + 1)
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1138, 863)
        MainWindow.setWindowIcon(QtGui.QIcon("cash-icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(240, 10, 601, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.Title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(40)
        self.Title.setFont(font)
        self.Title.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Title.setObjectName("Title")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1, 120, 1200, 1200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 211, 98, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CategoryBox = QtWidgets.QComboBox(self.frame)
        self.CategoryBox.setGeometry(QtCore.QRect(20, 30, 341, 41))
        self.CategoryBox.setMaxVisibleItems(20)
        self.CategoryBox.setObjectName("CategoryBox")
        for cat in self.__serv_cat.get_all():
            self.CategoryBox.addItem(str(cat))
            
            
        self.AddCatButton = QtWidgets.QPushButton(self.frame)
        self.AddCatButton.setGeometry(QtCore.QRect(380, 30, 131, 41))
        self.AddCatButton.setObjectName("AddCatButton")
        self.AddCatButton.clicked.connect(self.add)
        self.RemoveCatButton = QtWidgets.QPushButton(self.frame)
        self.RemoveCatButton.clicked.connect(self.remove)
        self.RemoveCatButton.setGeometry(QtCore.QRect(520, 30, 161, 41))
        self.RemoveCatButton.setObjectName("RemoveCatButton")
        self.ModifyCatButton = QtWidgets.QPushButton(self.frame)
        self.ModifyCatButton.setGeometry(QtCore.QRect(690, 30, 161, 41))
        self.ModifyCatButton.setObjectName("ModifyCatButton")
        self.ModifyCatButton.clicked.connect(self.modify)
        self.LabelCurrent = QtWidgets.QLabel(self.frame)
        self.LabelCurrent.setGeometry(QtCore.QRect(380, 80, 211, 31))
        self.LabelCurrent.setObjectName("LabelCurrent")
        self.SpendingsTable = QtWidgets.QTableWidget(self.frame)
        self.SpendingsTable.setGeometry(QtCore.QRect(20, 150, 511, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpendingsTable.sizePolicy().hasHeightForWidth())
        self.SpendingsTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(16)
        self.SpendingsTable.setFont(font)
        self.SpendingsTable.setFrameShape(QtWidgets.QFrame.Box)
        self.SpendingsTable.setAlternatingRowColors(False)
        self.SpendingsTable.setGridStyle(QtCore.Qt.DashDotLine)
        self.SpendingsTable.setColumnCount(3)
        self.SpendingsTable.setRowCount(0)
        self.SpendingsTable.setObjectName("SpendingsTable")
        self.SpendingsTable.clear()
        self.SpendingsTable.setHorizontalHeaderLabels("Sum;Category;Description".split(';'))
        for chel in self.__serv_chel.get_all_chel():
            self.SpendingsTable.setRowCount( self.SpendingsTable.rowCount() + 1)
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 0, QTableWidgetItem(str(chel.get_suma())))
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 1, QTableWidgetItem(chel.get_categorie()))
            self.SpendingsTable.setItem(self.SpendingsTable.rowCount() - 1, 2, QTableWidgetItem(chel.get_descriere()))
        
        self.SpendingsTable.setColumnWidth(0, 102)
        self.SpendingsTable.setColumnWidth(1, 200)
        self.SpendingsTable.setColumnWidth(2, 180)
        #self.SpendingsTable.resizeColumnsToContents()
        
        self.LabelBudget = QtWidgets.QLabel(self.frame)
        self.LabelBudget.setGeometry(QtCore.QRect(845, 10, 200, 200))
        
        
        self.LabelSpendings = QtWidgets.QLabel(self.frame)
        self.LabelSpendings.setGeometry(QtCore.QRect(20, 105, 141, 31))
        self.LabelSpendings.setObjectName("LabelSpendings")
        self.AddSpendingButton = QtWidgets.QPushButton(self.frame)
        self.AddSpendingButton.setGeometry(QtCore.QRect(540, 150, 111, 41))
        self.AddSpendingButton.setObjectName("AddSpendingButton")
        self.AddSpendingButton.clicked.connect(self.add_chel)
        self.RemoveSpendingButton = QtWidgets.QPushButton(self.frame)
        self.RemoveSpendingButton.setGeometry(QtCore.QRect(540, 200, 111, 41))
        self.RemoveSpendingButton.setObjectName("RemoveSpendingButton")
        self.RemoveSpendingButton.clicked.connect(self.remove_chel)
        self.ModifySpendingbutton = QtWidgets.QPushButton(self.frame)
        self.ModifySpendingbutton.setGeometry(QtCore.QRect(540, 250, 111, 41))
        self.ModifySpendingbutton.setObjectName("ModifySpendingbutton")
        self.ModifySpendingbutton.clicked.connect(self.modify_chel)
        self.SearchLabel = QtWidgets.QLabel(self.frame)
        self.SearchLabel.setGeometry(QtCore.QRect(540, 300, 261, 31))
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchLine = QtWidgets.QLineEdit(self.frame)
        self.SearchLine.setGeometry(QtCore.QRect(540, 350, 171, 41))
        self.SearchLine.setObjectName("SearchLine")
        self.SearchSpendingButton = QtWidgets.QPushButton(self.frame)
        self.SearchSpendingButton.setGeometry(QtCore.QRect(720, 347, 111, 51))
        self.SearchSpendingButton.setObjectName("SearchSpendingButton")
        self.SearchSpendingButton.clicked.connect(self.search_chel)
        
        
        self.BackSpendingButton = QtWidgets.QPushButton(self.frame)
        self.BackSpendingButton.setGeometry(QtCore.QRect(850, 347, 111, 51))
        self.BackSpendingButton.setObjectName("BackSpendingButton")
        self.BackSpendingButton.clicked.connect(self.back_chel)
        
        
        self.CloseButton = QtWidgets.QPushButton(self.frame)
        self.CloseButton.setGeometry(QtCore.QRect(430, 490, 121, 41))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.clicked.connect(sys.exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(self._translate("MainWindow", "Your Spendings App"))
        self.LabelBudget.setText(self._translate("MainWindow", "Current Budget: " + "\n" + self.__serv_cat.situatie_generala()))
        #self.LabelBudget.set
        
        self.Title.setText(self._translate("MainWindow", "Your Spendings App"))
        self.AddCatButton.setText(self._translate("MainWindow", "Add"))
        self.RemoveCatButton.setText(self._translate("MainWindow", "Remove"))
        self.ModifyCatButton.setText(self._translate("MainWindow", "Modify"))
        self.LabelCurrent.setText(self._translate("MainWindow", "Current situation:"))
        self.LabelSpendings.setText(self._translate("MainWindow", "Spendings:"))
        self.AddSpendingButton.setText(self._translate("MainWindow", "Add"))
        self.RemoveSpendingButton.setText(self._translate("MainWindow", "Remove"))
        self.ModifySpendingbutton.setText(self._translate("MainWindow", "Modify"))
        self.SearchLabel.setText(self._translate("MainWindow", "Search in description:"))
        self.SearchSpendingButton.setText(self._translate("MainWindow", "Search"))
        self.BackSpendingButton.setText(self._translate("MainWindow", "Back"))
        self.CloseButton.setText(self._translate("MainWindow", "Close"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    repoCat = RepoCategorie("categorii")
    valcat = ValidatorCategorie()
    serv_cat = ServiceCategorie(valcat, repoCat, "total")
    repoChel = RepoCheltuiala("cheltuieli")
    valchel = ValidatorCheltuiala()
    serv_chel = ServiceCheltuiala(valchel, repoCat, repoChel, "counter")
    ui = Ui_MainWindow(serv_cat, serv_chel)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
