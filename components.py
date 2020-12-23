import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui
import os.path
from os import path
from PyQt5.QtWidgets import QWidget
from analysis import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setStyleSheet('QScrollBar::add-line:horizontal {border: none;background: none;}QScrollBar::sub-line:horizontal { border: none;background: none;}')
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        content.setStyleSheet('color:white;font-family:OpenSans-Regular; background-image: url(./images/blank.png)')
        lay = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setStyleSheet('color:white;font-family:OpenSans-Regular; background-image: url(./images/blank.png)')
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)

def Spinner(self):
    self.spinner.setHidden(False)
    self.spinner.show()

def CreateSpinner(self):
    self.spinner = QtWidgets.QLabel(self)
    self.spinner.setGeometry(QtCore.QRect(750, 275, 200, 200))
    self.spinner.setMinimumSize(QtCore.QSize(70, 70))
    self.spinner.setMaximumSize(QtCore.QSize(70, 70))
    self.spinner.setObjectName("label")
    self.movie = QMovie("./images/doubleSpinner.gif")
    self.spinner.setMovie(self.movie)
    self.movie.start()
    self.spinner.setHidden(True)

def CreateCover(self):
    self.coverButton = QtWidgets.QLabel(self)
    self.coverButton.setStyleSheet('background-image: url(./images/block.png);')
    self.coverButton.move(500, 275)
    self.coverButton.setMinimumSize(QtCore.QSize(500, 250))
    self.coverButton.setMaximumSize(QtCore.QSize(500, 250))
    self.coverButton.setHidden(True)

def hideCover(self):
    self.coverButton.setHidden(False)

def hideSpinner(self):
    self.spinner.setHidden(True)
    self.coverButton.setHidden(True)


def createText(self):
    self.label2 = QtWidgets.QLabel("A", self)
    self.label2.setGeometry(QtCore.QRect(190, 100, 200, 200))
    self.label2.setStyleSheet('color:red;font-size: 25px;')

def generateText(self, complexity, maintainability, fullText):
    self.setStyleSheet("background-repeat:no-repeat;background-image: url(./images/page2.png)")
    hideSpinner(self)
    print("write text")
    self.labelTwo = QtWidgets.QLabel(self)
    self.labelTwo.setText(complexity[1])
    self.labelTwo.move(175,150)
    self.labelTwo.setMinimumSize(QtCore.QSize(100, 110))
    self.labelTwo.setStyleSheet('color:#00e091;font-family:LeagueSpartan-Bold;font-size: 80px; background-image: url(./images/blank.png)')
    self.labelTwo.show()

    self.labelThree = QtWidgets.QLabel(self)
    self.labelThree.setText(maintainability[1])
    self.labelThree.move(175,275)
    self.labelThree.setMinimumSize(QtCore.QSize(100, 110))
    self.labelThree.setStyleSheet('color:#00e091;font-family:LeagueSpartan-Bold;font-size: 80px; background-image: url(./images/blank.png)')
    self.labelThree.show()

    self.labelFour = QtWidgets.QLabel(self)
    self.labelFour.setText('- ' + str(round(complexity[0], 2)))
    self.labelFour.move(250,165)
    self.labelFour.setMinimumSize(QtCore.QSize(100, 110))
    self.labelFour.setStyleSheet('color:white;font-family:LeagueSpartan-Bold;font-size: 24px; background-image: url(./images/blank.png)')
    self.labelFour.show()

    self.labelFive = QtWidgets.QLabel(self)
    self.labelFive.setText('- ' + str(round(maintainability[0], 2)))
    self.labelFive.move(250,290)
    self.labelFive.setMinimumSize(QtCore.QSize(100, 110))
    self.labelFive.setStyleSheet('color:white;font-family:LeagueSpartan-Bold;font-size: 24px; background-image: url(./images/blank.png)')
    self.labelFive.show()


    self.fileName = QtWidgets.QLabel(self)
    self.fileName.setText("sample.py")
    self.fileName.move(170,60)
    self.fileName.setMinimumSize(QtCore.QSize(400, 110))
    self.fileName.setStyleSheet('color:white;font-family:LeagueSpartan-Bold;font-size: 25px; background-image: url(./images/blank.png)')
    self.fileName.show()

    self.textArea = ScrollLabel(self)
    self.textArea.setText(fullText)
    self.textArea.setGeometry(510, 100, 461, 301)
    self.textArea.setStyleSheet('color:white;font-family:OpenSans-Regular;font-size: 12px; background-image: url(./images/blank.png)')
    self.textArea.show()

    self.buttonBack = QPushButton(self)
    self.buttonBack.setGeometry(QtCore.QRect(20, 530, 61, 61))
    self.buttonBack.setStyleSheet('background: rgba(76, 175, 80, 0.0)')
    self.buttonBack.clicked.connect(self.goToPageOne)
    self.buttonBack.show()

def page1(self):
    self.fileName.hide()
    self.textArea.hide()
    self.labelFive.hide()
    self.labelFour.hide()
    self.labelThree.hide()
    self.labelTwo.hide()
    self.setStyleSheet("background-repeat:no-repeat;background-image: url(./images/page1.png)")

def runAnalysis(name):
    with open(name, 'r') as file:
        cc = cyclomaticComplexity(file.read())
        mi = maintainabilityIndex(file.read())
        results = run_pylint(name)
    return cc, mi, results
