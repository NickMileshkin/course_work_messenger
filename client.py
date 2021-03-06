import sys  # sys нужен для передачи argv в QApplication
import os
import requests.exceptions
from PyQt5 import QtWidgets, QtCore
from datetime import datetime

from server_connector import ServerConnector, SecurityError
from Interface.registration import Ui_RegistrationWindow  # Это наш конвертированный файл дизайна
from Interface.authorization import Ui_AuthorizationWindow
from Interface.main_page import Ui_MainWindow
from Interface.settings import Ui_SettingWindow
from clientDB import ClientDatabase


class RegistrationWindow(QtWidgets.QDialog, Ui_RegistrationWindow):  # класс, отвечающий за окно регистрации
    def __init__(self, server: ServerConnector):
        super().__init__()
        self.server = server
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_registration.clicked.connect(self.registration_acc)
        self.login = None
        self.password = None
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def registration_acc(self):
        self.login = self.lineEdit_login.text()
        self.password = self.lineEdit_password.text()
        if len(self.login) >= 5 and len(self.password) >= 5:
            if self.server.add_new_user(self.login, self.password):
                self.close()


class AuthorizationWindow(QtWidgets.QDialog, Ui_AuthorizationWindow):  # класс, отвечающий за окно авторизации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_accepted = None
        self.label_2.clicked.connect(self.go_to_registration_window)
        self.btn_authorization.clicked.connect(self.authorization_acc)
        self.login = None
        self.password = None
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def authorization_acc(self):
        self.login = (self.lineEdit_login.text())
        self.password = (self.lineEdit_password.text())
        if (self.login != '') and (self.password != ''):
            self.is_accepted = True
            self.close()

    def go_to_registration_window(self):
        registration_window = RegistrationWindow(connector)
        registration_window.exec()


class SettingsWindow(QtWidgets.QDialog, Ui_SettingWindow):
    def __init__(self, server: ServerConnector):
        super().__init__()
        self.server = server
        self.setupUi(self)
        self.btn_new_password.clicked.connect(self.set_new_password)
        self.btn_new_login.clicked.connect(self.set_new_login)
        self.new_password_1 = None
        self.new_password_2 = None
        self.old_password = None
        self.accept_user_password = None
        self.new_login = None
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    def set_new_password(self):
        self.label_message.setText('')
        self.old_password = self.lineEdit_old_user_password.text()
        self.new_password_1 = self.lineEdit_new_user_password_1.text()
        self.new_password_2 = self.lineEdit_new_user_password_2.text()
        if self.new_password_1 == self.new_password_2 and len(self.new_password_1) >= 5:
            try:
                self.server.change_password(self.old_password, self.new_password_1)
            except SecurityError:
                self.label_message.setText(connector.report_message)

            self.lineEdit_old_user_password.clear()
            self.lineEdit_new_user_password_1.clear()
            self.lineEdit_new_user_password_2.clear()
            self.new_password_1 = None
            self.new_password_2 = None
            self.old_password = None
            self.label_message.setText(connector.report_message)
        else:
            self.label_message.setText("Ошибка! Пароли не совпадают или длина нового пароля меньше 5")

    def set_new_login(self):
        self.new_login = self.lineEdit_new_login.text()
        self.accept_user_password = self.lineEdit_user_password_login.text()

        if len(self.new_login) >= 5:
            try:
                self.server.change_login(self.new_login, self.accept_user_password)
            except SecurityError:
                self.label_message.setText(connector.report_message)
            self.lineEdit_user_password_login.clear()
            self.lineEdit_new_login.clear()
            self.accept_user_password = None
            self.new_login = None
            self.label_message.setText(connector.report_message)
            main_window.label_user_name.setText(connector.user_login)
        else:
            self.label_message.setText("Ошибка! Длина нового логина меньше 5")


