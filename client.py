import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from Interface.registration import Ui_RegistrationWindow  # Это наш конвертированный файл дизайна


class RegistrationWindow(QtWidgets.QMainWindow, Ui_RegistrationWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_registration.clicked.connect(self.registration_acc)
        self.label_2.clicked.connect(self.go_to_authorization_window)
        self.label_2.clicked.connect(self.close)

    def registration_acc(self):
        login = (self.line_edit_login.text())
        password = (self.line_edit_password.text())
        if (login != '') and (password != ''):
            print("login = ", login)
            print("password = ", password)


    def go_to_authorization_window(self):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()


class AuthorizationWindow(QtWidgets.QMainWindow, Ui_RegistrationWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    registration_window = RegistrationWindow()  # Создаём объект класса ExampleApp
    registration_window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

