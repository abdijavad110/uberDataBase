# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'on_trip.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
aaa = None
from winds.passenger_main_ui import Ui_mainWidow

class Ui_trip_window(object):
    def setupUi(self, trip_window):
        aaa = trip_window
        # on_trip
        trip_window.setObjectName("on trip")
        trip_window.setWindowModality(QtCore.Qt.NonModal)
        trip_window.setEnabled(True)
        trip_window.resize(1306, 906)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(trip_window.sizePolicy().hasHeightForWidth())
        trip_window.setSizePolicy(sizePolicy)
        trip_window.setMinimumSize(QtCore.QSize(1306, 906))
        trip_window.setMaximumSize(QtCore.QSize(1306, 906))
        trip_window.setMouseTracking(True)
        trip_window.setFocusPolicy(QtCore.Qt.StrongFocus)
        trip_window.setToolTip("")
        trip_window.setStyleSheet(" background-image: url(C:/Users/abdijavad110/Documents/UNI/97-98 1/Data Base/project/ui/welcome_background.jpg);\n"
" background-repeat: norepeat;")
        trip_window.setAnimated(True)
        trip_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(trip_window)
        self.centralwidget.setObjectName("centralwidget")
        # profile pic
        self.profie_pic = QtWidgets.QLabel(self.centralwidget)
        self.profie_pic.setEnabled(True)
        self.profie_pic.setGeometry(QtCore.QRect(90, 50, 200, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profie_pic.sizePolicy().hasHeightForWidth())
        self.profie_pic.setSizePolicy(sizePolicy)
        self.profie_pic.setMaximumSize(QtCore.QSize(200, 200))
        self.profie_pic.setStyleSheet("background: transparent;")
        self.profie_pic.setText("")
        self.profie_pic.setPixmap(QtGui.QPixmap("ui/driver.png"))
        self.profie_pic.setScaledContents(True)
        self.profie_pic.setObjectName("profie_pic")
        # driver name
        self.drv_name = QtWidgets.QLabel(self.centralwidget)
        self.drv_name.setEnabled(True)
        self.drv_name.setGeometry(QtCore.QRect(60, 290, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drv_name.setFont(font)
        self.drv_name.setMouseTracking(False)
        self.drv_name.setStyleSheet("background: transparent;")
        self.drv_name.setScaledContents(True)
        self.drv_name.setObjectName("drv_name")
        # car ico
        self.car_ico = QtWidgets.QLabel(self.centralwidget)
        self.car_ico.setEnabled(True)
        self.car_ico.setGeometry(QtCore.QRect(1000, 60, 231, 211))
        self.car_ico.setStyleSheet("background: transparent;")
        self.car_ico.setText("")
        self.car_ico.setPixmap(QtGui.QPixmap("ui/car.png"))
        self.car_ico.setScaledContents(True)
        self.car_ico.setObjectName("car_ico")
        # wallet pay
        self.wallet_pay = QtWidgets.QPushButton(self.centralwidget)
        self.wallet_pay.setGeometry(QtCore.QRect(70, 750, 120, 120))
        self.wallet_pay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wallet_pay.setAutoFillBackground(False)
        self.wallet_pay.setStyleSheet("background:transparent;")
        self.wallet_pay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/wallet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wallet_pay.setIcon(icon)
        self.wallet_pay.setIconSize(QtCore.QSize(85, 85))
        self.wallet_pay.setAutoRepeat(False)
        self.wallet_pay.setObjectName("wallet_pay")
        # cancel
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(1080, 750, 111, 111))
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel.setAutoFillBackground(False)
        self.cancel.setStyleSheet("background:transparent;")
        self.cancel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon1)
        self.cancel.setIconSize(QtCore.QSize(100, 100))
        self.cancel.setAutoRepeat(False)
        self.cancel.setObjectName("cancel")
        # diver number
        self.drv_number = QtWidgets.QLabel(self.centralwidget)
        self.drv_number.setEnabled(True)
        self.drv_number.setGeometry(QtCore.QRect(60, 360, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drv_number.setFont(font)
        self.drv_number.setMouseTracking(False)
        self.drv_number.setStyleSheet("background: transparent;")
        self.drv_number.setScaledContents(True)
        self.drv_number.setObjectName("drv_number")
        # licence
        self.license = QtWidgets.QLabel(self.centralwidget)
        self.license.setEnabled(True)
        self.license.setGeometry(QtCore.QRect(920, 270, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.license.setFont(font)
        self.license.setMouseTracking(False)
        self.license.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.license.setStyleSheet("background: transparent;")
        self.license.setScaledContents(True)
        self.license.setAlignment(QtCore.Qt.AlignCenter)
        self.license.setObjectName("liscence")
        # car type
        self.car_type = QtWidgets.QLabel(self.centralwidget)
        self.car_type.setEnabled(True)
        self.car_type.setGeometry(QtCore.QRect(920, 340, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.car_type.setFont(font)
        self.car_type.setMouseTracking(False)
        self.car_type.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.car_type.setStyleSheet("background: transparent;")
        self.car_type.setScaledContents(True)
        self.car_type.setAlignment(QtCore.Qt.AlignCenter)
        self.car_type.setObjectName("car_type")
        # pay cash
        self.cash_pay = QtWidgets.QPushButton(self.centralwidget)
        self.cash_pay.setGeometry(QtCore.QRect(190, 750, 120, 120))
        self.cash_pay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cash_pay.setAutoFillBackground(False)
        self.cash_pay.setStyleSheet("background:transparent;")
        self.cash_pay.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/cash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cash_pay.setIcon(icon2)
        self.cash_pay.setIconSize(QtCore.QSize(150, 150))
        self.cash_pay.setAutoRepeat(False)
        self.cash_pay.setObjectName("cash_pay")
        # cost label
        self.cost_lbl = QtWidgets.QLabel(self.centralwidget)
        self.cost_lbl.setEnabled(True)
        self.cost_lbl.setGeometry(QtCore.QRect(520, 760, 121, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cost_lbl.setFont(font)
        self.cost_lbl.setMouseTracking(False)
        self.cost_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cost_lbl.setStyleSheet("background: transparent; color:rgb(100, 0, 100)")
        self.cost_lbl.setScaledContents(True)
        self.cost_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cost_lbl.setObjectName("cost_lbl")
        # balance label
        self.balance_lbl = QtWidgets.QLabel(self.centralwidget)
        self.balance_lbl.setEnabled(True)
        self.balance_lbl.setGeometry(QtCore.QRect(480, 820, 161, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.balance_lbl.setFont(font)
        self.balance_lbl.setMouseTracking(False)
        self.balance_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.balance_lbl.setStyleSheet("background: transparent; color:rgb(100, 0, 100)")
        self.balance_lbl.setScaledContents(True)
        self.balance_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.balance_lbl.setObjectName("balance_lbl")
        # balance
        self.balance = QtWidgets.QLabel(self.centralwidget)
        self.balance.setEnabled(True)
        self.balance.setGeometry(QtCore.QRect(670, 820, 291, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.balance.setFont(font)
        self.balance.setMouseTracking(False)
        self.balance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.balance.setStyleSheet("background: transparent; color:rgb(100, 0, 100)")
        self.balance.setScaledContents(True)
        self.balance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.balance.setObjectName("balance")
        # cost
        self.cost = QtWidgets.QLabel(self.centralwidget)
        self.cost.setEnabled(True)
        self.cost.setGeometry(QtCore.QRect(670, 760, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cost.setFont(font)
        self.cost.setMouseTracking(False)
        self.cost.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cost.setStyleSheet("background: transparent; color:rgb(100, 0, 100)")
        self.cost.setScaledContents(True)
        self.cost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cost.setObjectName("cost")
        # increase balance
        self.increase_balance = QtWidgets.QPushButton(self.centralwidget)
        self.increase_balance.setGeometry(QtCore.QRect(590, 440, 120, 120))
        self.increase_balance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.increase_balance.setAutoFillBackground(False)
        self.increase_balance.setStyleSheet("background:transparent;")
        self.increase_balance.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.increase_balance.setIcon(icon3)
        self.increase_balance.setIconSize(QtCore.QSize(90, 90))
        self.increase_balance.setAutoRepeat(False)
        self.increase_balance.hide()
        self.increase_balance.setObjectName("increase_balance")
        # empty wallet ico
        self.empty_wallet_ico = QtWidgets.QLabel(self.centralwidget)
        self.empty_wallet_ico.setEnabled(True)
        self.empty_wallet_ico.setGeometry(QtCore.QRect(600, 160, 121, 121))
        self.empty_wallet_ico.setStyleSheet("background: transparent;")
        self.empty_wallet_ico.setText("")
        self.empty_wallet_ico.setPixmap(QtGui.QPixmap("ui/empty.png"))
        self.empty_wallet_ico.setScaledContents(True)
        self.empty_wallet_ico.setObjectName("empty_wallet_ico")
        self.empty_wallet_ico.hide()
        # blur_bg
        self.blur_bg = QtWidgets.QLabel(self.centralwidget)
        self.blur_bg.setGeometry(QtCore.QRect(0, 0, 1311, 911))
        self.blur_bg.setStyleSheet("background: rgba(200, 200, 200, 200);")
        self.blur_bg.setText("")
        self.blur_bg.setObjectName("blur_bg")
        self.blur_bg.hide()
        # increase value
        self.increase_value = QtWidgets.QLineEdit(self.centralwidget)
        self.increase_value.setGeometry(QtCore.QRect(450, 350, 411, 58))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.increase_value.setFont(font)
        self.increase_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.increase_value.setStyleSheet("background: transparent;\n"
"mouse-over-background-color: yellow;")
        self.increase_value.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.increase_value.setText("")
        self.increase_value.setObjectName("increase_value")
        self.increase_value.hide()
        # why cancel label
        self.why_cancel = QtWidgets.QLabel(self.centralwidget)
        self.why_cancel.setEnabled(True)
        self.why_cancel.setGeometry(QtCore.QRect(320, 170, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.why_cancel.setFont(font)
        self.why_cancel.setMouseTracking(False)
        self.why_cancel.setStyleSheet("background: transparent;")
        self.why_cancel.setScaledContents(True)
        self.why_cancel.setObjectName("why_cancel")
        self.why_cancel.hide()
        # cancel reasons
        self.cancel_reason_1 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_reason_1.setGeometry(QtCore.QRect(370, 260, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel_reason_1.setFont(font)
        self.cancel_reason_1.setStyleSheet("background: rgba(255, 255, 255, 70)")
        self.cancel_reason_1.setObjectName("cancel_reason_1")
        self.cancel_reason_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_reason_2.setGeometry(QtCore.QRect(370, 340, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel_reason_2.setFont(font)
        self.cancel_reason_2.setStyleSheet("background: rgba(255, 255, 255, 70)")
        self.cancel_reason_2.setObjectName("cancel_reason_2")
        self.cancel_reason_3 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_reason_3.setGeometry(QtCore.QRect(370, 420, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel_reason_3.setFont(font)
        self.cancel_reason_3.setStyleSheet("background: rgba(255, 255, 255, 70)")
        self.cancel_reason_3.setObjectName("cancel_reason_3")
        self.cancel_reason_1.hide()
        self.cancel_reason_2.hide()
        self.cancel_reason_3.hide()
        # back_btn
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(1000, 800, 91, 91))
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setAutoFillBackground(False)
        self.back_btn.setStyleSheet("background:transparent;")
        self.back_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon2)
        self.back_btn.setIconSize(QtCore.QSize(90, 90))
        self.back_btn.setAutoRepeat(False)
        self.back_btn.hide()
        self.back_btn.setObjectName("back_btn")
        # raises
        self.drv_name.raise_()
        self.car_ico.raise_()
        self.profie_pic.raise_()
        self.wallet_pay.raise_()
        self.cancel.raise_()
        self.drv_number.raise_()
        self.license.raise_()
        self.car_type.raise_()
        self.cash_pay.raise_()
        self.cost_lbl.raise_()
        self.balance_lbl.raise_()
        self.balance.raise_()
        self.cost.raise_()
        self.blur_bg.raise_()
        self.empty_wallet_ico.raise_()
        self.increase_balance.raise_()
        self.increase_value.raise_()
        self.why_cancel.raise_()
        self.cancel_reason_1.raise_()
        self.cancel_reason_3.raise_()
        self.cancel_reason_2.raise_()
        self.back_btn.raise_()
        trip_window.setCentralWidget(self.centralwidget)

        # connections
        self.cancel.clicked.connect(self.cancel_clicked)
        self.cash_pay.clicked.connect(self.cash_pay_clicked)
        self.wallet_pay.clicked.connect(self.wallet_pay_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        self.cancel_reason_1.clicked.connect(trip_window.change_ui_to_main_window)
        self.cancel_reason_2.clicked.connect(trip_window.change_ui_to_main_window)
        self.cancel_reason_3.clicked.connect(trip_window.change_ui_to_main_window)
        self.increase_balance.clicked.connect(self.increase_balance_clicked)

        self.retranslateUi(trip_window)
        QtCore.QMetaObject.connectSlotsByName(trip_window)

    def retranslateUi(self, mainWidow):
        _translate = QtCore.QCoreApplication.translate
        mainWidow.setWindowTitle(_translate("mainWidow", "mainWindow"))
        self.drv_name.setText(_translate("mainWidow", "fname lname"))
        self.drv_number.setText(_translate("mainWidow", "+989123456789"))
        self.license.setText(_translate("mainWidow", "12 a 345 | 66"))
        self.car_type.setText(_translate("mainWidow", "peugeot 206"))
        self.cost_lbl.setText(_translate("mainWidow", "cost:"))
        self.balance_lbl.setText(_translate("mainWidow", "balance:"))
        self.balance.setText(_translate("mainWidow", "99.00"))
        self.cost.setText(_translate("mainWidow", "100.00"))
        self.increase_value.setPlaceholderText(_translate("mainWidow", "how much ?"))
        self.why_cancel.setText(_translate("mainWidow", "Why ?"))
        self.cancel_reason_1.setText(_translate("mainWidow", "car wrecked"))
        self.cancel_reason_2.setText(_translate("mainWidow", "driver didnt come"))
        self.cancel_reason_3.setText(_translate("mainWidow", "driver bad behavior"))

    def wallet_pay_clicked(self):
        # todo: inja baiad hesab check she va az balance kam she
        if float(self.cost.text()) > float(self.balance.text()):
            self.empty_wallet_ico.show()
            self.blur_bg.show()
            self.increase_value.show()
            self.increase_balance.show()
        self.cash_pay.setStyleSheet("background: transparent")
        self.wallet_pay.setStyleSheet("background: rgba(200, 200, 200, 100)")

    def cash_pay_clicked(self):
        # todo: age az hesab kam shode bood baiad ezafe she
        self.cash_pay.setStyleSheet("background: rgba(200, 200, 200, 100)")
        self.wallet_pay.setStyleSheet("background: transparent")

    def increase_balance_clicked(self):
        inc = 0
        try:
            inc = float(self.balance.text()) + float(self.increase_value.text())
            if float(self.cost.text()) < float(self.balance.text()):
                self.empty_wallet_ico.hide()
                self.blur_bg.hide()
                self.increase_value.hide()
                self.increase_balance.hide()
        except:
            inc = float(self.balance.text())
        finally:
            self.balance.setText(str(int(inc*100)/100))
        # todo: pool too DB ham ezafe she

    def cancel_clicked(self):
        self.blur_bg.show()
        self.why_cancel.show()
        self.cancel_reason_1.show()
        self.cancel_reason_2.show()
        self.cancel_reason_3.show()
        self.back_btn.show()

    def back_btn_clicked(self):
        self.back_btn.hide()
        self.blur_bg.hide()
        self.why_cancel.hide()
        self.cancel_reason_1.hide()
        self.cancel_reason_2.hide()
        self.cancel_reason_3.hide()