class MainPage(QtWidgets.QMainWindow, Ui_MainWindow):  # класс, отвечающий за главное окно
    def __init__(self, server: ServerConnector):
        super().__init__()
        self.setupUi(self)
        self.server = server
        self.client_db = server.client_db
        self.active_dialog = None  # хранит активный диалог
        self.dialogs = []

        self.user_id = server.user_id
        self.user_login = server.user_login
        self.user_password = server.user_password

        self.server.add_dialogs()

        dial = self.server.client_db.get_dialogs()
        for i in range(len(self.server.client_db.get_dialogs())):
            self.add_dialog(dial[i][0], dial[i][1])

        self.server.get_all_messages()

        self.btn_send_message.clicked.connect(self.send_message)
        self.textEdit_message.setEnabled(False)  # Отключает возможность ввода сообщения
        self.btn_search_user.clicked.connect(self.find_user)
        self.label_user_name.setText(self.user_login)
        self.label_user_id.setText("# " + str(self.user_id))
        self.btn_settings.clicked.connect(self.open_setting)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    # функция отправки сообщения
    def send_message(self):
        message_text = self.textEdit_message.text()
        time = (str(datetime.now()).split('.')[0])
        if message_text != '' and not(message_text.isspace()):
            self.server.send_message(self.active_dialog.id, message_text, time)
            new_message = Message(message_text, time, self.user_id, True, self.server)
            new_message.clicked.connect(new_message.p)
            self.client_db.add_message(self.user_id, self.active_dialog.id, time, message_text, True)
            self.active_dialog.messages.append(new_message)
            self.scrollLayout_message.addRow(new_message)
            self.vbar_scrollArea_message.setValue(self.vbar_scrollArea_message.maximum())
        self.active_dialog.server.read_this_dialog(self.active_dialog.id)
        self.textEdit_message.clear()

    # функция добавления диалога
    def add_dialog(self, dialog_id, interlocutors_id):
        new_dialog = Dialog(dialog_id, interlocutors_id, self.server)
        new_dialog.clicked.connect(new_dialog.open_dialogs)
        self.dialogs.append(new_dialog)
        self.scrollLayout_dialogs.addRow(new_dialog)

    # функция отвечающая за нажатие кнопки
    def keyPressEvent(self, event):
        if event.key() == 16777220:  # нажатие Enter
            if self.active_dialog != None:
                self.send_message()
                self.vbar_scrollArea_message.setValue(self.vbar_scrollArea_message.maximum())

    # функция открытия окна с поиском аккаунта
    def find_user(self):
        user_id = self.textEdit_search.text()
        user_login = None
        if user_id != '':
            user_login = self.server.find_user(int(user_id))
        if user_login != 'None':
            new_dialog = self.server.create_new_dialog(user_id)
            if new_dialog['status'] != 'error':
                self.server.client_db.add_dialog(new_dialog['dialog_id'], user_id)
                self.add_dialog(new_dialog['dialog_id'], user_id)
            else:
                message = QtWidgets.QMessageBox()
                message.setText('Попытка создать уже существующий диалог')
                message.setWindowTitle('Диалог уже существует')
                message.exec()
        else:
            message = QtWidgets.QMessageBox()
            message.setText('Аккаунта с таким ID не существует')
            message.setWindowTitle('Аккаунта не существует')
            message.exec()
        self.textEdit_search.setText("")

    def open_setting(self):
        settings_window = SettingsWindow(self.server)
        settings_window.exec()

    def update_data(self):

        self.server.get_new_messages()
        dial = self.server.get_dialogs()
        data = self.client_db.get_dialogs()
        for i in range((len(dial)-1)//2):
            if (dial["dialog_id"+str(i)], dial["account_id"+str(i)]) not in data:
                self.client_db.add_dialog(dial["dialog_id"+str(i)], dial["account_id"+str(i)])
                self.add_dialog(dial["dialog_id"+str(i)], dial["account_id"+str(i)])

        for i in reversed(range(self.scrollLayout_message.count())):
            widgetToRemove = self.scrollLayout_message.itemAt(i).widget()
            # remove it from the layout list
            self.scrollLayout_message.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
        for i in range(len(self.dialogs)):
            self.server.read_this_dialog(self.dialogs[i].id)
            if self.active_dialog != None:
                self.dialogs[i].update_message()

        if self.active_dialog != None:
            for i in range(len(self.active_dialog.messages)):
                self.scrollLayout_message.addRow(self.active_dialog.messages[i])


class ClickableWidget(QtWidgets.QWidget):  # класс для виджетов, на которые можно нажимать
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QWidget.mousePressEvent(self, QMouseEvent)


class Message(ClickableWidget):  # класс сообшения
    def __init__(self, message_text, message_time, message_sender, is_new, server: ServerConnector):
        super(Message, self).__init__()
        self.server = server
        if message_sender == server.user_id:
            self.name = QtWidgets.QLabel("Вы")
        else:
            self.name = QtWidgets.QLabel(self.server.active_dialog.interlocutor_login)
        self.is_new = is_new
        self.message_text = QtWidgets.QLabel(message_text)
        self.message_text.setWordWrap(True)
        self.message_time = QtWidgets.QLabel(message_time)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.message_text)
        layout.addWidget(self.message_time)
        self.setLayout(layout)

    def p(self):  # Временная заглушка функция выполняется при нажатии на сообщение
        print(self.message_time.text())


