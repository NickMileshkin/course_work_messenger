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

        self._dialogs = []
        self._messages = []

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

    def send_message(self, dialog_id, message):
        result = requests.post(f'{self.url}/messages',
                               json={'account_id': self.user_id,
                                     'dialog_id': dialog_id,
                                     'time': str(datetime.now().time()).split(".")[0],
                                     'message': message}).json()

        if result['status'] == 'error':
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
                raise SecurityError

    def create_new_dialog(self, interlocutor_id):
        result = requests.get(f'{self.url}/dialogs/{self.user_id}/{interlocutor_id}',
                               json={'user1_id': self.user_id,
                                     'user2_id': interlocutor_id}).json()
        if result['status'] == 'error':
            self.report_message = "Диалог уже существует"
            return result['status']
        else:
            self.report_message = "Диалог добавлен"
            return result['status']
