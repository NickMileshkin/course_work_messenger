from PyQt5 import QtCore, QtGui, QtWidgets


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)


class Ui_AuthorizationWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 439)
        Dialog.setMinimumSize(QtCore.QSize(290, 439))
        Dialog.setMaximumSize(QtCore.QSize(290, 439))

        self.btn_authorization = QtWidgets.QPushButton(Dialog)
        self.btn_authorization.setGeometry(QtCore.QRect(85, 140, 121, 23))
        self.btn_authorization.setObjectName("btn_registration")

        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 111, 150, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.lineEdit_login = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_login.setGeometry(QtCore.QRect(70, 80, 150, 20))
        self.lineEdit_login.setObjectName("lineEdit_login")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 170, 81, 21))
        self.label.setObjectName("label")

        self.label_2 = ClickableLabel(Dialog)
        color_label_2 = self.label_2.palette()
        color_label_2.setColor(QtGui.QPalette.WindowText, QtGui.QColor("blue"))
        self.label_2.setGeometry(QtCore.QRect(155, 170, 47, 21))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setObjectName("label_2")
        self.label_2.setPalette(color_label_2)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(205, 170, 16, 21))
        self.label_3.setObjectName("label_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.btn_authorization.setText(_translate("Dialog", "Войти в аккаунт"))
        self.btn_authorization.setText(_translate("Dialog", "Войти в аккаунт"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.lineEdit_login.setPlaceholderText(_translate("Dialog", "Логин"))
        self.label.setText(_translate("Dialog", "У вас ещё нет "))
        self.label_2.setText(_translate("Dialog", "аккаунта"))
        self.label_3.setText(_translate("Dialog", "?"))