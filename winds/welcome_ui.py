# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.setWindowModality(QtCore.Qt.NonModal)
        welcome.setEnabled(True)
        welcome.resize(1306, 906)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(welcome.sizePolicy().hasHeightForWidth())
        welcome.setSizePolicy(sizePolicy)
        welcome.setMinimumSize(QtCore.QSize(1306, 906))
        welcome.setMaximumSize(QtCore.QSize(1306, 906))
        welcome.setMouseTracking(True)
        welcome.setFocusPolicy(QtCore.Qt.StrongFocus)
        welcome.setToolTip("")
        welcome.setStyleSheet(" background-image: url(C:/Users/abdijavad110/Documents/UNI/97-98 1/Data Base/project/ui/welcome_background.jpg);\n"
" background-repeat: norepeat;")
        welcome.setAnimated(True)
        welcome.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setEnabled(True)
        self.loading.setGeometry(QtCore.QRect(-90, 615, 500, 500))
        self.loading.setMouseTracking(False)
        self.loading.setStyleSheet("background: transparent;")
        self.loading.setText("")
        movie = QtGui.QMovie("ui/loading.gif")
        self.loading.setMovie(movie)
        movie.start()
        self.loading.setScaledContents(True)
        self.loading.setObjectName("req_car_eco")
        welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "welcome"))

