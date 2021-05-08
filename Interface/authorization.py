from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 439)
        MainWindow.setMinimumSize(QtCore.QSize(290, 439))
        MainWindow.setMaximumSize(QtCore.QSize(290, 439))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_authorization = QtWidgets.QPushButton(self.centralwidget)
        self.btn_authorization.setGeometry(QtCore.QRect(80, 140, 121, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_authorization.sizePolicy().hasHeightForWidth())
        self.btn_authorization.setSizePolicy(sizePolicy)
        self.btn_authorization.setObjectName("btn_authorization")
        self.line_edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_password.setGeometry(QtCore.QRect(70, 110, 150, 20))
        self.line_edit_password.setObjectName("line_edit_password")
        self.line_edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_login.setGeometry(QtCore.QRect(70, 80, 150, 20))
        self.line_edit_login.setText("")
        self.line_edit_login.setObjectName("line_edit_login")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.btn_authorization.setText(_translate("MainWindow", "Войти"))
        self.line_edit_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.line_edit_login.setPlaceholderText(_translate("MainWindow", "Логин"))

