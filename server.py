import json
from flask import Flask, request
from database import AccountDatabase
from database import MessageDatabase

app = Flask(__name__)
accDB = AccountDatabase()
msgDB = MessageDatabase()


@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'


@app.route('/accounts', methods=['GET'])
def get_accounts():
    result = [{"id": id_, "login": login, "password": password}
              for id_, login, password in accDB.get_accounts()]
    print(result)
    return "db.get_accounts()"


@app.route('/accounts', methods=['POST'])
def add_new_account():
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    accDB.add_new_account(data["login"], data["password"])
    return {"status": "ok"}


@app.route('/accounts/auth', methods=['POST'])
def get_authorization():
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    result = accDB.get_authorization(data["login"], data["password"])
    if result:
        return {"auth": result}
    else:
        return {"auth": "rejected"}


@app.route('/accounts/<int:account_id>/password', methods=['POST'])
def change_password(account_id):
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    if not accDB.check_password(account_id, data["password"]):
        return {"status": "error", "message": "password is not correct"}
    accDB.change_password(account_id, data["new_password"])
    return {"status": "ok"}


@app.route('/accounts/<int:account_id>/login', methods=['POST'])
def change_login(account_id):
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    if not accDB.check_password(account_id, data["password"]):
        return {"status": "error", "message": "password is not correct"}
    accDB.change_login(account_id, data["new_login"])
    return {"status": "ok"}


if __name__ == '__main__':
    app.run()
