# Form implementation generated from reading ui file 'C:\Users\Admin\mypythoncode\K24406H\chuong1_ham\baitap21\ui\MainWindow21.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 506)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 371, 71))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 120, 301, 111))
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(18, 31, 47, 14))
        self.label_2.setObjectName("label_2")
        self.lineEditN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditN.setGeometry(QtCore.QRect(70, 30, 191, 21))
        self.lineEditN.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEditN.setObjectName("lineEditN")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(18, 61, 47, 14))
        self.label_3.setObjectName("label_3")
        self.lineEditK = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditK.setGeometry(QtCore.QRect(70, 60, 191, 21))
        self.lineEditK.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEditK.setObjectName("lineEditK")
        self.pushButtonThucHien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonThucHien.setGeometry(QtCore.QRect(210, 240, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Admin\\mypythoncode\\K24406H\\chuong1_ham\\baitap21\\ui\\../images/15720_exec_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThucHien.setIcon(icon)
        self.pushButtonThucHien.setObjectName("pushButtonThucHien")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 300, 301, 101))
        self.groupBox_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 47, 14))
        self.label_5.setObjectName("label_5")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditA.setGeometry(QtCore.QRect(90, 30, 161, 21))
        self.lineEditA.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditC.setGeometry(QtCore.QRect(90, 60, 161, 21))
        self.lineEditC.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.lineEditC.setObjectName("lineEditC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trần Ái Quyên - Bài 21"))
        self.label.setText(_translate("MainWindow", "Chỉnh hợp - Tổ hợp"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập N và K:"))
        self.label_2.setText(_translate("MainWindow", "Nhập N:"))
        self.label_3.setText(_translate("MainWindow", "Nhập K:"))
        self.pushButtonThucHien.setText(_translate("MainWindow", "Thực hiện"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả:"))
        self.label_4.setText(_translate("MainWindow", "Chỉnh hợp A:"))
        self.label_5.setText(_translate("MainWindow", "Tổ hợp C:"))
