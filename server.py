import json
from flask import Flask, request
from database import AccountDatabase

app = Flask(__name__)
db = AccountDatabase()


@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'


@app.route('/accounts', methods=['GET'])
def get_account():
    result = [{"id": id_, "login": login, "password": password}
              for id_, login, password in db.get_account()]
    print(result)
    return "db.get_account()"


@app.route('/accounts', methods=['POST'])
def add_new_account():
    if not request.is_json:
        return {"status": "error", "message": "request should be in json"}
    data = json.loads(request.data)
    db.add_new_account(data["login"], data["password"])
    return {"status": "ok"}


@app.route('/accounts/<int:account_id>/password', methods=['POST'])
def change_password():
    return "db.change_password(account_id, new_password)"


@app.route('/accounts/<int:account_id>/login', methods=['POST'])
def change_login():
    return "db.change_login(account_id, new_login)"


if __name__ == '__main__':
    app.run()
