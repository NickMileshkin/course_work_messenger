import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
from Interface.registration import Ui_RegistrationWindow  # Это наш конвертированный файл дизайна
from Interface.authorization import Ui_AuthorizationWindow
from Interface.main_page import Ui_MainWindow


class RegistrationWindow(QtWidgets.QMainWindow, Ui_RegistrationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_registration.clicked.connect(self.registration_acc)
        self.label_2.clicked.connect(self.go_to_authorization_window)
        self.label_2.clicked.connect(self.close)
        self.authorization_window = AuthorizationWindow()

    def registration_acc(self):
        login = (self.line_edit_login.text())
        password = (self.line_edit_password.text())
        if (login != '') and (password != ''):
            print("login = ", login)
            print("password = ", password)

    def go_to_authorization_window(self):

        self.authorization_window.show()


class AuthorizationWindow(QtWidgets.QMainWindow, Ui_AuthorizationWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_authorization.clicked.connect(self.authorization_acc)
        self.btn_authorization.clicked.connect(self.close)
        self.main_window = MainPage()

    def authorization_acc(self):
        login = (self.line_edit_login.text())
        password = (self.line_edit_password.text())
        if (login != '') and (password != ''):
            self.main_window.show()


class MainPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.messages = []
        self.btn_send_message.clicked.connect(self.send_message)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def send_message(self):
        if self.textEdit_message.text() != '':
            new_message = Message()
            new_message.clicked.connect(new_message.p)
            self.messages.append(new_message)

            self.scrollLayout_message.addRow(new_message)
            self.textEdit_message.clear()


class ClickableMessage(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QWidget.mousePressEvent(self, QMouseEvent)


class Message(ClickableMessage):
    def __init__(self):
        super(Message, self).__init__()
        self.name = QtWidgets.QLabel("You")
        self.message_text = QtWidgets.QLabel(registration_window.authorization_window.main_window.textEdit_message
                                             .text())  # надо сделать как-то подругому
        self.message_time = QtWidgets.QLabel(str(datetime.now().time()).split(".")[0])
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.message_text)
        layout.addWidget(self.message_time)

        self.setLayout(layout)

    def p(self):
        print(self.message_time.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    registration_window = RegistrationWindow()
    registration_window.show()  # Показываем окно
    app.exec_()  # то запускаем функцию main()

