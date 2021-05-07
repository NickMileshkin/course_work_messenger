from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'


@app.route('/accounts', methods=['GET'])
def get_account():
    return db.get_account()


@app.route('/accounts', methods=['POST'])
def add_new_account():
    return db.add_new_account(id_, login, password)


@app.route('/accounts/<int: account_id/password', methods=['POST'])
def change_password(account_id):
    return db.change_password(account_id, new_password)


@app.route('/accounts/<int: account_id/login', methods=['POST'])
def change_login(account_id):
    return db.change_login(account_id, new_login)


if __name__ == '__main__':
    app.run()
