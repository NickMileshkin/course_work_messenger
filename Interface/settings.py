from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 590)
        Dialog.setMinimumSize(QtCore.QSize(409, 590))
        Dialog.setMaximumSize(QtCore.QSize(409, 590))

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 411, 591))
        self.tabWidget.setObjectName("tabWidget")

        self.account_setting = QtWidgets.QWidget()
        self.account_setting.setObjectName("tab")
        self.lineEdit_new_login = QtWidgets.QLineEdit(self.account_setting)
        self.lineEdit_new_login.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.lineEdit_new_login.setObjectName("lineEdit")

        self.lineEdit_user_password_login = QtWidgets.QLineEdit(self.account_setting)
        self.lineEdit_user_password_login.setGeometry(QtCore.QRect(140, 40, 131, 20))
        self.lineEdit_user_password_login.setObjectName("lineEdit_2")

        self.btn_new_login = QtWidgets.QPushButton(self.account_setting)
        self.btn_new_login.setGeometry(QtCore.QRect(280, 40, 101, 20))
        self.btn_new_login.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.account_setting)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.account_setting)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_old_user_password = QtWidgets.QLineEdit(self.account_setting)
        self.lineEdit_old_user_password.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.lineEdit_old_user_password.setObjectName("lineEdit_3")

        self.lineEdit_new_user_password_1 = QtWidgets.QLineEdit(self.account_setting)
        self.lineEdit_new_user_password_1.setGeometry(QtCore.QRect(140, 100, 131, 20))
        self.lineEdit_new_user_password_1.setObjectName("lineEdit_4")

        self.lineEdit_new_user_password_2 = QtWidgets.QLineEdit(self.account_setting)
        self.lineEdit_new_user_password_2.setGeometry(QtCore.QRect(140, 130, 131, 20))
        self.lineEdit_new_user_password_2.setObjectName("lineEdit_5")

        self.btn_new_password = QtWidgets.QPushButton(self.account_setting)
        self.btn_new_password.setGeometry(QtCore.QRect(280, 110, 101, 20))
        self.btn_new_password.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.account_setting, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_new_login.setPlaceholderText(_translate("Dialog", "Новый логин"))
        self.lineEdit_user_password_login.setPlaceholderText(_translate("Dialog", "Введите пароль"))
        self.btn_new_login.setText(_translate("Dialog", "Сменить логин"))
        self.label.setText(_translate("Dialog", "Сменить логин"))
        self.label_2.setText(_translate("Dialog", "Сменить пароль"))
        self.lineEdit_old_user_password.setPlaceholderText(_translate("Dialog", "Старый пароль"))
        self.lineEdit_new_user_password_1.setPlaceholderText(_translate("Dialog", "Новый пароль"))
        self.lineEdit_new_user_password_2.setPlaceholderText(_translate("Dialog", "Подтвердите пароль"))
        self.btn_new_password.setText(_translate("Dialog", "Сменить пароль"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account_setting), _translate("Dialog", "Аккаунт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Пока ничего"))
