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
    if not accDB.check_password(data["account_id"], data["password"]):
        return {"status": "error", "message": "password is not correct"}
    accDB.send_message(data["account_id"], data["dialog_id"], data["time"], data["message"])
    return {"status": "ok"}


@app.route('/messages/<int:account_id>', methods=['POST'])
def get_all_messages(account_id):
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    if not accDB.check_password(account_id, data["password"]):
        return {"status": "error", "message": "password is not correct"}
    result = accDB.get_all_messages(account_id)
    if len(result) > 0:
        output = (("status", "ok"),
                  ("account_id0", result[0][0]),
                  ("dialog_id0", result[0][1]),
                  ("time0", result[0][2]),
                  ("message0", result[0][3]),
                  ("is_new0", result[0][4]))
        if len(result) > 1:
            for i in range(len(result) - 1):
                output += (("account_id" + str(i + 1), result[i + 1][0]),
                           ("dialog_id" + str(i + 1), result[i + 1][1]),
                           ("time" + str(i + 1), result[i + 1][2]),
                           ("message" + str(i + 1), result[i + 1][3]),
                           ("is_new" + str(i + 1), result[i + 1][4]))
            return json.dumps(dict(output))
        else:
            return json.dumps(dict(output))
    return {"status": "error", "message": "you do not have messages"}


@app.route('/messages/<int:account_id>/new', methods=['POST'])
def get_new_messages(account_id):
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    if not accDB.check_password(account_id, data["password"]):
        return {"status": "error", "message": "password is not correct"}
    result = accDB.get_all_messages(account_id)
    if len(result) > 0:
        output = (("status", "ok"),
                  ("account_id0", result[0][0]),
                  ("dialog_id0", result[0][1]),
                  ("time0", result[0][2]),
                  ("message0", result[0][3]))
        if len(result) > 1:
            for i in range(len(result) - 1):
                output += (("account_id" + str(i + 1), result[i + 1][0]),
                           ("dialog_id" + str(i + 1), result[i + 1][1]),
                           ("time" + str(i + 1), result[i + 1][2]),
                           ("message" + str(i + 1), result[i + 1][3]))
            return json.dumps(dict(output))
        else:
            return json.dumps(dict(output))
    return {"status": "error", "message": "you do not have new messages"}


@app.route('/dialogs/<int:user1_id>/<int:user2_id>', methods=['GET'])
def create_new_dialog(user1_id, user2_id):
    result = accDB.create_new_dialog(user1_id, user2_id)
    if result:
        return {"status": "ok", "dialog_id": result}
    else:
        return {"status": "error", "message": "dialog is already exist or users does not"}


@app.route('/dialogs/<int:user_id>', methods=['POST'])
def get_dialogs(user_id):
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    if not accDB.check_password(user_id, data["password"]):
        return {"status": "error", "message": "password is not correct"}
    result = accDB.get_dialogs(user_id)
    if len(result) > 1:
        output = (("status", "ok"),
                  ("dialog_id0", result[0][0]),
                  ("account_id0", result[0][1]))
        for i in range(len(result)-1):
            output += (("dialog_id"+str(i+1), result[i+1][0]),
                       ("account_id"+str(i+1), result[i+1][1]))
        return json.dumps(dict(output))
    elif len(result) == 1:
        return {"status": "ok", "dialog_id0": result[0][0], "account_id0": result[0][1]}
    return {"status": "error", "message": "you do not have dialogs"}


if __name__ == '__main__':
    app.run()
