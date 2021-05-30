import sys  # sys нужен для передачи argv в QApplication
from server_connector import ServerConnector, SecurityError
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
from Interface.registration import Ui_RegistrationWindow  # Это наш конвертированный файл дизайна
from Interface.authorization import Ui_AuthorizationWindow
from Interface.main_page import Ui_MainWindow


class RegistrationWindow(QtWidgets.QDialog, Ui_RegistrationWindow):  # класс, отвечающий за окно регистрации
    def __init__(self, server: ServerConnector):
        super().__init__()
        self.server = server
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_registration.clicked.connect(self.registration_acc)
        self.login = None
        self.password = None

    def registration_acc(self):
        self.login = self.lineEdit_login.text()
        self.password = self.lineEdit_password.text()
        if self.server.add_new_user(self.login, self.password):
            self.close()
        else:
            print("Ты Чмо")


class AuthorizationWindow(QtWidgets.QDialog, Ui_AuthorizationWindow):  # класс, отвечающий за окно авторизации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_accepted = None
        self.label_2.clicked.connect(self.go_to_registration_window)
        self.btn_authorization.clicked.connect(self.authorization_acc)
        self.login = None
        self.password = None
    def authorization_acc(self):
        self.login = (self.lineEdit_login.text())
        self.password = (self.lineEdit_password.text())
        if (self.login != '') and (self.password != ''):
            self.is_accepted = True
            self.close()

    def go_to_registration_window(self):
        registration_window = RegistrationWindow(connector)
        registration_window.exec()


class MainPage(QtWidgets.QMainWindow, Ui_MainWindow):  # класс, отвечающий за главное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prev_active_dialog = 0
        self.active_dialog = 0  # хранит номер активного диалога
        self.dialogs_count = 0  # количество диалогов
        self.messages = [[]]  # список списков для хранения сообщений по каждому диалогу
        self.dialogs = []  # хранит экземпляры Класса Dialog
        self.btn_send_message.clicked.connect(self.send_message)
        self.textEdit_message.setEnabled(False)  # Отключает возможность ввода сообщения
        self.btn_search_login.clicked.connect(self.search_account)
        self.label_user_name.setText(authorization_window.lineEdit_login.text())

    # функция отправки сообщения
    def send_message(self):
        if self.textEdit_message.text() != '' and not(self.textEdit_message.text().isspace()):
            new_message = Message()
            new_message.clicked.connect(new_message.p)
            self.messages[self.active_dialog].append(new_message)
            self.scrollLayout_message.addRow(new_message)
            self.vbar_scrollArea_message.setValue(self.vbar_scrollArea_message.maximum())

        self.textEdit_message.clear()

    # функция добавления диалога
    def add_dialog(self):
        new_dialog = Dialog()
        self.dialogs_count += 1
        self.messages.append([])
        new_dialog.clicked.connect(new_dialog.open_dialogs)
        self.dialogs.append(new_dialog)
        self.scrollLayout_dialogs.addRow(new_dialog)

    # функция отвечающая за нажатие кнопки
    def keyPressEvent(self, event):
        if event.key() == 16777220:  # нажатие Enter
            self.send_message()
            self.vbar_scrollArea_message.setValue(self.vbar_scrollArea_message.maximum())
        if event.key() == 61:  # условия для проверки работы добавления диалогов
            self.add_dialog()

    # функция открытия окна с поиском аккаунта
    def search_account(self):
        pass


class ClickableWidget(QtWidgets.QWidget):  # класс для виджетов, на которые можно нажимать
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QWidget.mousePressEvent(self, QMouseEvent)


class Message(ClickableWidget):  # класс сообшения
    def __init__(self):
        super(Message, self).__init__()
        self.name = QtWidgets.QLabel("You")
        self.message_text = QtWidgets.QLabel(main_window.textEdit_message.text())
        self.message_text.setWordWrap(True)
        self.message_time = QtWidgets.QLabel(str(datetime.now().time()).split(".")[0])
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.message_text)
        layout.addWidget(self.message_time)

        self.setLayout(layout)

    def p(self):  # Временная заглушка функция выполняется при нажатии на сообщение
        print(self.message_time.text())


class Dialog(ClickableWidget):  # Класс диалог
    def __init__(self):
        super(Dialog, self).__init__()
        self.number = main_window.dialogs_count
        self.container = QtWidgets.QWidget(self)
        self.container.setGeometry(QtCore.QRect(0, 0, 198, 50))
        self.name = QtWidgets.QLabel("Somebody " + str(self.number))
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.line)
        self.container.setStyleSheet("background-color:white;")

        self.setLayout(self.layout)

    def open_dialogs(self):  # функция отвечающая за открытие экземпляра класса диалог
        main_window.textEdit_message.clear()
        for i in reversed(range(main_window.scrollLayout_message.count())):
            widgetToRemove = main_window.scrollLayout_message.itemAt(i).widget()
            # remove it from the layout list
            main_window.scrollLayout_message.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

        for i in range(len(main_window.messages[self.number])):
            main_window.scrollLayout_message.addRow(main_window.messages[self.number][i])

        for i in range(len(main_window.dialogs)):
            main_window.dialogs[i].container.setStyleSheet("background-color:white;")

        self.container.setStyleSheet("background-color:blue;")
        main_window.textEdit_message.setEnabled(True)
        main_window.active_dialog = self.number
        main_window.vbar_scrollArea_message.setValue(main_window.vbar_scrollArea_message.maximum())


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    connector = ServerConnector("http://127.0.0.1", 5000)

    authorization_window = AuthorizationWindow()
    authorization_window.exec()
    main_window = MainPage()
    """if authorization_window.is_accepted:
        try:
            connector.add_new_user(authorization_window.)
        main_window = MainPage()
        main_window.show()"""
    app.exec_()  # то запускаем функцию main()
