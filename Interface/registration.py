from PyQt5 import QtCore, QtGui, QtWidgets


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)


class Ui_RegistrationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Registration")
        MainWindow.resize(290, 439)
        MainWindow.setMinimumSize(QtCore.QSize(290, 439))
        MainWindow.setMaximumSize(QtCore.QSize(290, 439))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_registration = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registration.setGeometry(QtCore.QRect(80, 140, 121, 23))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_registration.sizePolicy().hasHeightForWidth())

        self.btn_registration.setSizePolicy(sizePolicy)
        self.btn_registration.setObjectName("btn_registration")

        self.line_edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_password.setGeometry(QtCore.QRect(70, 110, 150, 20))
        self.line_edit_password.setObjectName("line_edit_password")

        self.line_edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_login.setGeometry(QtCore.QRect(70, 80, 150, 20))
        self.line_edit_login.setObjectName("line_edit_login")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 170, 81, 21))
        self.label.setObjectName("label")




        self.label_2 = ClickableLabel(self.centralwidget)
        color_label_2 = self.label_2.palette()
        color_label_2.setColor(QtGui.QPalette.WindowText, QtGui.QColor("blue"))
        self.label_2.setGeometry(QtCore.QRect(160, 170, 47, 21))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setObjectName("label_2")
        self.label_2.setPalette(color_label_2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(205, 170, 16, 21))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.btn_registration.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.line_edit_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.line_edit_login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.label.setText(_translate("MainWindow", "У вас уже есть "))
        self.label_2.setText(_translate("MainWindow", "аккаунт"))
        self.label_3.setText(_translate("MainWindow", "?"))

