import requests


class SecurityError(Exception):
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
                              json={'user_id': user_login,
                                    'password': user_password}).json()
        if result['status'] == 'error':
            if result['message'] == 'wrong user or password':
                raise SecurityError
            raise Exception
        self.user_id = result['id']
        self.user_login = user_login
        self.user_password = user_password


