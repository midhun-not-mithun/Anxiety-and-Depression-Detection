from getresult import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPlainTextEdit, QLabel
import pandas as pd 
import speech_recognition as sr

sen = ''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Mental Health Detection using Social Media")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image:url(bg3.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 60, 211, 51))
        font = QtGui.QFont("Helvetica")
        font.setPointSize(12)
        font1 = QtGui.QFont("Courier New")
        font1.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("background-image:url(gradient-background.png);")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(340, 320, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color:rgb(255,153,255);")
        self.submit.setCheckable(False)
        self.submit.setObjectName("submit")
        self.QLabel = QtWidgets.QLabel(self.centralwidget)
        self.QLabel.setGeometry(QtCore.QRect(155, 400, 500, 500))
        self.QLabel.setStyleSheet("background-color:rgb(204, 204, 255);")
        self.QLabel.setObjectName("")
        #------
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(271, 200, 220, 90))
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet("background-color:rgb(204, 204, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submit.clicked.connect(self.onButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select an option"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Text"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Twitter_ID"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))

    def onButtonClicked(self):
        self.storeString(self.lineEdit.text())
        self.QLabel.setText(sen)
       
    
    x='' 
    def storeString(self, inString):
        global x
        global sen
        x = inString
        sen = backtogui(x)
        print(sen)
        print(inString)
        return sen

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dir_ = QtCore.QDir("Roboto")
    _id = QtGui.QFontDatabase.addApplicationFont("Roboto/Roboto-Regular.ttf")
    print(QtGui.QFontDatabase.applicationFontFamilies(_id))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())