class Dialog(ClickableWidget):  # Класс диалог
    def __init__(self, dialogs_id, interlocutor_id, server: ServerConnector):
        super(Dialog, self).__init__()
        self.id = dialogs_id
        self.interlocutor_id = interlocutor_id
        self.server = server
        self.interlocutor_login = self.server.find_user(self.interlocutor_id)
        self.container = QtWidgets.QWidget(self)
        self.container.setGeometry(QtCore.QRect(0, 0, 198, 50))
        self.name = QtWidgets.QLabel(self.interlocutor_login)
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.line)
        self.container.setStyleSheet("background-color:white;")
        self.messages = []
        self.setLayout(self.layout)

    def open_dialogs(self):  # функция отвечающая за открытие экземпляра класса диалог
        if self != main_window.active_dialog:
            self.server.read_this_dialog(self.id)
            self.server.active_dialog = self
            main_window.textEdit_message.clear()
            if main_window.active_dialog != None:
                main_window.active_dialog.container.setStyleSheet("background-color:white;")
            main_window.active_dialog = self

            for i in reversed(range(main_window.scrollLayout_message.count())):
                widgetToRemove = main_window.scrollLayout_message.itemAt(i).widget()
                # remove it from the layout list
                main_window.scrollLayout_message.removeWidget(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)
            for i in range(len(self.messages)):
                main_window.scrollLayout_message.addRow(self.messages[i])
            self.container.setStyleSheet("background-color:rgb(183, 242, 255);")
            main_window.textEdit_message.setEnabled(True)
            main_window.vbar_scrollArea_message.setValue(main_window.vbar_scrollArea_message.maximum())

    def update_message(self):
        self.messages = []
        messages = self.server.client_db.get_messages(self.id)
        for i in range(len(messages)):

            new_message = Message(messages[i][2], messages[i][1], messages[i][0], messages[i][3], self.server)
            self.messages.append(new_message)


if __name__ == '__main__':

    try:
        os.remove("ClientDB.sqlite")
    except FileNotFoundError:
        pass
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    client_db = ClientDatabase()
    connector = ServerConnector("http://127.0.0.1", 5000, client_db)
    authorization_window = AuthorizationWindow()
    authorization_window.exec_()
    if authorization_window.is_accepted:
        try:
            connector.set_user(authorization_window.login, authorization_window.password)
        except requests.exceptions.ConnectionError:
            message = QtWidgets.QMessageBox()
            message.setText('Проверьте подключение к интернету и попробуйте попытку снова')
            message.setWindowTitle('Сервер не отвечает')
            message.exec()
            sys.exit(1)
        except SecurityError:
            error_box = QtWidgets.QErrorMessage()
            error_box.showMessage("Проверьте правильность логина и пароля!")
            error_box.setWindowTitle("Неправильный логин или пароль")
            error_box.exec()
            sys.exit()

        main_window = MainPage(connector)
        main_window.show()
    else:
        sys.exit()

    app.exec_()  # то запускаем функцию main()

