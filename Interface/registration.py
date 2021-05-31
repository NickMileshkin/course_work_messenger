from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 439)
        Dialog.setMinimumSize(QtCore.QSize(290, 439))
        Dialog.setMaximumSize(QtCore.QSize(290, 439))

        self.btn_registration = QtWidgets.QPushButton(Dialog)
        self.btn_registration.setGeometry(QtCore.QRect(85, 140, 121, 23))
        self.btn_registration.setObjectName("btn_registration")

        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 111, 150, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_login = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_login.setGeometry(QtCore.QRect(70, 80, 150, 20))
        self.lineEdit_login.setObjectName("lineEdit_login")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация"))
        self.btn_registration.setText(_translate("Dialog", "Зарегистрироваться"))
        self.btn_registration.setText(_translate("Dialog", "Зарегистрироваться"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.lineEdit_login.setPlaceholderText(_translate("Dialog", "Логин"))

