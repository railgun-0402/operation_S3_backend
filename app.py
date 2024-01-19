from flask import Flask
from flask_cors import CORS
from func import db

app = Flask(__name__)
CORS(app)


@app.route('/')
def sample_py():
    return db.try_conn()


if __name__ == '__main__':
    app.run()
