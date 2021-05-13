from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollLayout_message = QtWidgets.QFormLayout()
        self.scrollLayout_dialogs = QtWidgets.QFormLayout()

        self.scrollArea_dialogs = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_dialogs.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea_dialogs.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea_dialogs.setWidgetResizable(True)
        self.scrollArea_dialogs.setObjectName("scrollArea_dialogs")

        self.scrollArea_dialogs_Widget = QtWidgets.QWidget()
        self.scrollArea_dialogs_Widget.setLayout(self.scrollLayout_dialogs)
        self.scrollArea_dialogs_Widget.setGeometry(QtCore.QRect(0, 0, 198, 777))
        self.scrollArea_dialogs_Widget.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_dialogs.setWidget(self.scrollArea_dialogs_Widget)
        self.gridLayout.addWidget(self.scrollArea_dialogs, 0, 0, 1, 3)

        self.textEdit_message = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_message.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_message.setObjectName("textEdit_message")
        self.gridLayout.addWidget(self.textEdit_message, 2, 4, 1, 1)

        self.scrollArea_message = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_message.setMinimumSize(QtCore.QSize(600, 0))
        self.scrollArea_message.setWidgetResizable(True)
        self.scrollArea_message.setObjectName("scrollArea_message")

        self.scrollArea_message_Widget = QtWidgets.QWidget()
        self.scrollArea_message_Widget.setLayout(self.scrollLayout_message)
        self.scrollArea_message_Widget.setGeometry(QtCore.QRect(0, 0, 870, 777))
        self.scrollArea_message_Widget.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_message.setWidget(self.scrollArea_message_Widget)
        self.gridLayout.addWidget(self.scrollArea_message, 0, 4, 1, 2)

        self.btn_send_message = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_message.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_send_message.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_send_message.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("send_message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_send_message.setIcon(icon)
        self.btn_send_message.setIconSize(QtCore.QSize(30, 30))
        self.btn_send_message.setObjectName("btn_send_message")
        self.gridLayout.addWidget(self.btn_send_message, 2, 5, 1, 1)
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_settings.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Setings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QtCore.QSize(30, 30))
        self.btn_settings.setObjectName("btn_settings")
        self.gridLayout.addWidget(self.btn_settings, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 3, 1, 1)
        self.label_user_name = QtWidgets.QLabel(self.centralwidget)
        self.label_user_name.setObjectName("label_user_name")
        self.gridLayout.addWidget(self.label_user_name, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_user_name.setText(_translate("MainWindow", "TextLabel"))