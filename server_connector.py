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
                              json={'login': user_login,
                                    'password': user_password}).json()
        print(result)
        print("_________________")
        if result["auth"] == "rejected":
            raise SecurityError

        self.user_id = result['auth']
        self.user_login = user_login
        self.user_password = user_password


