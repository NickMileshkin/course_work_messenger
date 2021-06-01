import requests
from datetime import datetime


class SecurityError(Exception):
    pass


class JsonError(Exception):
    pass


class ServerConnector:

    def __init__(self, address, port):
        self.url = f"{address}:{port}"
        self.user_id = None
        self.user_login = None
        self.user_password = None
        self.report_message = None

        self.dialogs = []
        self.interlocutors_id = []
        self.messages = []

    def add_new_user(self, user_login, user_password):
        result = requests.post(f"{self.url}/accounts",
                               json={
                                   'login': user_login,
                                   'password': user_password
                               }).json()
        return result['status'] == 'ok'

    def set_user(self, user_login, user_password):
        result = requests.post(f"{self.url}/accounts/auth",
                              json={'login': user_login,
                                    'password': user_password}).json()
        if result['status'] == "error":
            raise Exception(result['message'])
        elif result['status'] == 'rejected':
            raise SecurityError
        else:
            self.user_id = result['id']
            self.user_login = user_login
            self.user_password = user_password

    def change_login(self, new_login, user_password):
        self.report_message = None
        result = requests.post(f"{self.url}/accounts/{self.user_id}/login",
                               json={'password': user_password,
                                     'new_login': new_login}).json()
        if result['status'] == "error":
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
                self.report_message = "Ошибка! Введён не правильный пароль"
                raise SecurityError
        else:
            self.report_message = "Логин изменён"
            self.user_login = new_login

    def change_password(self, user_password, new_password):
        self.report_message = None
        result = requests.post(f'{self.url}/accounts/{int(self.user_id)}/password',
                               json={'password': user_password,
                                     'new_password': new_password}).json()
        if result['status'] == 'error':
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
                self.report_message = "Ошибка! Введён не правильный пароль"
                raise SecurityError
        else:
            self.report_message = "Пароль изменён!"
            self.user_password = new_password

    def find_user(self, account_id):
        self.report_message = None
        result = requests.get(f'{self.url}/accounts/{account_id}',
                               json={'account_id': account_id}).json()
        if result['status'] == 'error':
            self.report_message = 'Такого аккаунта не существует'
            return 'None'
        else:
            return result['login']

    def send_message(self, dialog_id, message, time):
        result = requests.post(f'{self.url}/messages',
                               json={'account_id': self.user_id,
                                     'dialog_id': dialog_id,
                                     'time': time,
                                     'message': message,
                                     'password': self.user_password}).json()

        if result['status'] == 'error':
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
                raise SecurityError

    def create_new_dialog(self, interlocutor_id):
        result = requests.get(f'{self.url}/dialogs/{self.user_id}/{interlocutor_id}',
                               json={'user1_id': self.user_id,
                                     'user2_id': interlocutor_id}).json()
        print(result)
        if result['status'] == 'error':
            self.report_message = "Диалог уже существует"
            return result
        else:
            self.report_message = "Диалог добавлен"
            return result

    def get_dialogs(self):
        result = requests.post(f'{self.url}/dialogs/{self.user_id}',
                               json={'user_id': self.user_id,
                                     'password': self.user_password}).json()
        for i in range((len(result)-1) // 2):
            self.dialogs.append(result["dialog_id" + str(i)])
            self.interlocutors_id.append(result["account_id"+str(i)])

    def get_all_messages(self):
        result = result = requests.post(f'{self.url}/messages/{self.user_id}',
                                        json={'user_id': self.user_id,
                                              'password': self.user_password}).json()
        print(result)
