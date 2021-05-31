import requests


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
        self.views = set()

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
            self.user_id = result['status']
            self.user_login = user_login
            self.user_password = user_password

    def change_login(self, new_login, user_password):

        result = requests.post(f"{self.url}/accounts/{self.user_id}/login",
                               json={'password': user_password,
                                     'new_login': new_login}).json()
        if result['status'] == "error":
            raise Exception(result['message'])
        elif result['status'] == 'rejected':
            raise SecurityError
        else:
            self.user_login = new_login

    def change_password(self, user_password, new_password):
        result = requests.post(f'{self.url}/accounts/{int(self.user_id)}/password',
                               json={'password': user_password,
                                     'new_password': new_password}).json()
        if result['status'] == "error":
            if result['message'] == 'request should be in json':
                raise JsonError
            else:
               raise SecurityError
        else:
            self.user_password = new_password



