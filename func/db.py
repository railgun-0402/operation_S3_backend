import mysql.connector
import os


def sample():
    return 'Hello DB page!'


# DB接続情報
def conn_db():
    conn = mysql.connector.connect(
        host='localhost',
        user=os.environ['MYSQL_ID'],
        passwd=os.environ['MYSQL_PW'],
        db=os.environ['MYSQL_DB_QUIZ']
    )
    return conn


# DBに接続し、適当なデータを取りに行く
def try_conn():
    sql = 'SELECT * FROM users'
    try:
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

    except Exception as e:
        print('ERRORですね')
        print(e)

    for t_rows in rows:
        print('result:')
        print(t_rows)

    return rows
