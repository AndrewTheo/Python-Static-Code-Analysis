import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QScrollArea, QVBoxLayout, QGroupBox, QLabel
from PyQt5 import uic
from PyQt5 import QtGui
import os.path
from os import path
from PyQt5.QtWidgets import QWidget
from analysis import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from components import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./ui/mainwindow.ui", self)
        self.statusbar.setHidden(True)
        self.selectFile.clicked.connect(self.SelectFile)
        self.createUI(self)

    def createUI(self, args):
        CreateCover(self)
        CreateSpinner(self)

    def createUI2(self, args):
        hideCover(self)
        hideSpinner(self)

    def goToPageOne(self, args):
        page1(self)

    def SelectFile(self):
        print("Button pressed")
        fname, _ = QFileDialog.getOpenFileName()
        print(fname)
        if(path.exists(fname) != True):
            print("Path does not exist.")
        if(fname.lower().endswith('.py') != True):
            print("Not a python file")
        hideCover(self)
        Spinner(self)
        complexity, maintainability, codeResults = runAnalysis(fname)

        QtGui.QFontDatabase.addApplicationFont('./images/LeagueSpartan-Bold.otf')
        QtGui.QFontDatabase.addApplicationFont('./images/OpenSans-Regular.tff')
        generateText(self, complexity, maintainability, codeResults)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
