import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
from Interface.registration import Ui_RegistrationWindow  # Это наш конвертированный файл дизайна
from Interface.authorization import Ui_AuthorizationWindow
from Interface.main_page import Ui_MainWindow


class RegistrationWindow(QtWidgets.QMainWindow, Ui_RegistrationWindow):  # класс, отвечающий за окно регистрации
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


class AuthorizationWindow(QtWidgets.QMainWindow, Ui_AuthorizationWindow):  # класс, отвечающий за окно авторизации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_authorization.clicked.connect(self.authorization_acc)
        self.btn_authorization.clicked.connect(self.close)
        global main_window
        main_window = MainPage()

    def authorization_acc(self):
        login = (self.line_edit_login.text())
        password = (self.line_edit_password.text())
        if (login != '') and (password != ''):
            main_window.show()


class MainPage(QtWidgets.QMainWindow, Ui_MainWindow):  # класс, отвечающий за главное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.active_dialog = 0  # хранит номер активного диалога
        self.dialogs_count = 0  # количество диалогов
        self.messages = [[]]  # список списков для хранения сообщений по каждому диалогу
        self.dialogs = []  # храни экземпляры Класса Dialog
        self.btn_send_message.clicked.connect(self.send_message)
        self.textEdit_message.setEnabled(False)  # Отключает возможность ввода сообщения

    # функция отправки сообщения
    def send_message(self):
        if self.textEdit_message.text() != '':
            new_message = Message()
            new_message.clicked.connect(new_message.p)
            self.messages[self.active_dialog].append(new_message)
            self.scrollLayout_message.addRow(new_message)

            self.textEdit_message.clear()
            self.vbar_scrollArea_message.setValue(self.vbar_scrollArea_message.maximum())

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
        self.name = QtWidgets.QLabel("Somebody ")
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
    # x = input()
    """if x == "reg":
        registration_window = RegistrationWindow()
        registration_window.show()  # Показываем окно
    else:
        main_window = MainPage()
        main_window.show()"""
    main_window = MainPage()
    main_window.show()
    app.exec_()  # то запускаем функцию main()
