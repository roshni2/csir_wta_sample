import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import pandas as pd
import os



class Page1(QDialog):
    def __init__(self):
        super(Page1, self).__init__()
        loadUi("homepage.ui", self)
        self.data_btn.clicked.connect(self.gotoSecondpage)
        self.dataca_btn.clicked.connect(self.gotothirdpage)
        self.test_btn.clicked.connect(self.gotofourthpage)

    def gotoSecondpage(self):
        page_2 = Page1()
        widget.addWidget(page_2)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotothirdpage(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotofourthpage(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentWidget(widget.currentWidget() + 1)


class Page2(QDialog):
    def __init__(self):
        super(Page2, self).__init__()
        loadUi("filepage2.ui", self)
        self.home_btn.clicked.connect(self.gotofirstpage)
        self.dataca_btn.clicked.connect(self.gotothirdpage)
        self.test_btn.clicked.connect(self.gotofourthpage)
        self.open.clicked.connect(self.openfile)

    def openfile(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open', os.getenv('HOME'), 'CSV(*.csv)')
            self.all_data = pd.read_csv(path[0])
        except:
            print(path)


    def gotofirstpage(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotothirdpage(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotofourthpage(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentWidget(widget.currentWidget() + 1)


class Page3(QDialog):
    def __init__(self):
        super(Page3, self).__init__()
        loadUi("3page.ui", self)
        self.data_btn.clicked.connect(self.gotoSecondpage)
        self.home_btn.clicked.connect(self.gototfirstpage)
        self.test_btn.clicked.connect(self.gotofourthpage)

    def gotoSecondpage(self):
        page_2 = Page2()
        widget.addWidget(page_2)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gototfirstpage(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotofourthpage(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentWidget(widget.currentWidget() + 1)


class Page4(QDialog):
    def __init__(self):
        super(Page4, self).__init__()
        loadUi("4page.ui", self)
        self.data_btn.clicked.connect(self.gotoSecondpage)
        self.dataca_btn.clicked.connect(self.gotothirdpage)
        self.home_btn.clicked.connect(self.gotofirstpage)

    def gotoSecondpage(self):
        page_2 = Page1()
        widget.addWidget(page_2)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotothirdpage(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentWidget(widget.currentWidget() + 1)

    def gotofirstpage(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentWidget(widget.currentWidget() + 1)


app = QApplication(sys.argv)
mainWindow = Page1()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(720)
widget.setFixedHeight(520)
widget.show()
app.exec_()