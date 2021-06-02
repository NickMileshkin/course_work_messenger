import requests
from clientDB import ClientDatabase
from math import ceil
class SecurityError(Exception):
    pass


class JsonError(Exception):
    pass



def encryption(s):
    cod = ''
    k = 'Зачёт'
    m = []
    n = int(ceil(len(s) / len(k)))  # колличество строк в таблице
    z = 0  #
    for i in range(len(k)):  # Создание таблицы
        m.append([k[i]])
        for j in range(n):
            if z <= len(s)-1:
                m[i].append(s[z])
            else:
                m[i].append('*')  # заполнение пустых ячеек таблицы
            z += 1

    m.sort()
    for j in range(1, n+1):
        for i in range(len(k)):
            cod = cod + str(m[i][j])

    return cod


def decryption(cod):
    decod = ''
    m = []
    z = 0
    k = 'Зачёт'
    sort_k = []
    for i in range(len(k)):
        sort_k.append(k[i])
    sort_k.sort()  # создание отсортированного ключа
    n = int(ceil(len(cod) / len(k)))  # колличество строк в таблице
    for i in range(len(k)):
        m.append([])  # создание пустой таблицы

    for j in range(n):
        for i in range(len(k)):
            m[i].append(cod[z])
            z += 1
    for i in range(len(k)):
        m[i].append(sort_k[i])  # добавление в конец таблицы отсортированного ключа
    for i in range(len(k)):
        for j in range(len(k)):
            if k[i] == m[j][n]:  # сравнение последней строки таблицы с ключом
                tmp = m[j]
                m[j] = m[i]
                m[i] = tmp
    for i in range(len(k)):
        for j in range(n):
            decod += m[i][j]
    decod = decod.replace('*', '')
    return decod


class ServerConnector:

    def __init__(self, address, port, client_db: ClientDatabase):
        self.url = f"{address}:{port}"
        self.user_id = None
        self.client_db = client_db
        self.user_login = None
        self.user_password = None
        self.report_message = None
        self.active_dialog = None
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
                                     'message': encryption(message),
                                     'password': self.user_password}).json()

        if result['status'] == 'error':
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
                raise SecurityError

    def get_dialogs(self):
        result = requests.post(f'{self.url}/dialogs/{self.user_id}',
                               json={'user_id': self.user_id,
                                     'password': self.user_password}).json()
        return result

    def create_new_dialog(self, interlocutor_id):
        result = requests.get(f'{self.url}/dialogs/{self.user_id}/{interlocutor_id}',
                               json={'user1_id': self.user_id,
                                     'user2_id': interlocutor_id}).json()
        if result['status'] == 'error':
            self.report_message = "Диалог уже существует"
            return result
        else:
            self.report_message = "Диалог добавлен"
            return result

    def add_dialogs(self):
        result = requests.post(f'{self.url}/dialogs/{self.user_id}',
                               json={'user_id': self.user_id,
                                     'password': self.user_password}).json()
        for i in range((len(result)-1) // 2):
            self.client_db.add_dialog(result["dialog_id" + str(i)], result["account_id"+str(i)])

    def get_all_messages(self):
        result = requests.post(f'{self.url}/messages/{self.user_id}',
                                        json={'account_id': self.user_id,
                                              'password': self.user_password}).json()

        for i in range((len(result)-1)//5):
            self.client_db.add_message(result['account_id' + str(i)], result['dialog_id' + str(i)],
                                       result['time' + str(i)], decryption(result['message' + str(i)]),
                                       result['is_new' + str(i)])

    def read_this_dialog(self, dialog_id):
        requests.post(f'{self.url}/dialogs/{dialog_id}/read',
                               json={'account_id': self.user_id,
                                     'password': self.user_password}).json()

    def get_new_messages(self):
        result = requests.post(f'{self.url}/messages/{self.user_id}/new',
                               json={'user_id': self.user_id,
                                     'password': self.user_password}).json()
        if result['status'] != 'error':
            for i in range((len(result)-1)//4):
                if result['account_id' + str(i)] != self.user_id:
                    self.client_db.add_message(result['account_id' + str(i)], result['dialog_id' + str(i)],
                                               result['time' + str(i)], decryption(result['message' + str(i)]), True)


