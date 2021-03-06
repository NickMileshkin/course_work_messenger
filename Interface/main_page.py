from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_user_name = QtWidgets.QLabel(self.centralwidget)
        self.label_user_name.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_user_name.setObjectName("label_user_name")
        self.verticalLayout_2.addWidget(self.label_user_name)

        self.label_user_id = QtWidgets.QLabel(self.centralwidget)
        self.label_user_id.setMinimumSize(QtCore.QSize(15, 15))
        self.label_user_id.setMaximumSize(QtCore.QSize(1000, 15))
        self.label_user_id.setObjectName("label_iser_id")
        self.verticalLayout_2.addWidget(self.label_user_id)

        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.textEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_search.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_search.setObjectName("textEdit_login")
        self.textEdit_search.setPlaceholderText("Поиск друзей по ID")
        self.horizontalLayout.addWidget(self.textEdit_search)

        self.btn_search_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search_user.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_search_user.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_search_user.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search_user.setIcon(icon)
        self.btn_search_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_search_user.setObjectName("btn_search_login")
        self.horizontalLayout.addWidget(self.btn_search_user)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.scrollLayout_message = QtWidgets.QFormLayout()
        self.scrollLayout_dialogs = QtWidgets.QFormLayout()

        self.scrollArea_dialogs = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_dialogs.setMinimumSize(QtCore.QSize(200, 650))
        self.scrollArea_dialogs.setMaximumSize(QtCore.QSize(250, 1080))
        self.scrollArea_dialogs.setWidgetResizable(True)
        self.scrollArea_dialogs.setObjectName("scrollArea_dialogs")

        self.scrollArea_dialogs_Widget = QtWidgets.QWidget()
        self.scrollArea_dialogs_Widget.setLayout(self.scrollLayout_dialogs)
        self.scrollArea_dialogs_Widget.setGeometry(QtCore.QRect(0, 0, 198, 777))
        self.scrollArea_dialogs_Widget.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_dialogs.setWidget(self.scrollArea_dialogs_Widget)
        self.verticalLayout.addWidget(self.scrollArea_dialogs)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.textEdit_message = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_message.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_message.setObjectName("textEdit_message")
        self.horizontalLayout_2.addWidget(self.textEdit_message)

        self.btn_send_message = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_message.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_send_message.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_send_message.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("send_message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_send_message.setIcon(icon1)
        self.btn_send_message.setIconSize(QtCore.QSize(25, 25))
        self.btn_send_message.setObjectName("btn_send_message")
        self.horizontalLayout_2.addWidget(self.btn_send_message)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 3, 1, 1)

        self.scrollArea_message = QtWidgets.QScrollArea(self.centralwidget)
        self.vbar_scrollArea_message = self.scrollArea_message.verticalScrollBar()
        self.scrollArea_message.setMinimumSize(QtCore.QSize(1100, 600))
        self.scrollArea_message.setWidgetResizable(True)
        self.scrollArea_message.setObjectName("scrollArea_message")

        self.scrollArea_message_Widget = QtWidgets.QWidget()
        self.scrollArea_message_Widget.setLayout(self.scrollLayout_message)
        self.scrollArea_message_Widget.setGeometry(QtCore.QRect(0, 0, 1098, 728))
        self.scrollArea_message_Widget.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_message.setWidget(self.scrollArea_message_Widget)
        self.gridLayout.addWidget(self.scrollArea_message, 0, 4, 1, 1)

        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_settings.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_settings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setIconSize(QtCore.QSize(25, 25))
        self.btn_settings.setObjectName("btn_settings")
        self.gridLayout.addWidget(self.btn_settings, 2, 2, 1, 1)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 4, 1, 1)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 3, 1, 1)

        self.label_user_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_user_pic.setMinimumSize(QtCore.QSize(30, 30))
        self.label_user_pic.setMaximumSize(QtCore.QSize(30, 30))
        self.label_user_pic.setText("")
        self.label_user_pic.setObjectName("label_user_pic")
        self.gridLayout.addWidget(self.label_user_pic, 2, 0, 1, 1)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мессенджер"))
        self.label_user_name.setText(_translate("MainWindow", "TextLabel"))
        self.label_user_id.setText(_translate("MainWindow", "TextLabel"))