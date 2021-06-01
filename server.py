import json
from flask import Flask, request
from database import AccountDatabase

app = Flask(__name__)
accDB = AccountDatabase()


@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'


@app.route('/accounts', methods=['GET'])
def get_accounts():
    result = [{"id": id_, "login": login, "password": password}
              for id_, login, password in accDB.get_accounts()]
    print(result)
    return {"status": "ok"}


@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account_info(account_id):
    result = accDB.get_account_info(account_id)
    if result:
        return {"status": "ok", "login": result}
    else:
        return {"status": "error", "message": "account does not exist"}


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
        return {"status": "ok", "id": result}
    else:
        return {"status": "rejected"}


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


@app.route('/messages', methods=['POST'])
def send_message():
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    accDB.send_message(data["account_id"], data["dialog_id"], data["time"], data["message"])
    return {"status": "ok"}


@app.route('/messages/<int:account_id>', methods=['GET'])
def get_new_messages(account_id):
    #if not request.is_json:
    #    return {"status": "error", "message": "request should be in json"}
    #data = json.loads(request.data)
    accDB.get_new_messages(account_id)
    return {"status": "ok"}


@app.route('/dialogs/<int:user1_id>/<int:user2_id>', methods=['GET'])
def create_new_dialog(user1_id, user2_id):
    result = accDB.create_new_dialog(user1_id, user2_id)
    if result:
        return {"status": "ok"}
    else:
        return {"status": "error", "message": "dialog is already exist or users does not"}


if __name__ == '__main__':
    app.run()
