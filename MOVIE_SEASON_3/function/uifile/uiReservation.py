# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservation.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reservationWindow(object):
    def setupUi(self, reservationWindow):
        reservationWindow.setObjectName("reservationWindow")
        reservationWindow.resize(1200, 800)
        reservationWindow.setMinimumSize(QtCore.QSize(1200, 800))
        reservationWindow.setMaximumSize(QtCore.QSize(1200, 800))
        reservationWindow.setStyleSheet("QFrame#frame_2{ background-color: rgb(231, 231, 231)}\n"
"QLabel#label_12{ background-color: rgb(255, 255, 255)}\n"
"QMainWindow{ background-color: rgb(255, 255, 255)}\n"
"QLabel#label_total_count{ color: rgb(255, 0, 0)}\n"
"QLabel#label_movie_name{ font-size:16pt; }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(reservationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_movie = QtWidgets.QListWidget(self.centralwidget)
        self.list_movie.setGeometry(QtCore.QRect(10, 10, 331, 371))
        self.list_movie.setObjectName("list_movie")
        self.frame_seats = QtWidgets.QFrame(self.centralwidget)
        self.frame_seats.setGeometry(QtCore.QRect(360, 140, 361, 301))
        self.frame_seats.setStyleSheet("")
        self.frame_seats.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_seats.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seats.setObjectName("frame_seats")
        self.layoutWidget = QtWidgets.QWidget(self.frame_seats)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 231, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setSpacing(35)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(self.frame_seats)
        self.frame.setGeometry(QtCore.QRect(60, 70, 271, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.screen = QtWidgets.QLabel(self.frame)
        self.screen.setGeometry(QtCore.QRect(0, 0, 270, 21))
        self.screen.setStyleSheet("QLabel#screen { background-color: rgb(213, 213, 213) }")
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName("screen")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(8, 25, 261, 181))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 241, 178))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layout_group_seats = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.layout_group_seats.setSpacing(6)
        self.layout_group_seats.setObjectName("layout_group_seats")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbox_A1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_A1.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_A1.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_A1.setObjectName("cbox_A1")
        self.horizontalLayout.addWidget(self.cbox_A1)
        self.cbox_A2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_A2.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_A2.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_A2.setTristate(False)
        self.cbox_A2.setObjectName("cbox_A2")
        self.horizontalLayout.addWidget(self.cbox_A2)
        self.cbox_A3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_A3.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_A3.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_A3.setObjectName("cbox_A3")
        self.horizontalLayout.addWidget(self.cbox_A3)
        self.cbox_A4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_A4.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_A4.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_A4.setObjectName("cbox_A4")
        self.horizontalLayout.addWidget(self.cbox_A4)
        self.cbox_A5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_A5.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_A5.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_A5.setObjectName("cbox_A5")
        self.horizontalLayout.addWidget(self.cbox_A5)
        self.layout_group_seats.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbox_B1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_B1.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_B1.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_B1.setObjectName("cbox_B1")
        self.horizontalLayout_2.addWidget(self.cbox_B1)
        self.cbox_B2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_B2.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_B2.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_B2.setObjectName("cbox_B2")
        self.horizontalLayout_2.addWidget(self.cbox_B2)
        self.cbox_B3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_B3.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_B3.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_B3.setObjectName("cbox_B3")
        self.horizontalLayout_2.addWidget(self.cbox_B3)
        self.cbox_B4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_B4.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_B4.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_B4.setObjectName("cbox_B4")
        self.horizontalLayout_2.addWidget(self.cbox_B4)
        self.cbox_B5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_B5.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_B5.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_B5.setObjectName("cbox_B5")
        self.horizontalLayout_2.addWidget(self.cbox_B5)
        self.layout_group_seats.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbox_C1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_C1.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_C1.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_C1.setObjectName("cbox_C1")
        self.horizontalLayout_3.addWidget(self.cbox_C1)
        self.cbox_C2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_C2.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_C2.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_C2.setObjectName("cbox_C2")
        self.horizontalLayout_3.addWidget(self.cbox_C2)
        self.cbox_C3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_C3.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_C3.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_C3.setObjectName("cbox_C3")
        self.horizontalLayout_3.addWidget(self.cbox_C3)
        self.cbox_C4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_C4.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_C4.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_C4.setObjectName("cbox_C4")
        self.horizontalLayout_3.addWidget(self.cbox_C4)
        self.cbox_C5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_C5.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_C5.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_C5.setObjectName("cbox_C5")
        self.horizontalLayout_3.addWidget(self.cbox_C5)
        self.layout_group_seats.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbox_D1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_D1.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_D1.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_D1.setObjectName("cbox_D1")
        self.horizontalLayout_4.addWidget(self.cbox_D1)
        self.cbox_D2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_D2.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_D2.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_D2.setObjectName("cbox_D2")
        self.horizontalLayout_4.addWidget(self.cbox_D2)
        self.cbox_D3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_D3.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_D3.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_D3.setObjectName("cbox_D3")
        self.horizontalLayout_4.addWidget(self.cbox_D3)
        self.cbox_D4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_D4.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_D4.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_D4.setObjectName("cbox_D4")
        self.horizontalLayout_4.addWidget(self.cbox_D4)
        self.cbox_D5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_D5.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_D5.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_D5.setObjectName("cbox_D5")
        self.horizontalLayout_4.addWidget(self.cbox_D5)
        self.layout_group_seats.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbox_E1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_E1.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_E1.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_E1.setObjectName("cbox_E1")
        self.horizontalLayout_5.addWidget(self.cbox_E1)
        self.cbox_E2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_E2.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_E2.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_E2.setObjectName("cbox_E2")
        self.horizontalLayout_5.addWidget(self.cbox_E2)
        self.cbox_E3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_E3.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_E3.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_E3.setObjectName("cbox_E3")
        self.horizontalLayout_5.addWidget(self.cbox_E3)
        self.cbox_E4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_E4.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_E4.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_E4.setObjectName("cbox_E4")
        self.horizontalLayout_5.addWidget(self.cbox_E4)
        self.cbox_E5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbox_E5.setMinimumSize(QtCore.QSize(21, 21))
        self.cbox_E5.setMaximumSize(QtCore.QSize(21, 21))
        self.cbox_E5.setObjectName("cbox_E5")
        self.horizontalLayout_5.addWidget(self.cbox_E5)
        self.layout_group_seats.addLayout(self.horizontalLayout_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_seats)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 98, 41, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.frame_seats)
        self.label_12.setGeometry(QtCore.QRect(100, 270, 181, 21))
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.label_12.raise_()
        self.frame_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_info.setGeometry(QtCore.QRect(360, 460, 831, 301))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_info)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 230, 811, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.label_17 = QtWidgets.QLabel(self.frame_info)
        self.label_17.setGeometry(QtCore.QRect(30, 20, 371, 20))
        self.label_17.setObjectName("label_17")
        self.label_seats = QtWidgets.QLabel(self.frame_info)
        self.label_seats.setGeometry(QtCore.QRect(130, 90, 681, 16))
        self.label_seats.setObjectName("label_seats")
        self.label_movie_name = QtWidgets.QLabel(self.frame_info)
        self.label_movie_name.setGeometry(QtCore.QRect(40, 49, 201, 31))
        self.label_movie_name.setObjectName("label_movie_name")
        self.label_20 = QtWidgets.QLabel(self.frame_info)
        self.label_20.setGeometry(QtCore.QRect(40, 160, 61, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_info)
        self.label_21.setGeometry(QtCore.QRect(130, 130, 51, 21))
        self.label_21.setObjectName("label_21")
        self.label_discount = QtWidgets.QLabel(self.frame_info)
        self.label_discount.setGeometry(QtCore.QRect(490, 130, 70, 20))
        self.label_discount.setObjectName("label_discount")
        self.label_total_money = QtWidgets.QLabel(self.frame_info)
        self.label_total_money.setGeometry(QtCore.QRect(670, 130, 70, 20))
        self.label_total_money.setObjectName("label_total_money")
        self.label_22 = QtWidgets.QLabel(self.frame_info)
        self.label_22.setGeometry(QtCore.QRect(40, 90, 131, 20))
        self.label_22.setObjectName("label_22")
        self.label_time = QtWidgets.QLabel(self.frame_info)
        self.label_time.setGeometry(QtCore.QRect(240, 50, 70, 31))
        self.label_time.setObjectName("label_time")
        self.label_18 = QtWidgets.QLabel(self.frame_info)
        self.label_18.setGeometry(QtCore.QRect(130, 160, 70, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_info)
        self.label_19.setGeometry(QtCore.QRect(130, 190, 70, 20))
        self.label_19.setObjectName("label_19")
        self.label_24 = QtWidgets.QLabel(self.frame_info)
        self.label_24.setGeometry(QtCore.QRect(209, 125, 20, 91))
        self.label_24.setObjectName("label_24")
        self.label_adult_count = QtWidgets.QLabel(self.frame_info)
        self.label_adult_count.setGeometry(QtCore.QRect(245, 130, 31, 20))
        self.label_adult_count.setObjectName("label_adult_count")
        self.label_teenager_count = QtWidgets.QLabel(self.frame_info)
        self.label_teenager_count.setGeometry(QtCore.QRect(245, 160, 31, 20))
        self.label_teenager_count.setObjectName("label_teenager_count")
        self.label_child_count = QtWidgets.QLabel(self.frame_info)
        self.label_child_count.setGeometry(QtCore.QRect(245, 190, 31, 20))
        self.label_child_count.setObjectName("label_child_count")
        self.label_28 = QtWidgets.QLabel(self.frame_info)
        self.label_28.setGeometry(QtCore.QRect(289, 124, 20, 91))
        self.label_28.setObjectName("label_28")
        self.label_m_adult = QtWidgets.QLabel(self.frame_info)
        self.label_m_adult.setGeometry(QtCore.QRect(320, 130, 81, 20))
        self.label_m_adult.setObjectName("label_m_adult")
        self.label_m_teenager = QtWidgets.QLabel(self.frame_info)
        self.label_m_teenager.setGeometry(QtCore.QRect(320, 160, 81, 20))
        self.label_m_teenager.setObjectName("label_m_teenager")
        self.label_m_child = QtWidgets.QLabel(self.frame_info)
        self.label_m_child.setGeometry(QtCore.QRect(320, 190, 81, 20))
        self.label_m_child.setObjectName("label_m_child")
        self.frame_count = QtWidgets.QFrame(self.centralwidget)
        self.frame_count.setGeometry(QtCore.QRect(360, 10, 831, 111))
        self.frame_count.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_count.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_count.setObjectName("frame_count")
        self.label_16 = QtWidgets.QLabel(self.frame_count)
        self.label_16.setGeometry(QtCore.QRect(37, 6, 581, 51))
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.layoutWidget4 = QtWidgets.QWidget(self.frame_count)
        self.layoutWidget4.setGeometry(QtCore.QRect(40, 50, 561, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.sbox_adult = QtWidgets.QSpinBox(self.layoutWidget4)
        self.sbox_adult.setMinimumSize(QtCore.QSize(83, 28))
        self.sbox_adult.setAlignment(QtCore.Qt.AlignCenter)
        self.sbox_adult.setReadOnly(False)
        self.sbox_adult.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sbox_adult.setMaximum(9)
        self.sbox_adult.setObjectName("sbox_adult")
        self.horizontalLayout_10.addWidget(self.sbox_adult)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.sbox_teenager = QtWidgets.QSpinBox(self.layoutWidget4)
        self.sbox_teenager.setMinimumSize(QtCore.QSize(83, 28))
        self.sbox_teenager.setAlignment(QtCore.Qt.AlignCenter)
        self.sbox_teenager.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sbox_teenager.setMaximum(9)
        self.sbox_teenager.setObjectName("sbox_teenager")
        self.horizontalLayout_9.addWidget(self.sbox_teenager)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.sbox_child = QtWidgets.QSpinBox(self.layoutWidget4)
        self.sbox_child.setMinimumSize(QtCore.QSize(83, 28))
        self.sbox_child.setAlignment(QtCore.Qt.AlignCenter)
        self.sbox_child.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sbox_child.setMaximum(9)
        self.sbox_child.setObjectName("sbox_child")
        self.horizontalLayout_8.addWidget(self.sbox_child)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)
        self.layoutWidget5 = QtWidgets.QWidget(self.frame_count)
        self.layoutWidget5.setGeometry(QtCore.QRect(660, 20, 101, 71))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_total_count = QtWidgets.QLabel(self.layoutWidget5)
        self.label_total_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_count.setObjectName("label_total_count")
        self.verticalLayout_3.addWidget(self.label_total_count)
        self.frame_time = QtWidgets.QFrame(self.centralwidget)
        self.frame_time.setGeometry(QtCore.QRect(10, 400, 331, 361))
        self.frame_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_time.setObjectName("frame_time")
        self.list_time = QtWidgets.QListWidget(self.frame_time)
        self.list_time.setGeometry(QtCore.QRect(0, 0, 331, 361))
        self.list_time.setStyleSheet("")
        self.list_time.setObjectName("list_time")
        self.frame_movie = QtWidgets.QFrame(self.centralwidget)
        self.frame_movie.setGeometry(QtCore.QRect(740, 140, 451, 301))
        self.frame_movie.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_movie.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_movie.setObjectName("frame_movie")
        self.label_movieposter = QtWidgets.QLabel(self.frame_movie)
        self.label_movieposter.setGeometry(QtCore.QRect(0, 0, 211, 301))
        self.label_movieposter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_movieposter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_movieposter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_movieposter.setObjectName("label_movieposter")
        self.label_info = QtWidgets.QLabel(self.frame_movie)
        self.label_info.setGeometry(QtCore.QRect(220, 0, 231, 301))
        self.label_info.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.frame_info.raise_()
        self.frame_seats.raise_()
        self.list_movie.raise_()
        self.frame_count.raise_()
        self.frame_time.raise_()
        self.frame_movie.raise_()
        reservationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(reservationWindow)
        self.statusbar.setObjectName("statusbar")
        reservationWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(reservationWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 31))
        self.menuBar.setObjectName("menuBar")
        reservationWindow.setMenuBar(self.menuBar)

        self.retranslateUi(reservationWindow)
        self.pushButton.clicked.connect(self.list_movie.clearSelection)
        self.pushButton.clicked.connect(self.label_movieposter.clear)
        self.pushButton.clicked.connect(self.label_info.clear)
        self.sbox_adult.valueChanged['int'].connect(reservationWindow.total_is)
        self.sbox_teenager.valueChanged['int'].connect(reservationWindow.total_is)
        self.sbox_child.valueChanged['int'].connect(reservationWindow.total_is)
        self.pushButton.clicked.connect(reservationWindow.btn_re_action)
        self.list_movie.clicked['QModelIndex'].connect(reservationWindow.list_movie_action)
        self.sbox_adult.valueChanged['int'].connect(self.label_adult_count.setNum)
        self.sbox_teenager.valueChanged['int'].connect(self.label_teenager_count.setNum)
        self.sbox_child.valueChanged['int'].connect(self.label_child_count.setNum)
        self.cbox_A4.clicked.connect(reservationWindow.select_seats)
        self.cbox_A5.clicked.connect(reservationWindow.select_seats)
        self.cbox_A3.clicked.connect(reservationWindow.select_seats)
        self.cbox_A1.clicked.connect(reservationWindow.select_seats)
        self.cbox_A2.clicked.connect(reservationWindow.select_seats)
        self.cbox_B1.clicked.connect(reservationWindow.select_seats)
        self.cbox_B2.clicked.connect(reservationWindow.select_seats)
        self.cbox_B3.clicked.connect(reservationWindow.select_seats)
        self.cbox_B4.clicked.connect(reservationWindow.select_seats)
        self.cbox_B5.clicked.connect(reservationWindow.select_seats)
        self.cbox_C1.clicked.connect(reservationWindow.select_seats)
        self.cbox_C2.clicked.connect(reservationWindow.select_seats)
        self.cbox_C3.clicked.connect(reservationWindow.select_seats)
        self.cbox_C4.clicked.connect(reservationWindow.select_seats)
        self.cbox_C5.clicked.connect(reservationWindow.select_seats)
        self.cbox_D1.clicked.connect(reservationWindow.select_seats)
        self.cbox_D2.clicked.connect(reservationWindow.select_seats)
        self.cbox_D3.clicked.connect(reservationWindow.select_seats)
        self.cbox_D4.clicked.connect(reservationWindow.select_seats)
        self.cbox_D5.clicked.connect(reservationWindow.select_seats)
        self.cbox_E1.clicked.connect(reservationWindow.select_seats)
        self.cbox_E2.clicked.connect(reservationWindow.select_seats)
        self.cbox_E3.clicked.connect(reservationWindow.select_seats)
        self.cbox_E4.clicked.connect(reservationWindow.select_seats)
        self.cbox_E5.clicked.connect(reservationWindow.select_seats)
        self.pushButton_3.clicked.connect(reservationWindow.btn_ok_action)
        self.pushButton.clicked.connect(self.label_seats.clear)
        self.pushButton_2.clicked.connect(reservationWindow.btn_exit_action)
        self.list_time.clicked['QModelIndex'].connect(reservationWindow.list_time_action)
        QtCore.QMetaObject.connectSlotsByName(reservationWindow)

    def retranslateUi(self, reservationWindow):
        _translate = QtCore.QCoreApplication.translate
        reservationWindow.setWindowTitle(_translate("reservationWindow", "MainWindow"))
        self.label_2.setText(_translate("reservationWindow", "1"))
        self.label_3.setText(_translate("reservationWindow", "2"))
        self.label_4.setText(_translate("reservationWindow", "3"))
        self.label_5.setText(_translate("reservationWindow", "4"))
        self.label_6.setText(_translate("reservationWindow", "5"))
        self.screen.setText(_translate("reservationWindow", "SCREEN"))
        self.cbox_A1.setText(_translate("reservationWindow", "A1"))
        self.cbox_A2.setText(_translate("reservationWindow", "A2"))
        self.cbox_A3.setText(_translate("reservationWindow", "A3"))
        self.cbox_A4.setText(_translate("reservationWindow", "A4"))
        self.cbox_A5.setText(_translate("reservationWindow", "A5"))
        self.cbox_B1.setText(_translate("reservationWindow", "B1"))
        self.cbox_B2.setText(_translate("reservationWindow", "B2"))
        self.cbox_B3.setText(_translate("reservationWindow", "B3"))
        self.cbox_B4.setText(_translate("reservationWindow", "B4"))
        self.cbox_B5.setText(_translate("reservationWindow", "B5"))
        self.cbox_C1.setText(_translate("reservationWindow", "C1"))
        self.cbox_C2.setText(_translate("reservationWindow", "C2"))
        self.cbox_C3.setText(_translate("reservationWindow", "C3"))
        self.cbox_C4.setText(_translate("reservationWindow", "C4"))
        self.cbox_C5.setText(_translate("reservationWindow", "C5"))
        self.cbox_D1.setText(_translate("reservationWindow", "D1"))
        self.cbox_D2.setText(_translate("reservationWindow", "D2"))
        self.cbox_D3.setText(_translate("reservationWindow", "D3"))
        self.cbox_D4.setText(_translate("reservationWindow", "D4"))
        self.cbox_D5.setText(_translate("reservationWindow", "D5"))
        self.cbox_E1.setText(_translate("reservationWindow", "E1"))
        self.cbox_E2.setText(_translate("reservationWindow", "E2"))
        self.cbox_E3.setText(_translate("reservationWindow", "E3"))
        self.cbox_E4.setText(_translate("reservationWindow", "E4"))
        self.cbox_E5.setText(_translate("reservationWindow", "E5"))
        self.label_8.setText(_translate("reservationWindow", "A"))
        self.label_11.setText(_translate("reservationWindow", "B"))
        self.label_7.setText(_translate("reservationWindow", "C"))
        self.label_9.setText(_translate("reservationWindow", "D"))
        self.label_10.setText(_translate("reservationWindow", "E"))
        self.label_12.setText(_translate("reservationWindow", "<html><head/><body><p>Plz, <span style=\" color:#5500ff;\">Choice</span> your seats</p></body></html>"))
        self.pushButton.setText(_translate("reservationWindow", "RE"))
        self.pushButton_3.setText(_translate("reservationWindow", "OK"))
        self.pushButton_2.setText(_translate("reservationWindow", "EXIT"))
        self.label_17.setText(_translate("reservationWindow", "<html><head/><body><p>This is your<span style=\" color:#ff0051;\"> payment </span>information. <span style=\" color:#ff0051;\">Plz check again</span>.</p></body></html>"))
        self.label_seats.setText(_translate("reservationWindow", "print seats"))
        self.label_movie_name.setText(_translate("reservationWindow", "MOVIE NAME"))
        self.label_20.setText(_translate("reservationWindow", "Total"))
        self.label_21.setText(_translate("reservationWindow", "adult"))
        self.label_discount.setText(_translate("reservationWindow", "discount"))
        self.label_total_money.setText(_translate("reservationWindow", "total"))
        self.label_22.setText(_translate("reservationWindow", "Seats"))
        self.label_time.setText(_translate("reservationWindow", "Time"))
        self.label_18.setText(_translate("reservationWindow", "teenager"))
        self.label_19.setText(_translate("reservationWindow", "child"))
        self.label_24.setText(_translate("reservationWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">x</span></p><p><span style=\" font-size:10pt;\">x</span></p><p><span style=\" font-size:10pt;\">x</span></p></body></html>"))
        self.label_adult_count.setText(_translate("reservationWindow", "co"))
        self.label_teenager_count.setText(_translate("reservationWindow", "co"))
        self.label_child_count.setText(_translate("reservationWindow", "co"))
        self.label_28.setText(_translate("reservationWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">=</span></p><p><span style=\" font-size:10pt;\">=</span></p><p><span style=\" font-size:10pt;\">=</span></p></body></html>"))
        self.label_m_adult.setText(_translate("reservationWindow", "money"))
        self.label_m_teenager.setText(_translate("reservationWindow", "money"))
        self.label_m_child.setText(_translate("reservationWindow", "money"))
        self.label_16.setText(_translate("reservationWindow", "<html><head/><body><p>Plz,<span style=\" color:#5500ff;\"> Select</span> a person to view. You can choice conunt that between 0 to 10.</p></body></html>"))
        self.label.setText(_translate("reservationWindow", "Adult"))
        self.sbox_adult.setSpecialValueText(_translate("reservationWindow", "0"))
        self.label_13.setText(_translate("reservationWindow", "Teenager"))
        self.label_14.setText(_translate("reservationWindow", "Child"))
        self.label_15.setText(_translate("reservationWindow", "Total is"))
        self.label_total_count.setText(_translate("reservationWindow", "0"))
        self.label_movieposter.setText(_translate("reservationWindow", "Movie Poster"))
        self.label_info.setText(_translate("reservationWindow", "Movie info"))

