from flask import Flask
from flask_cors import CORS
from func import db

app = Flask(__name__)
CORS(app)


# SQLの値をUserにアレンジ
def format(nodes):
    return [
        {
            "id": node[0],
            "name": node[1],
            "email": node[2],
            "password": node[3],
            "auth": node[4],
        }
        for node in nodes
    ]


@app.route('/')
def get_user_info():
    sql = 'SELECT * FROM users'

    # MySQL接続
    conn = db.conn_db()

    # user情報取得
    return format(db.try_conn(conn, sql))


if __name__ == '__main__':
    app.run()
